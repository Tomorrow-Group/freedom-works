"""Copy each Thinking article's real image into the site, so cards and articles
no longer depend on Substack.

For every article in src/thinking it uses, in order:
  1. the first image in the article text, or
  2. the cover image of the original Substack post (its og:image).

Images are saved as src/thinking-img/<slug>.webp (max 1400px wide) and listed
in src/thinking-images.json. Both live in the source, so commit them to GitHub.
build.py copies them into the site on every build.

Run once (in Replit's Shell, or anywhere with internet access):
    pip install -r requirements.txt
    python3 fetch_thinking_images.py
    python3 build.py
Safe to re-run: articles that already have an image are skipped, so on Netlify
it only fetches images for new articles. If Substack can't be reached it
carries on, and those cards fall back to a brand film still.
"""
import io, json, os, re, sys, time
import requests
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
ARTICLES = os.path.join(ROOT, 'src', 'thinking')
OUT_DIR = os.path.join(ROOT, 'src', 'thinking-img')   # source folder: commit it to GitHub
MANIFEST = os.path.join(ROOT, 'src', 'thinking-images.json')
HEADERS = {'User-Agent': 'Mozilla/5.0 (compatible; FreedomWorksSiteBuild/1.0)'}

def frontmatter(text):
    m = re.match(r'---\n(.*?)\n---\n', text, re.S)
    out = {}
    for line in (m.group(1).splitlines() if m else []):
        if ': ' in line:
            k, v = line.split(': ', 1)
            out[k] = v.strip().strip('"')
    return out

def body_image(text):
    m = re.search(r'!\[[^\]]*\]\((https://[^)\s]+)\)', text)
    return m.group(1) if m else None

def cover_image(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=20)
        if r.status_code != 200:
            return None
        m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)', r.text) \
            or re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image', r.text)
        return m.group(1).replace('&amp;', '&') if m else None
    except requests.RequestException:
        return None

def save(url, dest):
    r = requests.get(url, headers=HEADERS, timeout=30)
    r.raise_for_status()
    im = Image.open(io.BytesIO(r.content)).convert('RGB')
    if im.width > 1400:
        im = im.resize((1400, round(im.height * 1400 / im.width)), Image.LANCZOS)
    im.save(dest, 'WEBP', quality=78, method=6)

def inline_urls(text):
    """Every image used inside an article: Markdown images and HTML <img> tags."""
    urls = re.findall(r'!\[[^\]]*\]\((https://[^)\s]+)\)', text) + re.findall(r'<img[^>]+src=["\'](https://[^"\']+)', text)
    seen = []
    for u in urls:
        u = u.replace('&amp;', '&')
        if u not in seen: seen.append(u)
    return seen

def fetch_inline(manifest):
    """Save a local copy of every in-article image (max 1400px wide), with its size, so the site never hotlinks Substack or Unsplash."""
    import hashlib
    inline = manifest.setdefault('_inline', {})
    d = os.path.join(OUT_DIR, 'inline'); os.makedirs(d, exist_ok=True)
    got = skipped = failed = 0
    for f in sorted(x for x in os.listdir(ARTICLES) if x.endswith('.md')):
        for url in inline_urls(open(os.path.join(ARTICLES, f), encoding='utf-8').read()):
            name = hashlib.sha1(url.encode()).hexdigest()[:16] + '.webp'; dest = os.path.join(d, name)
            if url in inline and os.path.exists(dest): skipped += 1; continue
            try:
                save(url, dest)
                w, h = Image.open(dest).size
                inline[url] = {'file': 'thinking/inline/' + name, 'w': w, 'h': h}; got += 1
            except Exception as e:
                failed += 1; print(f'  inline image failed: {url[:80]} ({e})')
    json.dump(manifest, open(MANIFEST, 'w'), indent=1)
    print(f'In-article images: {got} saved, {skipped} already there, {failed} failed (those keep their original address).')

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    manifest = json.load(open(MANIFEST)) if os.path.exists(MANIFEST) else {}
    files = sorted(f for f in os.listdir(ARTICLES) if f.endswith('.md'))
    got = skipped = missing = 0
    for i, f in enumerate(files, 1):
        text = open(os.path.join(ARTICLES, f), encoding='utf-8').read()
        fm = frontmatter(text)
        slug = fm.get('slug') or f[:-3]
        dest = os.path.join(OUT_DIR, slug + '.webp')
        if slug in manifest and (os.path.exists(dest) or (manifest[slug].get('none') and '--retry' not in sys.argv)):
            skipped += 1   # already saved, or already known to have no image (re-check with --retry)
            continue
        src, kind = body_image(text), 'article'
        if not src and fm.get('originalUrl'):
            src, kind = cover_image(fm['originalUrl']), 'cover'
            time.sleep(0.4)
        if not src:
            missing += 1
            manifest[slug] = {'none': True}
            json.dump(manifest, open(MANIFEST, 'w'), indent=1)
            print(f'[{i}/{len(files)}] no image found: {slug}')
            continue
        try:
            save(src, dest)
            manifest[slug] = {'file': f'thinking/{slug}.webp', 'src': src, 'from': kind}
            got += 1
            print(f'[{i}/{len(files)}] saved ({kind}): {slug}')
        except Exception as e:
            missing += 1
            print(f'[{i}/{len(files)}] failed: {slug} ({e})')
        json.dump(manifest, open(MANIFEST, 'w'), indent=1)
    print(f'\nDone: {got} saved, {skipped} already there, {missing} without an image.')
    fetch_inline(manifest)
    print('Now run: python3 build.py')

if __name__ == '__main__':
    sys.exit(main())
