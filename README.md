# Freedom Works website

Static site for freedom.works. Every page is plain HTML in `site/`, generated from the files in `src/` by `build.py`.

## How publishing works
- `main` is the live site. Anything merged into `main` is rebuilt and published by Netlify in about a minute.
- Changes made on another branch get a private Netlify **Deploy Preview** link to check before merging.
- Every change is recorded in GitHub, so any version can be restored.

## Where things live
| What | File |
|---|---|
| Copy, case studies, quotes, services, page structure | `build.py` |
| Homepage hero and Explore list | `src/home-main.html` |
| Design (one stylesheet: tokens, colour grounds, grid, type, components, page templates, motion) | `src/site.css` |
| Motion, header and menu behaviour, and the HubSpot form loader and styling | `src/flourish.js` |
| WebGL effects (red flow, ripple, footer wordmark) | `src/shaders.js` |
| Articles | `src/thinking/*.md` |
| Images, films, fonts, logos | `site/assets/` |
| Culture3 logo | `c3-logo.svg` |

Do not edit the HTML files in `site/` directly: the next build overwrites them. Edit the source above instead.

Design notes: `AUDIT.md` (what was wrong) and `CHANGELOG-design.md` (what changed and why). Before and after screenshots are in `qa/`.

## Build locally (optional)
```
pip install -r requirements.txt
python3 build.py
```
Then open `site/index.html`, or run `python3 -m http.server 8080 --directory site`.

## Also included
- `netlify.toml`: Netlify build and caching settings
- `site/_redirects` (Netlify) and `site/.htaccess` (cPanel/Apache): old addresses redirect to new pages
- `.replit`: lets the same project run on Replit if needed

## Thinking images (run once, then commit)
Copies each article's real image (or its Substack cover image) into src/thinking-img/ and lists them in
src/thinking-images.json. Commit both to GitHub. Every build copies them into the site, and Netlify re-runs
the fetch on each build, so new articles get their images automatically:
```
pip install -r requirements.txt
python3 fetch_thinking_images.py
python3 build.py
```
Articles with no image at all show a branded type card instead.

## Brand fonts and licences
- Headlines: Super Castel XCond (Production Type). The files in site/assets/fonts/castel-*.woff2 are TRIAL versions with a limited character set. Replace them with the licensed web fonts (same file names) before launch.
- Fallback / long-form serif: Instrument Serif (open licence).
- Labels and navigation: Barlow Condensed (open licence).
- Body: Hanken Grotesk (open licence).

## Service pages (not live yet)
One page per service and sub-service, built from src/service_pages.py (Brand strategy and its three sub-services so far).
They are switched OFF: set SERVICE_PAGES_LIVE = True near the top of the service-pages block in build.py to publish them,
add them to the sitemap and make their URLs live (/services/brand-strategy/ and below).
