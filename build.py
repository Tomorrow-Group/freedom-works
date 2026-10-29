import urllib.parse
import os, re, json, html, base64, shutil, datetime
ROOT = os.path.dirname(os.path.abspath(__file__))
def SP(*a): return os.path.join(ROOT, 'src', *a)
import markdown

SRC = os.path.join(ROOT, 'site')                    # existing home build + assets
OUT = os.path.join(ROOT, 'site')
THINK = SP('thinking')
PREVIEW_MODE = [False]
DOMAIN = 'https://freedom.works'

CSS = open(SP('site.css')).read()   # the whole design system: tokens, grounds, layout, type, components, templates, motion
HOME_MAIN = open(SP('home-main.html')).read()

NAV = [('services/', 'Services'), ('work/', 'Work'), ('agency/', 'About'), ('the-guild/', 'The Guild'),
       ('culture3/', 'Culture3'), ('thinking/', 'Thinking'), ('contact/', 'Talk to us')]
TAGS = {'ai-and-creativity': 'AI and creativity', 'on-the-model': 'The agency model', 'talent-and-work': 'Talent and work',
        'culture-and-ads': 'Culture and advertising', 'purpose': 'Purpose'}

def esc(t): return html.escape(t, quote=True)
def month(d):
    dt = datetime.date.fromisoformat(d); return dt.strftime('%B %Y')

# ---------------- data ----------------
PROJECTS = [
    dict(slug='king-arthur-baking', img='poster-king-arthur', loop='king-arthur', client='King Arthur Baking', camp='Keep Rising', vimeo=('1156877036', ''),
         short='A creative platform that celebrates the essence of the King Arthur brand and drives differentiation in a low interest category.', res='From #3 to #1 flour brand in the US. Doubled sales.', stat='+100%',
         copy='Our Keep Rising platform helped King Arthur become the #1 flour brand in the US, driving a 100% sales uplift and adding 3.4m households. A leading FMCG example of emotional storytelling driving commercial growth.',
         n='+100%', l='Sales uplift', extra=['#1 flour brand in the US', '+3.2pt share gain', '+3.4m new households'],
         quote=("Keep Rising has been transformative for King Arthur Baking. Not just creatively, but commercially. In a low interest category, The Guild helped us connect on a deeper emotional level. They captured our brand\u2019s purpose with humanity and craft, and the results speak for themselves: record market share, millions of new households, and the highest repeat rate in the category.", 'Kim Stellavato', 'Brand Director, King Arthur Baking'), home=True),
    dict(slug='wizz-air', img='poster-wizz-air', loop='wizz-air', client='Wizz Air', camp='Locos for Low Cost', vimeo=('1156877642', ''),
         short="The airline\u2019s first fully AI powered campaign, a human idea scaled by AI.", res='+11.4% demand, year on year.', stat='+11.4%',
         copy="Wizz Air\u2019s first fully AI powered campaign, created through our partnership with Monks, delivered 17 broadcast ready assets in three weeks. A human idea scaled by AI. A new model for airlines needing fast, high impact campaigns.",
         n='+11.4%', l='Increase in demand, year on year', extra=['17 TV, OOH, and social assets', 'Delivered in three weeks'],
         quote=("Locos is about letting go, embracing spontaneity, and leaning into life\u2019s fun side. Because low cost isn\u2019t only about saving money, it\u2019s about having the freedom to do more and live bigger. Wizz Air has, from its inception, been a digital-first company, so it makes sense that we would be at the leading edge of using new technology in all areas of our business. So making an all AI ad just makes sense.", 'Silvia Mosquera Gonz\u00e1lez', 'Commercial Officer Central, Wizz Air'), home=True),
    dict(slug='ms-food', img='poster-ms-food', loop='ms-food', client='M&S Food', camp='Magic Really Does Sell', vimeo=('1156877368', ''),
         short='Our script provided the creative fuel that allowed M&S\u2019s inhouse team to reunite French & Saunders to bring back the joy of Christmas.', res='+10.2% sales.', stat='+10.2%',
         copy="Working with M&S Food\u2019s in-house team, we created the idea to reunite Dawn French and Jennifer Saunders, delivering a Christmas campaign that lifted sales by 10.2%. Cultural storytelling turning into real retail impact.",
         n='+10.2%', l='Sales', extra=[],
         quote=("M&S outperformed the market in food in both volume and value for the second year running. The retailer\u2019s high-end food offer traditionally appeals to shoppers at Christmas, and 2022 was no exception despite increasing economic pressure on consumers.", 'Stuart Machin', 'Chief Executive, M&S'), home=True),
    dict(slug='loveholidays', img='poster-loveholidays', loop='loveholidays', client='loveholidays', camp='At Your Fingertips', vimeo=('1156877210', ''),
         short='From performance to brand, without losing demand.', res='+72% consideration, \u201342% cost per click, + a million people to their ATOL licence.', stat='+72%',
         copy='We helped loveholidays shift from performance to brand, lifting awareness +15pts and consideration +72%, driving demand that required 1m extra ATOL licences. Proof that brand and performance work better together in travel.',
         n='+72%', l='Consideration', extra=['\u201342% cost per click', '+15pts awareness', '1m extra ATOL licences'],
         quote=("Since starting our brand journey with The Liberty Guild, we\u2019ve added nearly 15%pts of awareness and seen every brand metric we track increase at pace, while our competitors are flat or falling, all despite dramatically lower brand budgets.", 'Al Murray', 'CMO, loveholidays'), home=True),
    dict(slug='rowse-honey', img='poster-rowse', loop='rowse', client='Rowse Honey', camp='The Squeeze That Protects the Bees', vimeo=('1156877553', ''),
         short='Repositioned as the purpose led choice, with bee welfare at its heart.', res='+24% new customers.', stat='+24%',
         copy='We repositioned Rowse Honey as a purpose led choice, putting bee welfare at the heart of the brand. The work attracted +24% more new customers and delivered a 98th percentile brand power score. Proving that doing good can drive both growth and equity.',
         n='+24%', l='New customers', extra=['98th percentile brand power'], quote=None, home=True),
    dict(slug='brompton', img='poster-brompton', loop='brompton', client='Brompton', camp='Life Unfolded', vimeo=('1156876773', ''),
         short='', res='50th anniversary film.', stat='50',
         copy="There\u2019s a confidence that comes from knowing who you are. The film we created for Brompton\u2019s 50th anniversary leans into that. Life Unfolded doesn\u2019t look back, it launches the brand forward.",
         n='50', l='Years of Brompton, launched forward', extra=[],
         quote=("We were looking for a partner who truly understood the spirit of Brompton, not just as a mode of transport, but as a way of moving through life with freedom, creativity, and purpose. The Liberty Guild\u2019s fresh, unique global model and deep cultural insight made them the perfect fit to help us inspire a new wave of riders around the world.", 'Chris Willingham', 'Global CMO, Brompton'), home=True),
    dict(slug='snowfox-group', img='poster-snowfox', loop='snowfox', herofilm='snowfox-film', client='Snowfox Group', camp='One Platform to Grow', vimeo=None,
         short='Four sushi brands unified under one strategic platform.', res='$621m acquisition by Zensho.', stat='$621m',
         copy='We unified four Snowfox sushi brands under one strategic platform, strengthening identity and commercial performance, contributing to a $621m acquisition by Zensho. A retail food example of brand architecture driving enterprise value.',
         n='$621m', l='Acquisition by Zensho', extra=['Four sushi brands, one platform'], quote=None, home=False),
    dict(slug='kitkat-f1', img='poster-kitkat', loop='kitkat', client='KitKat', camp='F1 Ident', vimeo=('1156877162', ''),
         short='Handpicked production power for Formula 1 launch film.', res='Watch the film', stat='', copy='', n='', l='', extra=[], quote=None, home=False),
    dict(slug='nestle-sma', img='poster-sma', loop='sma', client='Nestl\u00e9 SMA', camp='Go With Your Gut', vimeo=('1203806335', '054f9189f0'),
         short='Building trust long before parents choose formula.', res='2x Baby Club sign-ups.', stat='2x',
         copy="Working with Nestl\u00e9\u2019s Content Studio, we helped SMA\u00ae shift the conversation from infant formula to genuine support, creating a campaign that brought its unique Baby Club services to life and positioned the brand as a trusted companion from pregnancy through to baby\u2019s first months.",
         n='2x', l='Baby Club sign-ups', extra=[],
         sections=[
          ('The brief', 'Build trust long before parents choose formula.', ["Around 70% of parents don\u2019t expect to formula feed when they first become pregnant. But almost all are looking for trusted advice, reassurance and expert guidance as they prepare for life with a new baby.", "SMA\u00ae already offered something genuinely different: a Baby Club providing access to qualified midwives, a 24/7 Careline, educational content, and expert guidance throughout the parenting journey.", "Our challenge wasn\u2019t creating another baby club. It was showing parents that SMA\u00ae is there whenever they need someone to turn to."], None),
          ('The idea', 'Go With Your Gut.', ["Becoming a parent doesn\u2019t just bring questions. It brings a constant stream of opinions, from family, friends, social media, Google, and experts. Everyone seems to have the right answer. But parents aren\u2019t looking for perfect answers. They\u2019re looking for someone they can trust.", "So the most valuable thing SMA\u00ae could give them wasn\u2019t more advice. It was the confidence to trust themselves. \u2018Go With Your Gut\u2019 encourages parents to trust their own instincts, knowing expert support is always there whenever they need reassurance.", "Rather than positioning SMA\u00ae Baby Club as another voice telling parents what to do, we positioned it as the trusted companion that helps parents feel confident in the decisions that are right for their family."], None),
          ('The execution', 'Real parents. Real moments.', ["Authenticity sat at the heart of the campaign. Rather than scripted performances, we worked with real parents whose experiences reflected the realities of early parenthood.", "The creative was designed to feel creator-led, intimate and relatable, capturing the emotional highs, and lows that every parent experiences. This allowed SMA\u00ae to show up not as an advertiser, but as a trusted source of reassurance."], None),
          ('The Baby Club', 'Support that goes beyond nutrition.', ["The Baby Club brings together expert support designed around the questions parents ask every day.", "Each service demonstrates the same belief: parents don\u2019t need all the answers. They just need to know someone is there to help."], ['Midwife Live Chat', '24/7 Careline', 'Baby gut health education', 'Parenting podcast series']),
         ],
         gallery=['sma-1', 'sma-2', 'sma-3', 'sma-4'],
         quote=("I really couldn\u2019t have hoped for better. We can all collectively take pride in the achievement. Not just the creative but the fact we\u2019re here. Infant nutrition is one of Nestl\u00e9\u2019s most protected categories and notoriously hard to navigate in creatively. And also throw in the biggest global crisis Nestl\u00e9 has had in well over a decade on the most sensitive of products, the reception is amazing. It\u2019s testament to The Guild\u2019s Amplify product, the process and the amazing talent you brought to the table. Thank you.", 'Tom Nixon', 'Head of Content Studios UK&I, Nestl\u00e9'), home=False),
    dict(slug='tui', img='poster-tui', loop='tui', client='TUI', camp='Skip To The Good Bit', vimeo=('1203813505', '5dd01fa66a'),
         short='A global brand platform that lets travellers start enjoying their holiday long before they leave home.', res='9 markets globally.', stat='', copy='', n='', l='', extra=[],
         quote=("The Liberty Guild have been a delight to work with. Their interpretation and understanding of our brief helped crystallise the strategic approach, which then went on to create some creative work that brought to life the proposition in a way that will allow us to flex across markets. In conjunction with DEPT we went on to create an ad using AI. The Liberty Guild project managed the whole process, making it seem like a breeze for me!", 'Rachel Moss', 'Head of International Marketing, TUI Group'), home=False),
]

VOICES = [
    ("In a sea of sameness, The Liberty Guild [now Freedom Works] is a breath of fresh air. A thoroughly modern, no-nonsense approach to applied strategic creative thinking.", 'Nick Tate', 'ex VP Head of Next, Haleon Plc'),
    ("We were looking for a partner who truly understood the spirit of Brompton, not just as a mode of transport, but as a way of moving through life with freedom, creativity, and purpose.", 'Chris Willingham', 'Global CMO, Brompton'),
    ("What\u2019s great about their offering is the global reach of their network. The ability to tap into creatives and strategists from across the globe whilst still having the expert support of a centrally managed account team gives us the best of both worlds.", 'Gemma Schmid', 'ex-Director of Brand Marketing, loveholidays'),
    ("The Liberty Guild [now Freedom Works] do more than just brilliant ideas delivered with beautiful precision, it\u2019s the soap box to elevate the in-house voice at the very heart of our brands. Bringing the best of outside, inside.", 'Tom Nixon', 'Head of Content Studios UK&I, Nestl\u00e9'),
    ("Its sheer audacity and its willingness to rip up the rule book to create a creative business for our new world.", 'The Drum', 'Grand Prix jury, The Drum Awards 2021'),
    ("Liberty Guild [now Freedom Works] is a breath of fresh air having worked in the industry for over 20 years now. The process and the set-up is really adapted to the way consumer communication has evolved: fluid, media agnostic, agile, and very consumer driven.", 'Estrella Lopez-Brea', 'ex-Global Head of Insights, CPW'),
]


def now_fw(text):
    """Client quotes predate the rename: tag the first mention of the old name, as agreed."""
    return re.sub(r'\b(The Liberty Guild|Liberty Guild)(\u2019s)?(?! \[now)', lambda m: m.group(1) + ' [now Freedom Works]' + (m.group(2) or ''), text, count=1)
VOICES = [(now_fw(q), n, r) for q, n, r in VOICES]
for _p in PROJECTS:
    if _p['slug'] == 'nestle-sma': _p['quote'] = None   # not signed off for public use yet
    if _p.get('quote'): _p['quote'] = (now_fw(_p['quote'][0]),) + tuple(_p['quote'][1:])

def voices_html(items, label='What clients say', foot='', theme=''):
    slides = ''.join(f'<figure class="slide{" on" if i == 0 else ""}"><blockquote>\u201c{esc(q)}\u201d</blockquote><figcaption class="who">{esc(n)}<span>{esc(t)}</span></figcaption></figure>' for i, (q, n, t) in enumerate(items))
    head = ('<div class="sec-head"><h2 class="sec-title">What clients <span class="thin">say</span></h2></div>' if theme
            else '<p class="sec-lbl"><span class="mk" aria-hidden="true"></span>' + esc(label) + '</p>')
    return f'<section class="voice voices wrap dark{(" " + theme) if theme else ""}" aria-label="What clients say" aria-roledescription="carousel">{head}{slides}<div class="ctrl"><button type="button" data-prev aria-label="Previous quote"><svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M10 3L5 8l5 5" fill="none" stroke="currentColor" stroke-width="1.5"/></svg></button><button type="button" data-next aria-label="Next quote"><svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M6 3l5 5-5 5" fill="none" stroke="currentColor" stroke-width="1.5"/></svg></button><button type="button" data-toggle aria-pressed="false" aria-label="Pause quotes"><svg class="i-pause" width="14" height="14" viewBox="0 0 14 14" aria-hidden="true"><rect x="3" y="2" width="2.5" height="10" fill="currentColor"/><rect x="8.5" y="2" width="2.5" height="10" fill="currentColor"/></svg><svg class="i-play" width="14" height="14" viewBox="0 0 14 14" aria-hidden="true"><path d="M4 2l8 5-8 5z" fill="currentColor"/></svg></button><span class="count">1 / {len(items)}</span></div>' + (f'<p class="voice-foot">{esc(foot)}</p>' if foot else '') + '</section>'

AUTHOR_LINKEDIN = {'Jon Williams': 'https://www.linkedin.com/in/creativegenius/', 'Aim\u00e9e Luther': 'https://www.linkedin.com/in/aimeeluther/'}

def load_posts():
    posts = []
    for f in sorted(os.listdir(THINK)):
        if not f.endswith('.md'): continue
        raw = open(os.path.join(THINK, f)).read()
        m = re.match(r'---\n(.*?)\n---\n\n?(.*)', raw, re.S)
        fm = {}
        for line in m.group(1).splitlines():
            k, v = line.split(': ', 1); fm[k] = json.loads(v)
        fm['body_md'] = m.group(2)
        posts.append(fm)
    posts.sort(key=lambda p: p['date'], reverse=True)
    return posts
POSTS = load_posts()
for _p in POSTS:   # article titles show with typographic apostrophes wherever they appear (bodies are left as written)
    _p['title'] = re.sub(r"(?<=\w)'(?=\w)", '\u2019', _p['title'])
# Authors: only those confirmed from the articles' own sign-offs (src/confirmed_authors.json); everything else is credited to
# Freedom Works until confirmed. To confirm more, add [slug, name] pairs to that file.
_CONF = {s_: a for s_, a in json.load(open(SP('confirmed_authors.json'), encoding='utf-8'))} if os.path.exists(SP('confirmed_authors.json')) else {}
for _p in POSTS: _p['author'] = _CONF.get(_p['slug'], 'Freedom Works')
AUTHOR_ROLE = {'Jon Williams': 'Founder and Chief Creative Officer', 'Aim\u00e9e Luther': 'Managing Director'}   # add Aim\u00e9e's role here once confirmed
TOPIC_SLUG = {'ai-and-creativity': 'ai-and-creativity', 'on-the-model': 'the-agency-model', 'talent-and-work': 'talent-and-work',
              'culture-and-ads': 'culture-and-advertising', 'purpose': 'purpose'}
TOPIC_INTRO = {
    'ai-and-creativity': 'What AI changes for creativity, and what it never will. Our thinking on using AI for process and production, while people stay in charge of the ideas.',
    'on-the-model': 'How agencies are built, paid, and run, and why the old model is creaking. Our thinking on independent talent, charging for ideas, and building an agency fit for the next ten years.',
    'talent-and-work': 'The people who make the work, and how they want to work. Our thinking on independent talent, distributed teams, and getting the best creative minds onto every brief.',
    'culture-and-ads': 'Where brands meet culture, and what it takes to earn a place there. Our thinking on campaigns, cultural moments, and the ideas that get people talking.',
    'purpose': 'Purpose that\u2019s real, and purpose that\u2019s just words. Our thinking on brands, responsibility, and doing good in a way people believe.'}
TOPIC_SVC = {'ai-and-creativity': ('AI production', 'Creative'), 'on-the-model': ('In-house creative', 'Creative'),
             'talent-and-work': ('Creative', 'In-house creative'), 'culture-and-ads': ('Campaign strategy and development', 'Brand and product launches'),
             'purpose': ('Brand positioning', 'Brand strategy')}
_clash = [t for t in TOPIC_SLUG.values() if any(_p['slug'] == t for _p in POSTS)]
assert not _clash, f'topic page address clashes with an article: {_clash}'

FAQ = [
    ("Who are Freedom Works?", "A global creative agency built on Calibre, Culture and Craft. More than 600 award winning independent creatives and strategists across 37 countries and cultures, led by a founder and leadership team who have run businesses, boutique agencies, global networks, production companies, and start-ups."),
    ("How do you work?", "We run a distributed creative department. No buildings. No fixed teams. For every brief we build a bespoke team from our network, supported by insight from qual, quant, or behavioural science research, with workflow optimised through our tech stack. We use AI when it helps, and we don't when it doesn’t. We can run everything end to end, or plug into your in-house team."),
    ("How are you different to a legacy agency?", "We don't sell hours. We sell ideas. Our work is productised: fixed scope, fixed cost, fixed time, clear outputs. We work in short sprints, with proper decision points and evidence built in, and when clients want more, a subscription model makes it cheaper and easier."),
    ("What makes your talent better?", "Every project starts by finding the right people for the brief. Not whoever's free. Not whoever's cheapest. Our creatives value the freedom to work on their own terms, on briefs they choose, and between them they've won 2,315 Lions, Pencils, and Effies."),
]

# ---------------- page bodies ----------------
def hs_form(uid='hs-form'):
    return f'''<div class="hs-wrap" data-hs-portal="{HS_PORTAL}" data-hs-form="{HS_FORM}">
      <div class="hs-target" id="{uid}"></div>
      <p class="hs-fallback"><a class="ct-btn" data-cta="start-enquiry" href="{HS_SHARE}" target="_blank" rel="noopener">Start your enquiry <span aria-hidden="true">\u2192</span></a></p>
    </div>'''

def contact_cards(big=False, hl='h3', L=None):
    return f'''<div class="ct-cards{" big" if big else ""}">
      <div class="ct-card form-card">
        <{hl}>How can we help?</{hl}>
        {hs_form()}
        {('<p class="ct-note">By submitting this form, Freedom Works will use the information you provide to respond to your enquiry. See our <a href="' + L('privacy/') + '">Privacy Policy</a> and <a href="' + L('cookies/') + '">Cookie Policy</a> for more information.</p>') if L else ''}
      </div>
    </div>'''

def cta(L):
    return f'''<section class="contact" aria-labelledby="ct">
  <div class="wrap">
    <h2 id="ct">Let’s make <span class="thin">work that matters.</span></h2>
    {contact_cards(L=L)}
  </div>
</section>'''

def case_desc(p):
    return fit_desc(p['short'] or f"{p['client']}: {p['camp']}.", p['copy'])

def vimeo_url(p):
    vid, h = p['vimeo']
    return f'https://vimeo.com/{vid}' + (f'/{h}' if h else '')

def vim_attrs(p):
    if not p.get('vimeo'): return ''
    vid, h = p['vimeo']
    return f' data-vimeo="{vid}"' + (f' data-h="{h}"' if h else '')

def num_html(n):
    """Stat markup: the number is animated by the count-up; % and $ are set as raised units
    (they aren't in the trial Castel font, so they render as a deliberate typographic unit, not a stray fallback)."""
    m = re.match(r'^([^0-9]*)([0-9][0-9,.]*)(.*)$', n)
    if not m: return esc(n)
    unit = lambda t: re.sub(r'([%$])', r'<span class="u">\1</span>', esc(t))
    pre, num, suf = m.groups()
    return f'{unit(pre)}<span class="num">{esc(num)}</span>{unit(suf)}'

# Client logos per service page (Emmaclare's list in the copy deck). A logo without an image file yet shows as a typeset name,
# and switches to the real logo as soon as site/assets/logos/wall/<slug>-ink.png is added.
LOGO_NAMES = {'rowse-honey': 'Rowse Honey', 'snowfox-group': 'Snowfox Group', 'nasstar': 'Nasstar'}
LOGO_EXTRA_H = {'snowfox-group': 54, 'rowse-honey': 50, 'nasstar': 28}   # height in px for logos not on the homepage wall
def svc_logos(sp, A):
    wall = {x['slug']: x for x in LOGOWALL}
    slugs = sp.get('logos')
    if slugs is None: slugs = [x['slug'] for x in LOGOWALL[:8]]
    out = []
    for sl in slugs:
        x = wall.get(sl); f = os.path.join(OUT, 'assets', 'logos', 'wall', sl + '-ink.png')
        if x and os.path.exists(f):
            out.append(f'<li><img src="{A("logos/wall/"+sl+"-ink.png")}" alt="{esc(x["name"])}" style="max-height:{min(44, 1500 / x["w"]):.0f}px" loading="lazy"></li>')
        elif os.path.exists(f):
            out.append(f'<li><img src="{A("logos/wall/"+sl+"-ink.png")}" alt="{esc(LOGO_NAMES.get(sl, sl))}" style="max-height:{LOGO_EXTRA_H.get(sl, 36)}px" loading="lazy"></li>')
        else:
            out.append(f'<li><span class="logo-name">{esc((x or {}).get("name") or LOGO_NAMES.get(sl, sl))}</span></li>')
    return ''.join(out)

# Client logo at the top of each case study (full colour: it's the client's own page)
CASE_LOGO = {'king-arthur-baking': 'king-arthur', 'wizz-air': 'wizz-air', 'ms-food': 'm-and-s-food', 'loveholidays': 'loveholidays',
             'rowse-honey': 'rowse-honey', 'brompton': 'brompton', 'snowfox-group': 'snowfox-group', 'tui': 'tui',
             'kitkat-f1': 'nestle', 'nestle-sma': 'nestle'}          # KitKat and SMA are Nestle brands: Nestle logo plus the brand name
CASE_BRAND = {'kitkat-f1': 'KitKat', 'nestle-sma': 'SMA'}
def case_logo(p, A):
    sl = CASE_LOGO.get(p['slug']); wall = {x['slug']: x for x in LOGOWALL}
    if not sl or not os.path.exists(os.path.join(OUT, 'assets', 'logos', 'wall', sl + '-col.png')):
        return f'<p class="client">{esc(p["client"])}</p>'
    h = round(min(104, 3600 / wall[sl]['w'])) if sl in wall else {'snowfox-group': 132, 'rowse-honey': 120}.get(sl, 100)
    name = wall[sl]['name'] if sl in wall else LOGO_NAMES.get(sl, p['client'])
    tag = f'<span class="client-tag">{esc(CASE_BRAND[p["slug"]])}</span>' if p['slug'] in CASE_BRAND else ''
    return f'<p class="client client-has-logo"><img class="client-logo" src="{A("logos/wall/"+sl+"-col.png")}" alt="{esc(name)}" style="max-height:{h}px">{tag}</p>'

# ---------------- Case studies: copy deck section 7 (simplified, one structure throughout) ----------------
# Logo, headline, film, case copy, headline stat + supporting results, quote, next project. No extra sections or galleries.
CASE_COPY = {
 'king-arthur-baking': dict(copy='Our Keep Rising platform helped King Arthur become the #1 flour brand in the US, driving a 100% sales uplift and adding 3.4m households. A leading FMCG example of emotional storytelling driving commercial growth.',
    n='+100%', l='Sales uplift', extra=['#1 flour brand in the US', '+3.2pt share gain', '+3.4m new households'],
    quote=('Keep Rising has been transformative for King Arthur Baking. Not just creatively, but commercially. In a low interest category, The Guild helped us connect on a deeper emotional level. They captured our brand\u2019s purpose with humanity and craft, and the results speak for themselves: record market share, millions of new households, and the highest repeat rate in the category.', 'Kim Stellavato', 'Brand Director, King Arthur Baking')),
 'wizz-air': dict(copy='Wizz Air\u2019s first fully AI powered campaign, created through our partnership with Monks, delivered 17 broadcast ready assets in three weeks. A human idea scaled by AI. A new model for airlines needing fast, high impact campaigns.',
    n='+11.4%', l='Increase in demand, year on year', extra=['17 TV, OOH, and social assets', 'Delivered in three weeks'],
    quote=('Locos is about letting go, embracing spontaneity, and leaning into life\u2019s fun side. Because low cost isn\u2019t only about saving money, it\u2019s about having the freedom to do more and live bigger. Wizz Air has, from its inception, been a digital-first company, so it makes sense that we would be at the leading edge of using new technology in all areas of our business. So making an all AI ad just makes sense.', 'Silvia Mosquera Gonz\u00e1lez', 'Commercial Officer Central, Wizz Air')),
 'ms-food': dict(copy='Working with M&S Food\u2019s in-house team, we created the idea to reunite Dawn French and Jennifer Saunders, delivering a Christmas campaign that lifted sales by 10.2%. Cultural storytelling turning into real retail impact.',
    n='+10.2%', l='Sales', extra=[],
    quote=('M&S outperformed the market in food in both volume and value for the second year running. The retailer\u2019s high-end food offer traditionally appeals to shoppers at Christmas, and 2022 was no exception despite increasing economic pressure on consumers.', 'Stuart Machin', 'Chief Executive, M&S', '\u201cWine and sequins help UK\u2019s M&S sparkle at Christmas\u201d, 12 January 2023')),
 'loveholidays': dict(copy='We helped loveholidays shift from performance to brand, lifting awareness +15pts and consideration +72%, driving demand that required 1m extra ATOL licences. Proof that brand and performance work better together in travel.',
    n='+72%', l='Consideration', extra=['\u201342% cost per click', '+15pts awareness', '1m extra ATOL licences'],
    quote=('Since starting our brand journey with The Liberty Guild, we\u2019ve added nearly 15% pts of awareness and seen every brand metric we track increase at pace, while our competitors are flat or falling, all despite dramatically lower brand budgets.', 'Al Murray', 'CMO, loveholidays')),
 'rowse-honey': dict(copy='We repositioned Rowse Honey as a purpose led choice, putting bee welfare at the heart of the brand. The work attracted +24% more new customers and delivered a 98th percentile brand power score. Proving that doing good can drive both growth and equity.',
    n='+24%', l='New customers', extra=['98th percentile brand power'],
    quote=('The most integrated model I have seen when it comes to creative development. And yet it is so obvious that if you embed the consumer into the creative development process and are guided by the data and not the creative ego you are going to get better, more effective work.\nSo many others have tried and failed. But the Liberty Guild process is seamless.', 'Kirstie Jamieson', 'Marketing Director, Rowse Honey')),
 'brompton': dict(copy='There\u2019s a confidence that comes from knowing who you are. The film we created for Brompton\u2019s 50th anniversary leans into that. Life Unfolded doesn\u2019t look back, it launches the brand forward.',
    n='50', l='Years of Brompton, launched forward', extra=[],
    quote=('We were looking for a partner who truly understood the spirit of Brompton, not just as a mode of transport, but as a way of moving through life with freedom, creativity, and purpose. The Liberty Guild\u2019s fresh, unique global model and deep cultural insight made them the perfect fit to help us inspire a new wave of riders around the world.', 'Chris Willingham', 'Global CMO, Brompton')),
 'snowfox-group': dict(copy='We unified four Snowfox sushi brands under one strategic platform, strengthening identity and commercial performance, contributing to a $621m acquisition by Zensho. A retail food example of brand architecture driving enterprise value.',
    n='$621m', l='Acquisition by Zensho', extra=['Four sushi brands, one platform'],
    quote=('You [Freedom Works] delivered brilliantly throughout, provided amazing creativity and moral support and (most importantly) you were great fun to work with.', 'Simon Clough', 'Strategic Brand Consultant, Snowfox Group')),
 'kitkat-f1': dict(copy='Nestl\u00e9\u2019s Inhouse Studio needed extra production power for their KitKat x Formula 1 launch film. We handpicked the specialists and set up the workflow to get everyone working as one team.',
    n='', l='', extra=[],
    quote=('The Liberty Guild do more than just brilliant ideas delivered with beautiful precision, it\u2019s the soap box to elevate the in-house voice at the very heart of our brands. Bringing the best of outside, inside, it\u2019s where brand knowledge meets creative prowess to deliver magic results. Agility in this fast moving new age is paramount, and Freedom Works, [formerly The Liberty Guild] flexibility delivers us that in spades\u2026', 'Tom Nixon', 'Head of Content Studios UK&I, Nestl\u00e9')),
 'nestle-sma': dict(copy='Working with Nestl\u00e9\u2019s Content Studio, we helped SMA\u00ae shift the conversation from infant formula to genuine support, creating a campaign that brought its unique Baby Club services to life and positioned the brand as a trusted companion from pregnancy through to baby\u2019s first months.',
    n='2x', l='Baby Club sign-ups', extra=[],
    quote=('I can now assemble a team through The Guild within a few days\u2019 notice that has more Cannes Lions and D&AD Pencils within it than all of our agency accounts put together.', 'Tom Nixon', 'Head of Content Studios UK&I, Nestl\u00e9')),
 'tui': dict(copy='We helped TUI Hotels reclaim what made travel joyful by creating a global brand platform that lets travellers start enjoying their holiday long before they leave home. \u2018Skip to the Good Bit\u2019 positions TUI Hotels as the brand that has already done the hard work, so customers don\u2019t have to. Brought to life through an entirely AI produced launch campaign.',
    n='', l='', extra=[],
    quote=('Freedom Works [formerly The Liberty Guild] have been a delight to work with. Their interpretation and understanding of our brief helped crystallise the strategic approach, which then went on to create some creative work that brought to life the proposition in a way that will allow us to flex across markets. In conjunction with DEPT we went on to create an ad using AI. The Liberty Guild project managed the whole process, making it seem like a breeze for me!', 'Rachel Moss', 'Head of International Marketing, TUI Group')),
}
for _p in PROJECTS:
    if _p['slug'] in CASE_COPY:
        _p.update(CASE_COPY[_p['slug']])
    _p['sections'] = []; _p['gallery'] = []

def tidy_pending(body):
    """Hide leadership details that haven't been supplied yet, so the live page never shows placeholders."""
    body = body.replace('<p class="role"><span class="pending-tag">Role to confirm</span></p>', '')
    body = re.sub(r'<ul class="pstats pending">.*?</ul>', '', body, flags=re.S)
    def mono(m):
        name = html.unescape(m.group(1)); ini = ''.join(w[0] for w in name.split()[:2]).upper()
        return f'<div class="ph ph-mono" aria-hidden="true"><span>{ini}</span></div><div class="lr-txt"><h3>{m.group(1)}</h3>'
    return re.sub(r'<div class="ph">Portrait to come</div><div class="lr-txt"><h3>(.*?)</h3>', mono, body)


def analytics_head():
    """Consent Mode defaults (everything denied until the visitor accepts), then Cookiebot (when its ID is set), then Tag Manager."""
    if not ANALYTICS_ON or PREVIEW_MODE[0]: return ''
    consent = ("<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}"
               "gtag('consent','default',{ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',analytics_storage:'denied',"
               "functionality_storage:'granted',security_storage:'granted',wait_for_update:500});gtag('set','ads_data_redaction',true);</script>\n")
    cmp = (f'<script id="Cookiebot" src="https://consent.cookiebot.com/uc.js" data-cbid="{COOKIEBOT_ID}" type="text/javascript"></script>\n' if COOKIEBOT_ID else '')
    gtm = ("<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],"
           "j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);"
           f"}})(window,document,'script','dataLayer','{GTM_ID}');</script>\n")
    return consent + cmp + gtm

def analytics_body():
    if not ANALYTICS_ON or PREVIEW_MODE[0]: return ''
    return f'<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={GTM_ID}" height="0" width="0" style="display:none;visibility:hidden" title="Google Tag Manager"></iframe></noscript>\n'


# ---------------- SEO helpers ----------------
def plain_text(md_text):
    """Readable body text for descriptions: skips images, captions, headings and other short lines that aren't sentences."""
    keep = []
    for ln in (md_text or '').splitlines():
        ln = ln.strip()
        if not ln or ln.startswith(('#', '!', '>', '|', '<')): continue
        if re.fullmatch(r'[*_].*[*_]', ln): continue                                   # an all-italic line: usually a caption
        t = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', ln); t = re.sub(r'[*_`]+', '', t).strip()
        if len(t) < 60 and not t.endswith(('.', '!', '?')): continue                   # a caption or heading, not a sentence
        keep.append(t)
    return ' '.join(' '.join(keep).split())

def fit_desc(primary, more=''):
    """Search descriptions of roughly 110-155 characters: keep good ones, top up short ones with the page's own opening lines."""
    d = ' '.join((primary or '').split())
    if len(d) > 160: return d[:152].rsplit(' ', 1)[0].rstrip(',;:') + '\u2026'
    if len(d) >= 70: return d
    if d and d[-1] not in '.!?\u2026': d += '.'
    for sent in re.split(r'(?<=[.!?])\s+', plain_text(more)):
        if not sent or sent.lower().startswith(d.lower()[:30]): continue
        cand = (d + ' ' + sent).strip()
        if len(cand) > 155:
            if len(d) < 70: d = cand[:152].rsplit(' ', 1)[0].rstrip(',;:') + '\u2026'
            break
        d = cand
        if len(d) >= 110: break
    return d

def share_jpg(src_rel):
    """A 1200x630 JPEG copy of a page's image for LinkedIn and other link previews (they don't all accept WebP)."""
    if not src_rel: return None
    src = os.path.join(OUT, 'assets', src_rel)
    if not os.path.exists(src): return None
    rel = 'share/' + os.path.splitext(os.path.basename(src_rel))[0] + '.jpg'; out = os.path.join(OUT, 'assets', rel)
    if not os.path.exists(out) or os.path.getmtime(out) < os.path.getmtime(src):
        try:
            from PIL import Image
            im = Image.open(src).convert('RGB'); W, H = 1200, 630; r = max(W / im.width, H / im.height)
            im = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
            x, y = (im.width - W) // 2, (im.height - H) // 2
            os.makedirs(os.path.dirname(out), exist_ok=True); im.crop((x, y, x + W, y + H)).save(out, quality=84, optimize=True, progressive=True)
        except Exception:
            return None
    return rel

def short_title(t, limit=60):
    """The browser and search title: the full headline when it fits, else its natural short form. The page keeps the full headline."""
    if len(t) <= limit: return t
    for sep in (': ', ' | ', ' \u2013 ', ' - '):
        head = t.split(sep)[0]
        if 20 <= len(head) <= limit: return head
    m = re.match(r'^(.{15,%d}?(?<!\.)[.?!])\s' % limit, t)            # a first sentence (an ellipsis doesn’t count)
    if m: return m.group(1)
    return t[:limit - 1].rsplit(' ', 1)[0].rstrip(',;:\u2013-') + '\u2026'

def localise_inline(body, A):
    """Swap hotlinked in-article images for the site's own copies (from fetch_thinking_images.py), with their size."""
    inline = IMGMAP.get('_inline', {})
    if not inline: return body
    def sub(m):
        tag = m.group(0); src = html.unescape(m.group(1)); e = inline.get(src)
        if not e or not os.path.exists(os.path.join(THINK_IMG_SRC, 'inline', os.path.basename(e['file']))): return tag
        tag = tag.replace(m.group(1), A(e['file']), 1)
        if ' width=' not in tag: tag = tag.replace('<img', f'<img width="{e["w"]}" height="{e["h"]}"', 1)
        return tag
    return re.sub(r'<img[^>]*\bsrc="([^"]+)"[^>]*>', sub, body)


# ---------------- headlines arrive already split into words (no layout shift when the reveal starts) ----------------
from html.parser import HTMLParser as _HP
_HEAD_RULES = [('h1', {'page-hero', 'proj-hero', 'svc-top', 'contact-page', 'nf'}), ('h2', {'contact'}), ('h2', {'lw-head'}), ('h2', {'over'})]
def _wants_split(tag, cls, ancestors):
    if tag not in ('h1', 'h2'): return False
    if 'sec-title' in cls or 'h2' in cls: return True
    anc = set().union(*ancestors) if ancestors else set()
    return any(tag == t and (need & anc) for t, need in _HEAD_RULES)
class _Finder(_HP):
    def __init__(self, src):
        super().__init__(convert_charrefs=False); self.src = src; self.stack = []; self.found = []; self.open = []
        self.line_off = [0]
        for ln in src.split('\n'): self.line_off.append(self.line_off[-1] + len(ln) + 1)
    def off(self): l, c = self.getpos(); return self.line_off[l - 1] + c
    def handle_starttag(self, tag, attrs):
        if tag in ('br', 'img', 'source', 'meta', 'link', 'input', 'hr', 'wbr'): return
        cls = set((dict(attrs).get('class') or '').split()); start = self.off()
        if _wants_split(tag, cls, [c for _, c in self.stack]) and not self.open:
            self.open.append((tag, start, len(self.stack)))
        self.stack.append((tag, cls))
    def handle_endtag(self, tag):
        while self.stack:
            t, _ = self.stack.pop()
            if self.open and len(self.stack) == self.open[-1][2] and t == self.open[-1][0]:
                ot, st, _ = self.open.pop(); self.found.append((st, self.off() + len(f'</{tag}>')))
            if t == tag: break
def _split_inner(inner):
    out = []; pill = 0; depth = 0
    for tok in re.split(r'(<[^>]+>)', inner):
        if not tok: continue
        if tok.startswith('<'):
            if re.match(r'<span\b[^>]*\bclass="[^"]*\b(?:pill|sr-only|wi-sub)\b', tok): pill = 1; depth = 0
            elif pill and tok.startswith('<span'): depth += 1
            elif pill and tok.startswith('</span'):
                if depth == 0: pill = 0; out.append(tok); continue
                depth -= 1
            out.append(tok); continue
        if pill: out.append(tok); continue
        for part in re.split(r'(\s+)', tok):
            if not part: continue
            out.append(part if part.isspace() else f'<span class="w"><span class="wi">{part}</span></span>')
    return ''.join(out)
def presplit_headings(body):
    if 'class="wi"' in body and False: return body
    f = _Finder(body)
    try: f.feed(body); f.close()
    except Exception: return body
    for st, en in sorted(f.found, reverse=True):
        seg = body[st:en]; m = re.match(r'(<(h[12])\b[^>]*>)(.*)(</h[12]>)$', seg, re.S)
        if not m or 'class="w"' in m.group(3): continue
        open_tag, inner, close = m.group(1), m.group(3), m.group(4)
        label = ' '.join(html.unescape(re.sub(r'<[^>]+>', ' ', re.sub(r'<span\b[^>]*\bpill\b.*?</span>', ' ', inner, flags=re.S))).split())
        if not label: continue
        if 'class="' in open_tag: open_tag = re.sub(r'class="', 'class="rw ', open_tag, count=1)
        else: open_tag = open_tag[:-1] + ' class="rw">'
        if 'aria-label=' not in open_tag: open_tag = open_tag[:-1] + f' aria-label="{esc(label)}">'
        body = body[:st] + open_tag + _split_inner(inner) + close + body[en:]
    return body

L2_SERVICES = [('Brand strategy', 'services/brand-strategy/'), ('Brand identity', 'services/brand-identity/'), ('Creative', 'services/creative/'),
               ('Production', 'services/production/'), ('In-house creative', 'services/in-house/')]
CHEVRON = '<svg width="10" height="10" viewBox="0 0 10 10" aria-hidden="true"><path d="M1.5 3.5 5 7l3.5-3.5" fill="none" stroke="currentColor" stroke-width="1.4"/></svg>'

SHARE_TITLES = {'': 'Freedom Works | Global creative agency', 'agency/': 'About Freedom Works | Global creative agency',
                'services/': 'Services | Freedom Works', 'work/': 'Our work | Freedom Works', 'the-guild/': 'The Guild | Freedom Works',
                'culture3/': 'Culture3 | Freedom Works', 'thinking/': 'Thinking | Freedom Works', 'contact/': 'Contact Freedom Works'}

def share_title(path, title):
    """What a shared link says on LinkedIn: the page's full name, plus Freedom Works (articles keep their full headline)."""
    if path in SHARE_TITLES: return SHARE_TITLES[path]
    slug = path.strip('/').split('/')[-1] if path.startswith('thinking/') else None
    post = next((x for x in POSTS if x['slug'] == slug), None) if slug else None
    tag = next((t for t in TOPIC_SLUG if path == 'thinking/' + TOPIC_SLUG[t] + '/'), None)
    if tag: return f'{TAGS[tag]} | Thinking from Freedom Works'
    name = post['title'] if post else title.split(' | ')[0]
    full = f'{name} | Freedom Works'
    return full if len(full) <= 110 else name

OFFICE_ADDRESS = ['Johnson Building', 'Johnson Gardens', '77 Hatton Garden', 'London, EC1N 8JS', 'UK']

LASTMOD = {}
HOME_TILE_COPY = {
    'king-arthur-baking': ('A creative platform that celebrates the essence of the King Arthur brand and drives differentiation in a low interest category.', 'From #2 to #1 flour brand in the US. Doubled sales.'),
    'wizz-air': ('With a distinctly Spanish flavour, WIZZ\u2019s first fully AI campaign was built on a real human insight and human crafted script.', '+11.4% demand, year on year.'),
    'ms-food': ('Our script provided the creative fuel that allowed M&S\u2019s inhouse team to reunite French & Saunders to bring back the joy of Christmas.', '+10.2% sales.'),
    'loveholidays': ('From performance to brand, without losing demand.', '+72% consideration, \u201342% cost per click, + a million people to their ATOL licence.'),
    'rowse-honey': ('Purpose led is ok if it\u2019s real. We moved beyond \u2018share of toast\u2019 and gave shoppers bee welfare as a reason to choose Rowse.', '+24% new customers.'),
    'brompton': ('For 50 years it\u2019s been that funny little folding bike. But actually the real life affirming stuff happens when you unfold it. Welcome to the fold.', '50th anniversary film.'),
}
# The homepage tile copy is the definitive tile copy: the Work page and service pages use it too
for _p in PROJECTS:
    if _p['slug'] in HOME_TILE_COPY:
        _p['short'], _p['res'] = HOME_TILE_COPY[_p['slug']]

def tile(p, L, A, hl='h3', home=False):
    stat = p['stat'] or 'Play'
    if p['img']:
        small = os.path.join(OUT, 'assets', 'media', p['img'] + '-800.webp')
        if os.path.exists(small) and not PREVIEW_MODE[0] and _IMG_W.get(p['img']):
            ss = f' srcset="{A("media/"+p["img"]+"-800.webp")} 800w, {A("media/"+p["img"]+".webp")} {_IMG_W[p["img"]]}w" sizes="(max-width: 900px) 92vw, 46vw"'
        else: ss = ''
        media = f'<img src="{A("media/"+p["img"]+".webp")}"{ss} alt="{esc(p["client"])}, {esc(p["camp"])}" loading="lazy">'
    else:
        big = p['stat'] or p['client']
        media = f'<div class="typo" aria-hidden="true"><span class="tn">{num_html(big)}</span><span class="tc">{esc(p["client"])}</span></div>'
    short = (HOME_TILE_COPY.get(p['slug'], (None, None))[0] if home else None) or p['short']
    res = (HOME_TILE_COPY.get(p['slug'], (None, None))[1] if home else None) or p['res']
    brief = f'<p>{esc(short)}</p>' if short else ''
    loop = f' data-loop="{A("film/loop-"+p["loop"]+".mp4")}"' if p.get('loop') else ''
    inner = f'<div class="media">{media}</div><{hl}>{esc(p["client"])}: {esc(p["camp"])}</{hl}>{brief}<p class="res">{esc(res)}</p>'
    if CASE_PAGES:
        return f'<a class="tile" href="{L("work/"+p["slug"]+"/")}" data-stat="{esc(stat)}"{vim_attrs(p)}{loop}>{inner}</a>'
    if p.get('vimeo'):
        return f'<a class="tile film-tile" href="{vimeo_url(p)}" data-title="{esc(p["client"])}: {esc(p["camp"])}" data-stat="Play"{vim_attrs(p)}{loop}>{inner}</a>'
    return f'<div class="tile still-tile" data-stat="{esc(stat)}"{loop}>{inner}</div>'

def first_img(p):
    m = re.search(r'!\[[^\]]*\]\((https://[^)\s]+)\)', p['body_md'])
    return m.group(1) if m else ''

PH = ['still-lunch', 'still-calibre', 'still-culture', 'still-craft', 'still-pie', 'still-wreath', 'still-market', 'still-mountain', 'still-veil', 'still-honey', 'poster-kitkat', 'poster-tui', 'poster-sma', 'poster-wizz-air', 'poster-brompton', 'poster-loveholidays', 'poster-ms-food', 'poster-rowse', 'poster-king-arthur']
IMG_MANIFEST = SP('thinking-images.json')
IMGMAP = json.load(open(IMG_MANIFEST, encoding='utf-8')) if os.path.exists(IMG_MANIFEST) else {}
TAG_VARIANT = {t: i % 3 for i, t in enumerate(TAGS)}
THINK_IMG_SRC = SP('thinking-img')     # committed source images (from fetch_thinking_images.py)
def sync_thinking_images():
    """Copy the committed article images into the site so builds never lose them."""
    if not os.path.isdir(THINK_IMG_SRC): return
    dst = os.path.join(OUT, 'assets', 'thinking'); os.makedirs(dst, exist_ok=True)
    for name in os.listdir(THINK_IMG_SRC):
        if name.endswith('.webp'): shutil.copy2(os.path.join(THINK_IMG_SRC, name), os.path.join(dst, name))
    isrc = os.path.join(THINK_IMG_SRC, 'inline')
    if os.path.isdir(isrc):
        os.makedirs(os.path.join(dst, 'inline'), exist_ok=True)
        for name in os.listdir(isrc):
            if name.endswith('.webp'): shutil.copy2(os.path.join(isrc, name), os.path.join(dst, 'inline', name))
    missing = [k for k, e in IMGMAP.items() if e.get('file') and not os.path.exists(os.path.join(THINK_IMG_SRC, os.path.basename(e['file'])))]
    if missing: print(f'Note: {len(missing)} Thinking images are listed but missing; run python3 fetch_thinking_images.py')
def local_img(slug):
    e = IMGMAP.get(slug)
    if e and e.get('file') and os.path.exists(os.path.join(THINK_IMG_SRC, os.path.basename(e['file']))): return e['file']
    return None
def post_cards(posts, L, A=None, with_data=False):
    out = []
    for i, p in enumerate(posts):
        tag = TAGS.get(p['tag'], 'Thinking')
        da = f' data-tag="{p["tag"]}"' if with_data else ''
        typo = f'<span class="tc-in"><span class="mk" aria-hidden="true"></span><span class="tt">{esc(tag)}</span></span>'
        # stand-in photo: fixed per article (by its place in the archive), so neighbours never repeat
        k = (POSTS.index(p) if p in POSTS else i) % len(PH)
        loc = local_img(p['slug'])
        remote = '' if PREVIEW_MODE[0] else first_img(p)
        if loc and A:
            img = f'<span class="cimg"><img src="{A(loc)}" alt="" loading="lazy"></span>'
        elif remote:
            img = f'<span class="cimg ph-{k}"><img src="{esc(remote)}" alt="" loading="lazy" onerror="this.remove()"></span>'
        else:
            img = f'<span class="cimg ph-{k}"></span>'
        out.append(f'<li{da}><a href="{L("thinking/"+p["slug"]+"/")}">{img}<span class="k">{esc(tag)}</span><span class="t">{esc(p["title"])}</span><span class="m">{esc(p["author"])}, {month(p["date"])}</span></a></li>')
    return '<ul class="cards">\n' + '\n'.join(out) + '\n</ul>'

def posts_list(posts, L, with_data=False):
    out = []
    for p in posts:
        fi = first_img(p) if not PREVIEW_MODE[0] else ''
        di = f' data-img="{esc(fi)}"' if fi else ''
        tag = TAGS.get(p['tag'], 'Thinking')
        da = f' data-tag="{p["tag"]}"' if with_data else ''
        out.append(f'<li{da}{di}><a href="{L("thinking/"+p["slug"]+"/")}"><span class="k">{esc(tag)}</span><span class="t">{esc(p["title"])}</span><span class="m">{esc(p["author"])}, {month(p["date"])}</span></a></li>')
    return '<ul class="posts">\n' + '\n'.join(out) + '\n</ul>'

DNA = [
    ('Calibre', 'Make it exceptional.', 'Freedom from tired thinking.', 'p-paper', 'still-calibre', 'While output is now infinite, great ideas are not.',
     'When anyone can generate, the edge is knowing good from great. The Guild is the creative and strategic A-list, handpicked for your brief.',
     "When anyone can generate, the edge is knowing good from great. The Guild is the global creative and strategic A-list. 600+ of the best independent minds across 37 countries and cultures, with 2,315 Lions, Pencils, and Effies between them. Taste and judgement. Insight and evidence. Handpicked for your brief, on your work from day one.",
     'Calibre gets you cut through.'),
    ('Culture', 'Make it resonate.', 'Freedom from cultural isolation.', 'p-red', 'still-culture', 'In the brave new world of AI, human connections are crucial.',
     'AI can talk about culture. It can never be in it. Culture3 gives brands access to the real conversations, communities and moments shaping culture.',
     "AI can talk about culture. It can never be in it. Culture3 puts brands in the rooms that matter: offstage dinners with cultural leaders, onstage with TED, amplified beyond it through organic and paid media. Physical. Nuanced. Human.",
     'Culture gets you noticed.'),
    ('Craft', 'Make it beautiful.', 'Freedom from slop.', 'p-black', 'still-craft', 'Experience, taste, and judgement just got even more differentiating.',
     "AI speeds up the making. People make it great, and decide what ships, from first brief to final cut.",
     "Agentic production removes the old constraints of time, cost, and scale. It doesn’t remove the need for someone to say “not good enough”. Our creative crew have made this call at the very top of the industry, and they stay with the work from first brief to final cut. Even when machines do the making, humans aren\u2019t just in the loop, they\u2019re in the lead.",
     'Craft gets you remembered.'),
]

def dna_panels(A, full=False):
    out = []
    for word, make, free, cls, img, belief, short, long_, outc in DNA:
        out.append(f'''<article class="panel {cls}">
  <div><h3 class="word">{word}</h3><p class="make">{make}</p>{f'<p class="belief">We believe in {word}. {belief}</p>' if full else ''}</div>
  <div class="row"><div class="media"><img src="{A("media/"+img+".webp")}" alt="" loading="lazy"></div>
  <div class="txt"><p class="free">{free}</p><p class="body">{esc(long_ if full else short)}</p><p class="out"><span class="mk" aria-hidden="true"></span>{outc}</p></div></div>
</article>''')
    return '<div class="panels">' + '\n'.join(out) + '</div>'

def ticker(A):
    lines = ["Nearly ten years ago we built the agency model that everyone talks about.", "But the world has moved on. And so have we.",
             "Today we are entering the agentic age.", "A creative renaissance is here, where machines make anything possible.",
             "And that makes humanity more important than ever.", "Freedom from tired thinking and production constraints.",
             "Freedom from slop and a sea of sameness.", "Freedom from office bound monotony.", "Freedom from convention.", "Freedom. Works."]
    one = ''.join(f'<span class="it"><span class="mk" aria-hidden="true"></span>{esc(t)}</span>' for t in lines)
    dup = one.replace('<span class="it">', '<span class="it" aria-hidden="true">')
    return f'<section class="ticker words" aria-label="Why Freedom Works"><div class="track">{one}{dup}</div></section>'

def logo_marquee(A):
    """Client logos in mono white, scrolling under the hero. Heights are optically balanced (equal visual area)."""
    items = ''.join(f'<li><img src="{A("logos/wall/"+x["slug"]+"-white.png")}" alt="{esc(x["name"])}" style="height:{min(58, 2150 / x["w"]):.0f}px" decoding="async"></li>' for x in LOGOWALL)
    dup = items.replace('<li><img ', '<li aria-hidden="true"><img ').replace(' alt="', ' data-alt="')
    dup = dup.replace(' data-alt="', ' alt="" data-alt="')
    return f'<section class="logo-run" aria-label="Brands we\u2019ve made work for"><ul class="track">{items}{dup}</ul></section>'

def img_wh(rel):
    try:
        from PIL import Image
        w, h = Image.open(os.path.join(OUT, 'assets', rel)).size; return f' width="{w}" height="{h}"'
    except Exception: return ''

def logos_band(A, dark=False):
    strip = 'clients-white' if dark else 'clients-dark'
    cls = ' dark' if dark else ''
    mk = '' if dark else ' ink'
    return f'''<section class="logos-band{cls}" aria-label="Clients">
  <p class="lbl wrap"><span class="mk{mk}" aria-hidden="true"></span>Brands we've made work for</p>
  <div class="marquee" aria-label="Clients include Heineken, Wizz Air, Diageo, Nestlé, TUI, P&amp;G, Coca-Cola, GSK, M&amp;S Food, Brompton, and loveholidays">
    <img src="{A("logos/"+strip+".png")}" alt=""{img_wh("logos/"+strip+".png")}><img src="{A("logos/"+strip+".png")}" alt="" aria-hidden="true"{img_wh("logos/"+strip+".png")}>
  </div>
</section>'''

def strip3(A, a, b, c, pos=('', '', '')):
    """Three stills: tall, wide, tall. pos optionally sets each crop's focus (CSS object-position, e.g. '40% 50%')."""
    st = lambda k: f' style="object-position:{pos[k]}"' if pos[k] else ''
    return (f'<div class="strip3" aria-hidden="true"><div class="a px"><img src="{A("media/"+a+".webp")}" alt="" loading="lazy"{st(0)}></div>'
            f'<div class="b px"><img src="{A("media/"+b+".webp")}" alt="" loading="lazy"{st(1)}></div>'
            f'<div class="c px"><img src="{A("media/"+c+".webp")}" alt="" loading="lazy"{st(2)}></div></div>')

HS_PORTAL, HS_FORM, HS_SHARE = '25281165', '0aad04dc-5ab6-4146-b353-f73841abc855', 'https://share-eu1.hsforms.com/1Cq0E3Fq2QUazU_c4QavIVQf1v2l'

IMPACT = [
    ('+100%', 'Sales uplift', 'King Arthur Baking', 'Keep Rising took King Arthur to the #1 flour brand in the US and added 3.4m new households.', 'king-arthur-baking'),
    ('+10.2%', 'Sales', 'M&S Food', "The Christmas idea that reunited Dawn French and Jennifer Saunders, made with M&S Food\u2019s in-house team.", 'ms-food'),
    ('+11.4%', 'Demand, year on year', 'Wizz Air', "The airline\u2019s first fully AI powered campaign: 17 broadcast ready assets in three weeks.", 'wizz-air'),
    ('+72%', 'Consideration', 'loveholidays', 'From performance to brand: +15pts awareness and demand that needed 1m people added to their ATOL licence.', 'loveholidays'),
    ('$621m', 'Acquisition by Zensho', 'Snowfox Group', 'Our platform unified Snowfox Group\u2019s four sushi brands and contributed to its $621m acquisition by Zensho.', 'snowfox-group'),
]

C3_SVG = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'c3-logo.svg')).read() if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'c3-logo.svg')) else None

def c3_logo(cls=''):
    svg = C3_SVG.replace('<svg ', '<svg role="img" aria-label="Culture3" focusable="false" ', 1)
    return f'<span class="c3-logo-svg {cls}">{svg}</span>'

def logo_slot(name, cls=''):
    """Real logo where we have the file; text stand-in otherwise."""
    if name == 'Culture3' and C3_SVG:
        return c3_logo(cls)
    return f'<span class="logo-slot {cls}" data-logo="{esc(name)}">{esc(name)}</span>'

def impact_html(L, A, logos=True, heading='<em>work</em> with impact', intro=True):
    by = {p['slug']: p for p in PROJECTS}
    def card(n, t, c, d, slug):
        body = f'<span class="n" data-count>{num_html(n)}</span><span class="t">{esc(t)}<em>{esc(c)}</em></span><span class="d">{esc(d)}</span>'
        pj = by.get(slug, {})
        if CASE_PAGES: return f'<a class="im-card" href="{L("work/"+slug+"/")}">{body}<span class="go">See the case study</span></a>'
        if pj.get('vimeo'): return f'<a class="im-card film-tile" href="{vimeo_url(pj)}" data-title="{esc(pj["client"])}: {esc(pj["camp"])}"{vim_attrs(pj)}>{body}<span class="go">Watch the film</span></a>'
        return f'<div class="im-card">{body}</div>'
    cards = ''.join(card(*x) for x in IMPACT)
    logos_html = f'''  <div class="im-logos">
    <p class="lbl wrap"><span class="mk" aria-hidden="true"></span>Brands we\u2019ve made work for</p>
    <div class="marquee" aria-hidden="true"><img src="{A("logos/clients-white.png")}" alt=""><img src="{A("logos/clients-white.png")}" alt=""></div>
  </div>''' if logos else ''
    return f'''<section class="impact dark" aria-labelledby="im">
  <div class="wrap">
    <div class="im-head">
      <h2 class="sec-title" id="im">{heading}</h2>
      {'<p>Creative work should drive fame in the boardroom as well: sales, market share, demand, and value.</p>' if intro else ''}
    </div>
    <div class="im-grid">
      <div class="im-card big"><span class="n" data-count>2,315</span><span class="t">Lions, Pencils, and Effies<em>Won by the talent in The Guild</em></span><span class="awards"><img src="{A("brand/award-cannes-lions.png")}" alt="Cannes Lions" width="369" height="160"><img class="dad" src="{A("brand/award-dandad.png")}" alt="D&amp;AD" width="147" height="160"><img src="{A("brand/award-effie.png")}" alt="Effie Awards" width="360" height="160"></span></div>
      {cards}
    </div>
  </div>
{logos_html}
</section>'''

CLIENTS = ['Heineken', 'Wizz Air', 'Diageo', 'Nestlé', 'TUI', 'P&G', 'Burger King', 'Coca-Cola', 'GSK', 'Campari Group', 'King Arthur Baking', 'Pernod Ricard', 'M&S Food', 'Brompton', 'Octopus', 'Virgin Red', 'loveholidays', 'Bayer', 'reMarkable', 'Haleon', 'Brown-Forman', 'Logitech', 'EDF']
def clients_wall():
    items = ''.join(f'<li>{esc(c)}</li>' for c in CLIENTS)
    return f'''<section class="clients-wall wrap light" aria-labelledby="cw">
  <p class="sec-lbl" id="cw"><span class="mk" aria-hidden="true"></span>Brands we\u2019ve made work for</p>
  <ul class="cw-list">{items}</ul>
</section>'''

LOGOWALL = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logowall.json'), encoding='utf-8'))
def logo_wall(A):
    cells = ''.join(f'''<li><span class="lw-cell" style="--w:{x["w"]}%"><img class="ink" src="{A("logos/wall/"+x["slug"]+"-ink.png")}" alt="{esc(x["name"])}" loading="lazy"><img class="col" src="{A("logos/wall/"+x["slug"]+"-col.png")}" alt="" aria-hidden="true" loading="lazy"></span></li>''' for x in LOGOWALL)
    return f'''<section class="logo-wall light" aria-labelledby="lw">
  <div class="wrap">
    <div class="lw-head"><h2 class="sec-title" id="lw">Brands we\u2019ve <span class="thin">made work for</span></h2></div>
    <ul class="lw-grid">{cells}</ul>
  </div>
</section>'''

def page_home(L, A):
    m = HOME_MAIN.replace('src="assets/', 'src="' + A('')).replace('poster="assets/', 'poster="' + A('')).replace('srcset="assets/', 'srcset="' + A('')).replace(', assets/', ', ' + A(''))
    hero = re.search(r'<section class="hero".*?</section>', m, re.S).group(0)
    doors = re.search(r'<section class="doors wrap[^"]*".*?</section>', m, re.S).group(0)
    doors = re.sub(r'href="/(work|agency|the-guild|services|culture3|thinking|contact)(/[^"]*)?"', lambda mo: f'href="{L(mo.group(1) + "/")}"', doors)
    for a, b in {'craft.webp': 'still-lunch.webp', 'calibre.webp': 'still-calibre.webp', 'brompton.webp': 'still-craft.webp', 'culture.webp': 'still-culture.webp'}.items():
        doors = doors.replace('media/' + a, 'media/' + b)
    doors = doors.replace("Platforms, campaigns, content, and teams on demand. Fixed scope, fixed cost, fixed time.", "Brand strategy, identity, creative, production, and in-house creative.")
    doors = doors.replace('<span class="name">Agency</span>', '<span class="name">About</span>')

    doors = doors.replace('<section class="doors wrap on-white" aria-label="Explore Freedom Works">', '<section class="doors wrap on-white" aria-labelledby="ex"><div class="sec-head"><h2 class="sec-title" id="ex">Explore <span class="thin">Freedom Works</span></h2></div>')
    pill = f'<span class="pill" aria-hidden="true"><video autoplay muted loop playsinline poster="{A("media/hero-poster.jpg")}"><source src="{A("film/pill-home.mp4")}" type="video/mp4"></video></span>'
    statement = f'''<section class="statement wrap indigo" aria-labelledby="st">
  <p class="sec-lbl">Why Freedom Works</p>
  <h2 class="fw-head fw-lockup" id="st"><img src="{A("brand/lockup-freedom-makes-better-work.png")}" alt="Freedom makes better work" width="3482" height="552"></h2>
  <div class="intro-grid">
    <p class="intro-lead">And better work shows up where it counts.<br>On screen, in culture, and on your P&amp;L.</p>
    <p class="intro-body">Creativity doesn\u2019t thrive in rigid systems or office bound models. It thrives when people are trusted and supported to do their best thinking. This freedom attracts better talent. Better talent produces better ideas. And better ideas grow your brand. Simple.</p>
  </div>
</section>'''
    who_intro = '''<section class="who-intro wrap white" aria-labelledby="whoi">
  <h1 class="sec-title wi-title" id="whoi">Welcome to <span class="thin">Freedom Works.</span> <span class="wi-sub">Global creative agency</span></h1>
  <div class="wi-lead"><p>In a world drowning in content, we make work that matters. The world\u2019s best creative minds anchor your brand at the heart of culture, and craft the work for impact.</p><p class="wi-tag">Calibre, Culture &amp; Craft.</p></div>
</section>'''
    pillars = f'''<section class="pillars-e wrap light" aria-labelledby="who">
  <div class="sec-head"><h2 class="sec-title" id="who">Who <span class="thin">we are</span></h2></div>
  <div class="pe-grid">
    <a class="pe" href="{L("the-guild/")}"><span class="pe-n">01</span><h3 class="pe-t">The Guild</h3><p>We have the best creative department in the world: The Guild. More than six hundred A-list creatives, strategists, and producers, in 37 countries and cultures, with over 2,300 Lions &amp; Pencils between them, handpicked for each brief.</p><span class="pe-go">Meet The Guild</span></a>
    <a class="pe" href="{L("culture3/")}"><span class="pe-n">02</span><h3 class="pe-t">{c3_logo()}</h3><p>AI can talk about culture. It can never be in it. Culture3 puts brands in the rooms that matter: offstage dinners with cultural leaders, onstage with TED, amplified beyond it through organic and paid media. Physical. Nuanced. Human.</p><span class="pe-go">Explore Culture3</span></a>
    <a class="pe" href="{L("agency/")}#leadership"><span class="pe-n">03</span><h3 class="pe-t">Leadership</h3><p>We\u2019re led by a founder and a leadership team who have excelled with ideas, organisations, and talent at the very top of the industry. Their vision and judgement runs through every piece of work we make.</p><span class="pe-go">Meet the leadership</span></a>
  </div>
</section>'''
    reel = f'<section class="reel" aria-hidden="true"><video class="lazyvid" muted loop playsinline preload="none" poster="{A("media/poster-brompton.webp")}" data-src="{A("film/sizzle-home.mp4")}"></video></section>'
    work = f'''<section class="work wrap light" id="work" aria-labelledby="wk">
  <div class="sec-head"><h2 class="sec-title" id="wk"><em>work</em> that matters</h2><a class="sec-link" href="{L("work/")}">All work</a></div>
  <div class="grid">
    {chr(10).join(tile(p, L, A, home=True) for p in PROJECTS if p['home'])}
  </div>
</section>'''
    impact = impact_html(L, A, logos=False)
    hint = f'''<section class="dna-hint dark" aria-labelledby="dh">
  <div class="wrap">
    <div class="dh-top">
      <p class="dh-lbl"><span class="mk" aria-hidden="true"></span>Our DNA</p>
      <h2 id="dh" class="dh-lead">In a world where machines can do almost anything, the things they can\u2019t do just became a whole lot more important.</h2>
    </div>
    <ul class="dh-rows">
      <li><a href="{L("agency/")}#dna"><span class="w">Calibre</span><span class="s"><b>Make it exceptional.</b> Access the best creative department in the world.</span></a></li>
      <li><a href="{L("agency/")}#dna"><span class="w">Culture</span><span class="s"><b>Make it resonate.</b> Real human moments are where brands live longest.</span></a></li>
      <li><a href="{L("agency/")}#dna"><span class="w">Craft</span><span class="s"><b>Make it beautiful.</b> Obsessive attention to detail is a superpower.</span></a></li>
    </ul>
    <div class="dh-end"><p>This is our DNA. Humanity at the core.</p><a class="sec-link" href="{L("agency/")}#dna">Explore our DNA</a></div>
  </div>
</section>'''
    guild = mosaic(A, '<span>600+ minds.</span> <span>37 countries and cultures.</span> <span>One brief at a time.</span>', 'The Guild is the creative and strategic A-list. For every project, we handpick the people who fit your brief, your brand, and your culture.', L('the-guild/'), 'Meet The Guild')
    marquee = '<section class="big-marquee light" aria-hidden="true"><div class="track">' + ''.join('<span class="h">Freedom</span><span class="t">works</span><span class="mkb"></span>' for _ in range(5)) + '</div></section>'
    voices = voices_html(VOICES, theme='on-light')
    thinking = f'''<section class="thinking wrap light" aria-labelledby="th">
  <div class="sec-head"><h2 class="sec-title" id="th"><em>Thinking</em></h2><a class="sec-link" href="{L("thinking/")}">All articles</a></div>
  {post_cards(POSTS[:3], L, A)}
</section>'''
    hero = hero.replace('<!--LOGO_RUN-->', logo_marquee(A), 1)
    stills = f'''<section class="still-strip" aria-hidden="true"><img src="{A("media/poster-culture3.webp")}" alt="" loading="lazy"><img src="{A("media/still-market.webp")}" alt="" loading="lazy"><img src="{A("media/poster-kitkat.webp")}" alt="" loading="lazy"></section>'''
    return '\n'.join([hero, who_intro, work, reel, logo_wall(A), pillars, impact, voices, hint, guild, statement, ticker(A), stills, doors, thinking, cta(L)])

def page_agency(L, A):
    return f'''<section class="page-hero wrap">
  <h1>Freedom makes <span class="thin">better</span> work.</h1>
  <div class="intro"><div class="stack">
    <p>Freedom Works is a global creative agency offering brand strategy, brand identity, creative, production, and in-house creative. We bring together The Guild, a network of more than 600 award winning independent creatives, strategists, and producers across 37 countries and cultures, and Culture3, our cultural partnerships business, to build a handpicked team for every brief.</p>
    <p>We believe freedom makes better work. Not as fancy words. In practice. In real life. Creativity doesn\u2019t thrive in rigid systems or office bound models. It thrives when people are trusted and supported to do their best thinking.</p>
  </div></div>
</section>
<div class="sizzle wrap"><video class="lazyvid" muted loop playsinline preload="none" poster="{A("media/still-lunch.webp")}" data-src="{A("film/sizzle-agency.mp4")}" aria-hidden="true"></video></div>
<section class="band wrap">
  <div class="split">
    <div class="l"><h2 class="h2">Built for the <span class="thin">next ten years</span></h2></div>
    <div class="r prose">
      <p class="lead-light">Nearly ten years ago we built the agency model that everyone talks about. But the world has moved on. And so have we.</p>
      <p>As we build out an agency fit for the next ten years, AI is embedded for process and production. But for ideas, we have designed a business with humanity at its core.</p>
      <p>With The Guild, we have the best creative department in the world: more than six hundred A-list creatives, strategists, and producers, in 37 countries and cultures, with over 2,300 Lions and Pencils between them, handpicked for each brief.</p>
      <p>AI can talk about culture. It can never be in it. Culture3 puts brands in the rooms that matter: offstage dinners with cultural leaders, onstage with TED, amplified beyond it through organic and paid media. Physical. Nuanced. Human.</p>
      <p>We\u2019re led by a founder and a leadership team who have excelled with ideas, organisations, and talent at the very top of the industry. Our vision and judgement runs through every piece of work we make.</p>
    </div>
  </div>
</section>
{strip3(A, "still-pie", "poster-loveholidays", "still-honey")}
<section class="band wrap" id="dna" aria-labelledby="dna-h">
  <div class="split split-head">
    <div class="l"><h2 class="h2" id="dna-h">Our DNA</h2></div>
    <div class="r"><p class="lead-light">In a world where machines can do almost anything, the things they can\u2019t do just became a whole lot more important. Where the work belongs. Who decides what\u2019s worth making. How well it\u2019s made. This is our DNA. Humanity at the core, with an agentic engine behind it.</p></div>
  </div>
</section>
{dna_panels(A, full=True)}
<section class="band wrap" id="leadership" aria-labelledby="ld">
  <div class="split split-head">
    <div class="l"><h2 class="h2" id="ld">Taste. Judgement. <span class="thin">Experience.</span></h2><p class="ld-sub">The people behind Freedom Works.</p></div>
    <div class="r"><p class="lead-light">Anyone can generate a hundred ideas now. Knowing a great idea from an average one is where the value lies. This call gets made by people who\u2019ve made it at the very top of the industry, on the biggest brands in the world. And they don\u2019t hand it off after the presentation. They stay on it until it deploys.</p></div>
  </div>
  <div class="leaders">
    <article class="lead-row" id="jon-williams"><div class="ph ph-photo"><img src="{A("media/team/jon-williams-600.webp")}" srcset="{A("media/team/jon-williams-600.webp")} 600w, {A("media/team/jon-williams-1200.webp")} 1200w" sizes="(max-width: 900px) 50vw, 25vw" alt="Jon Williams, Founder and Chief Creative Officer" width="600" height="750" loading="lazy" decoding="async"></div><div class="lr-txt"><h3>Jon Williams</h3><p class="role">Founder and Chief Creative Officer</p><a class="lr-li" href="https://www.linkedin.com/in/creativegenius/" target="_blank" rel="noopener" aria-label="Jon Williams on LinkedIn"><svg aria-hidden="true" viewBox="0 0 24 24" width="14" height="14"><path fill="currentColor" d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9.5h4V21H3zM9.5 9.5h3.8v1.6h.06c.53-1 1.83-2.06 3.77-2.06 4.03 0 4.77 2.65 4.77 6.1V21h-4v-5.1c0-1.22-.02-2.78-1.7-2.78-1.7 0-1.96 1.33-1.96 2.7V21h-4z"/></svg><span>LinkedIn</span></a><ul class="pstats"><li><b data-count>49</b>Agencies led</li><li><b data-count>105</b>Cannes Lions</li><li><b data-count>109</b>Effies</li><li><b data-count>51</b>D&amp;AD Pencils</li></ul><div class="bio"><p>Jon Williams is Founder and Chief Creative Officer of Freedom Works.</p><p>At Publicis he created HYPE for HP, the platform Cannes used as its benchmark for the Titanium Lion, and \u201cChoices\u201d for the DePaul Trust, the world\u2019s first true interactive TV spot. He went on to make the Carling iPint, the world\u2019s first native branded iPhone app, downloaded six million times.</p><p>As Chief Creative Officer of Grey London, then Grey EMEA across 47 agencies, he built the network\u2019s best performing creative region: 105 Cannes Lions, 109 Effies, and 51 D&amp;AD Pencils, plus a 2,000 strong talent platform.</p><p>In 2017 he founded The Liberty Guild, which now powers Freedom Works.</p><p>As well as having chaired or sat on pretty much every award show there is, Jon sits on the Creative UK council and has judged the Luma AI Dream Brief and the Advertising Turing Test. Fuelling his conviction that as machines make more, human taste and judgement matter more than ever.</p></div></div></article>
    <article class="lead-row" id="aimee-luther"><div class="ph ph-photo"><img src="{A("media/team/aimee-luther-600.webp")}" srcset="{A("media/team/aimee-luther-600.webp")} 600w, {A("media/team/aimee-luther-1200.webp")} 1200w" sizes="(max-width: 900px) 50vw, 25vw" alt="Aim\u00e9e Luther, Managing Director" width="600" height="750" loading="lazy" decoding="async"></div><div class="lr-txt"><h3>Aim\u00e9e Luther</h3><p class="role">Managing Director</p><a class="lr-li" href="https://www.linkedin.com/in/aimeeluther/" target="_blank" rel="noopener" aria-label="Aimée Luther on LinkedIn"><svg aria-hidden="true" viewBox="0 0 24 24" width="14" height="14"><path fill="currentColor" d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9.5h4V21H3zM9.5 9.5h3.8v1.6h.06c.53-1 1.83-2.06 3.77-2.06 4.03 0 4.77 2.65 4.77 6.1V21h-4v-5.1c0-1.22-.02-2.78-1.7-2.78-1.7 0-1.96 1.33-1.96 2.7V21h-4z"/></svg><span>LinkedIn</span></a><div class="bio"><p>Aim\u00e9e is Managing Director of Freedom Works.</p><p>A graduate of Ogilvy &amp; Mather, Aim\u00e9e spent a decade running TUI at BMB, the start-up agency she joined and went on to lead as Managing Director by 2013, producing some of the most decorated work in the industry. After launching Fortnight Collective in Europe, she joined The Liberty Guild and helped take it into the Sunday Times Best Places to Work 2026.</p><p>She is a Founding Trustee of CALM, Chair of Words Matter and a Trustee of the Langa Township Pre-School Trust in Cape Town, and she is Marketer in Residence and Honorary Teaching Fellow at Lancaster University. Her conviction is that the best businesses are the ones that make a difference.</p><p>And while not a natural athlete, she has harrumphed around the London Marathon five times.</p></div></div></article>
    <article class="lead-row" id="lins-karnes"><div class="ph ph-photo"><img src="{A("media/team/lins-karnes-600.webp")}" srcset="{A("media/team/lins-karnes-600.webp")} 600w, {A("media/team/lins-karnes-1200.webp")} 1200w" sizes="(max-width: 900px) 50vw, 25vw" alt="Lins Karnes, Chief Delivery Officer" width="600" height="750" loading="lazy" decoding="async"></div><div class="lr-txt"><h3>Lins Karnes</h3><p class="role">Chief Delivery Officer</p><a class="lr-li" href="https://www.linkedin.com/in/linskarnes/" target="_blank" rel="noopener" aria-label="Lins Karnes on LinkedIn"><svg aria-hidden="true" viewBox="0 0 24 24" width="14" height="14"><path fill="currentColor" d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9.5h4V21H3zM9.5 9.5h3.8v1.6h.06c.53-1 1.83-2.06 3.77-2.06 4.03 0 4.77 2.65 4.77 6.1V21h-4v-5.1c0-1.22-.02-2.78-1.7-2.78-1.7 0-1.96 1.33-1.96 2.7V21h-4z"/></svg><span>LinkedIn</span></a><div class="bio"><p>Lins\u2019 attention to detail keeps everyone in line and makes stuff actually happen. He\u2019s a rare multi-platform, multi-format, digital native production leader with a degree in computer science.</p><p>He\u2019s worked with big tech, CMS, e-commerce, and digital transformation for companies such as HP, Compaq, Ford, Harvard Business School, and non-governmental agencies. He\u2019s headed up digital production at Wunderman, BHH, and Saint@RKCR/Y&amp;R, improving creative output across digital, and integrated, and delivering global, European, and national programmes for clients such as Microsoft and Unilever.</p><p>His last gig before he came to co-found The Liberty Guild was MD of B-Reel, the world\u2019s leading mixed media production company, where he drove technical innovation and creative excellence across TV, film, content, digital, integrated, experiential, and product development.</p></div></div></article>
    <article class="lead-row" id="holly-dillon"><div class="ph ph-photo"><img src="{A("media/team/holly-dillon-600.webp")}" srcset="{A("media/team/holly-dillon-600.webp")} 600w, {A("media/team/holly-dillon-1200.webp")} 1200w" sizes="(max-width: 900px) 50vw, 25vw" alt="Holly Dillon, Chief Operating Officer, Culture3" width="600" height="750" loading="lazy" decoding="async"></div><div class="lr-txt"><h3>Holly Dillon</h3><p class="role">Chief Operating Officer, Culture3</p><a class="lr-li" href="https://www.linkedin.com/in/holly-dillon/" target="_blank" rel="noopener" aria-label="Holly Dillon on LinkedIn"><svg aria-hidden="true" viewBox="0 0 24 24" width="14" height="14"><path fill="currentColor" d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9.5h4V21H3zM9.5 9.5h3.8v1.6h.06c.53-1 1.83-2.06 3.77-2.06 4.03 0 4.77 2.65 4.77 6.1V21h-4v-5.1c0-1.22-.02-2.78-1.7-2.78-1.7 0-1.96 1.33-1.96 2.7V21h-4z"/></svg><span>LinkedIn</span></a><div class="bio"><p>Holly leads the business across commercial strategy, growth, operations, and delivery. She oversees senior client relationships and strategic partnerships, including partnerships with cultural organisations such as TED, connecting brands and businesses with the conversations, communities and moments shaping their industries.</p><p>With over 15 years of experience building businesses and leading international teams, Holly brings executive leadership experience from film and television production and storytelling, which informs her approach to business strategy, creative ambition, and commercial growth. She works closely with C-suite leaders and senior decision makers to identify commercial opportunities, build relationships, and translate ambition into business growth.</p><p>Prior to Culture3, Holly launched and built Variety\u2019s branded content studio, developing partnerships with Netflix and Apple TV, and delivering award winning work around NEON\u2019s Parasite.</p><p>Holly is also the founder of Get Your Skin Out, changing how visible skin conditions are represented across culture.</p></div></div></article>
    <article class="lead-row" id="jamila-saidi"><div class="ph ph-photo"><img src="{A("media/team/jamila-saidi-600.webp")}" srcset="{A("media/team/jamila-saidi-600.webp")} 600w, {A("media/team/jamila-saidi-1200.webp")} 1200w" sizes="(max-width: 900px) 50vw, 25vw" alt="Jamila Saidi, Chief Growth Officer, Culture3" width="600" height="750" loading="lazy" decoding="async"></div><div class="lr-txt"><h3>Jamila Saidi</h3><p class="role">Chief Growth Officer, Culture3</p><a class="lr-li" href="https://www.linkedin.com/in/jamila-saidi/" target="_blank" rel="noopener" aria-label="Jamila Saidi on LinkedIn"><svg aria-hidden="true" viewBox="0 0 24 24" width="14" height="14"><path fill="currentColor" d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9.5h4V21H3zM9.5 9.5h3.8v1.6h.06c.53-1 1.83-2.06 3.77-2.06 4.03 0 4.77 2.65 4.77 6.1V21h-4v-5.1c0-1.22-.02-2.78-1.7-2.78-1.7 0-1.96 1.33-1.96 2.7V21h-4z"/></svg><span>LinkedIn</span></a><div class="bio"><p>Jamila leads on strategic growth, partnership development, and commercial expansion, working with brands, businesses, and entrepreneurs at the intersection of culture, creativity, and commerce. Her background in marketing and international trade and investment promotion informs a commercially grounded approach to building lasting client relationships.</p><p>With over 20 years of experience as a global growth leader and commercial strategist, Jamila specialises in entering new markets, building high value partnerships, and scaling opportunities internationally. She works closely with founders, C-suite leaders, and brand decision makers to unlock growth that is both ambitious and culturally resonant.</p><p>Jamila brings deep expertise in retail, luxury, fashion, beauty, digital, and the creative industries. She is a passionate advocate for digital trade as a growth enabler and champions female founders and SMEs across the creative economy.</p><p>Prior to joining Culture3, Jamila held senior leadership roles at the UK\u2019s Department for Business and Trade, and worked in international marketing roles at Lloyds Bank Private Banking, Merrill Lynch Global Wealth Management and Grant Thornton.</p></div></div></article>
  </div>
</section>
{logo_wall(A)}
<section class="closing-st wrap" aria-label="What we stand for"><p>We make work that matters. Work that\u2019s anchored in culture, crafted for impact, and guided by the best creative minds in the industry.</p></section>
{cta(L)}'''

def mosaic(A, title, para, link_href, link_text):
    imgs = ['still-lunch', 'still-calibre', 'poster-wizz-air', 'still-craft', 'still-culture', 'still-wreath', 'still-mountain', 'still-veil']
    cls = {0: ' class="w2 h2"', 6: ' class="w2"'}
    im = '\n    '.join(f'<img{cls.get(i, "")} src="{A("media/"+k+".webp")}" alt="" loading="lazy">' for i, k in enumerate(imgs))
    return f'''<section class="guild" aria-label="{esc(re.sub("<[^>]+>", "", title))}">
  <div class="mosaic" aria-hidden="true">
    {im}
  </div>
  <div class="over">
    <h2>{title}</h2>
    <p>{para}</p>
    <a class="sec-link" href="{link_href}">{link_text}</a>
  </div>
</section>'''

def guild_voices():
    cpw = ('The quality of the healthy debates we have is a proof of the senior and highly experienced individuals behind the team, allowing us to build on each other\u2019s points of view that yield nothing but better outputs.', 'Estrella Lopez-Brea', 'ex-Global Head of Insights, CPW')
    picks = ['king-arthur-baking', 'loveholidays', 'brompton', 'wizz-air', 'tui']
    by = {p['slug']: p for p in PROJECTS}
    out = [cpw]
    for k in picks:
        q = by[k].get('quote')
        if q: out.append((q[0].strip('\u201c\u201d"'), q[1], q[2]))
    return out

GUILD_VOICES = guild_voices()

def page_guild(L, A):
    return f'''<section class="page-hero wrap">
  <h1>The best creative <span class="thin">department in the world.</span></h1>
  <div class="intro"><div class="stack">
    <p>The Guild is the creative A-list: 600+ of the world\u2019s best independent creatives, strategists, and producers across 37 countries and cultures, with 2,315 awards between them.</p>
    <p>We work with our clients to handpick a bespoke team from this community for every project, whatever or wherever required.</p>
  </div></div>
</section>
<div class="sizzle wrap"><video class="lazyvid" muted loop playsinline preload="none" poster="{A("media/still-calibre.webp")}" data-src="{A("film/sizzle-guild.mp4")}" aria-hidden="true"></video></div>
<section class="band tight dark" aria-label="The Guild in numbers">
  <div class="wrap">
    <div class="figures">
      <div><span class="n">600+</span><span class="l">Creatives, strategists, and producers</span></div>
      <div><span class="n">37</span><span class="l">Countries and cultures</span></div>
      <div><span class="n">2,315</span><span class="l">Lions, Pencils, and Effies collectively</span></div>
      <div><span class="n">33<span class="u">%</span></span><span class="l">Female (14% industry benchmark)</span></div>
    </div>
  </div>
</section>
<section class="band tight">{strip3(A, "still-market", "poster-wizz-air", "still-veil")}</section>
<section class="band wrap" aria-labelledby="gw">
  <div class="split">
    <div class="l"><h2 class="h2" id="gw">How does The Guild <span class="thin">work?</span></h2></div>
    <div class="r prose">
      <p class="lead-light">The best creatives don\u2019t sit in agencies anymore. They work independently, on the projects and terms that bring out their best thinking.</p>
      <p>So we built a distributed creative department around them. No buildings. No fixed teams. Just the right people for the job. Every time.</p>
      <p>For every brief, we handpick a team from our network. We back them with qual, quant, or behavioural research, and run the work through our own tech stack. We use AI when it helps, and not when it doesn\u2019t.</p>
      <p>We can run everything end to end, from brief to production, or plug straight into your in-house team. Same calibre of talent either way.</p>
    </div>
  </div>
</section>
<section class="band wrap flush-top" aria-labelledby="gt">
  <div class="split">
    <div class="l"><h2 class="h2" id="gt">What makes our talent <span class="thin">better?</span></h2></div>
    <div class="r prose">
      <p class="lead-light">They\u2019ve already won big at Cannes, D&amp;AD, and the Effies. Strategically and creatively, this is the global A-list.</p>
      <p>And they\u2019re not passing through. They\u2019re here because this is how they want to work. As client demand grows, they\u2019re being joined by a new generation of social native creators and AI artists.</p>
      <p>Every project starts by finding the right people for the brief. Not whoever\u2019s free. Not whoever\u2019s cheapest.</p>
      <p>Get that right and the ideas get better. And they get there faster.</p>
    </div>
  </div>
</section>
{mosaic(A, '<span>Taste and judgement.</span> <span>Insight and evidence.</span>', 'Handpicked for your brief, on your work from day one. See what a Guild team can do for you.', L('services/'), 'Our services')}
{voices_html(GUILD_VOICES)}
{cta(L)}'''

WHATWEDO = [
    ('Brand strategy', "Building a new brand from scratch? Taking an existing one somewhere new? Or just buffing a dusty one up a bit? We work out where it\u2019s coming from and where it needs to go. And why. From positioning and architecture to the brief that gets the work made.",
     ['Strategic consultancy', 'Brand audits and roadmaps', 'Brand positioning', 'Brand architecture', 'Communications strategy', 'Creative briefing'], 'still-calibre'),
    ('Brand identity', "Once you know what your brand stands for, you have to look and sound like it. We create the name, the identity, the voice, and the visual world that make it unmistakable. And the guidelines that keep it this way.",
     ['Brand development and rebranding', 'Naming', 'Visual identity and brand guidelines', 'Tone of voice'], 'poster-ms-food'),
    ('Creative', "A box fresh global platform. Your next differentiating brand campaign. The socially native work you\u2019re just not getting from your AoR? A difficult brief that needs a fresh perspective? We develop ideas with the breadth to span channels and cultures. We can spin a \u2018creative hot shop\u2019 up literally anywhere.",
     ['Creative platforms', 'Campaign strategy and development', 'Advertising concepts', 'Integrated and multi-channel campaigns', 'Brand and product launches', 'Digital and social creative', 'Content ideas', 'Creator and influencer', 'Global and local campaigns', 'Creative sprints'], 'poster-wizz-air'),
    ('Production', "Give the idea the craft it deserves. We bring campaigns and content to life across channels and markets, through us or alongside your existing production team. Our AI artists and virtual production specialists work alongside traditional crews, so big ideas no longer need big budgets to get made. And with our global content amplification partner, we deliver scaled brilliance: one great idea, built out into every asset, format, and market it needs.",
     ['Campaign production', 'Film and video', 'AI production', 'Virtual production', 'Animation and motion', 'Design', 'Digital and social assets', 'Post-production', 'Adaptation and localisation', 'Content at scale'], 'still-craft'),
    ('In-house creative', "Boost your in-house team with freshness and firepower on demand or embedded. Many in-house teams carry a \u2018negative trust equity\u2019 with the business for years. Through our plug and play services built for in-house agencies, we put award winning creatives and strategists alongside your team within days, to crack briefs, develop campaigns, and strengthen design. We can also give you \u2018strategy on demand\u2019 over WhatsApp. Together, they help your team earn its place as a strategic partner.",
     ['Strategic projects', 'Campaign development', 'Design projects', 'Creative direction', 'Creative mentoring', 'Production excellence', 'Ongoing creative support'], 'still-pie'),
]

def page_services(L, A):
    rows = []
    for i, (name, txt, caps, img) in enumerate(WHATWEDO):
        cap = ''.join(f'<li>{esc(c)}</li>' for c in caps)
        more = ''
        l2 = None
        if SERVICE_PAGES_LIVE:
            from service_pages import LEVEL2
            l2 = next((x for x in LEVEL2 if x['name'].lower() == name.lower()), None)
            if l2 and l2.get('children'):
                names = {c['name'].lower() for c in l2['children']}
                cap = (''.join(f'<li><a href="{L(c["path"])}">{esc(c["name"])}</a></li>' for c in l2['children'])
                       + ''.join(f'<li>{esc(c)}</li>' for c in caps if c.lower() not in names))
            if l2: more = f'<a class="sec-link svc-more" href="{L(l2["path"])}">Explore {esc(name.lower())}</a>'
        head = esc(name)
        if SERVICE_PAGES_LIVE and l2: head = f'<a class="k-link" href="{L(l2["path"])}">{esc(name)}</a>'
        rows.append(f'<li class="wwd"><div class="kk"><span class="wn">{i+1:02d}</span><h2 class="k">{head}</h2></div><div class="v"><p>{esc(txt)}</p><ul class="caps">{cap}</ul>{more}</div></li>')
    c3caps = ''.join(f'<li>{esc(c)}</li>' for c in ['Cultural partnerships', 'Culture3: Offstage', 'A Culture3 Conversation', 'Brand partnerships', 'Cultural strategy and programming', 'Original film and content'])
    rows.append(f'<li class="wwd"><div class="kk"><span class="wn">06</span><h2 class="k k-logo"><a class="k-link" href="{L("culture3/")}">{c3_logo()}</a></h2></div><div class="v"><p>Culture3 works directly with brands and organisations to build bespoke cultural partnerships, content, and experiences, from partnerships with TED to Offstage at Cannes and A Culture3 Conversation. We find the right moments, voices, and partners to earn a credible place in culture, rather than simply buy attention.</p><ul class="caps">{c3caps}</ul><a class="sec-link svc-more" href="{L("culture3/")}">Explore Culture3</a></div></li>')
    faq = '\n'.join(f'<details{" open" if i == 0 else ""}><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for i, (q, a) in enumerate(FAQ))
    return f'''<section class="page-hero wrap">
  <h1>What <span class="thin">we do</span></h1>
  <div class="intro"><div class="stack">
    <p>We can run everything from naming to brand building to production, end to end, or plug into your in-house teams. Same quality of talent either way.</p>
  </div></div>
</section>
<div class="sizzle wrap"><video class="lazyvid" muted loop playsinline preload="none" poster="{A("media/still-craft.webp")}" data-src="{A("film/sizzle-services.mp4")}" aria-hidden="true"></video></div>
<section class="band tight wrap" aria-label="Services">
  <ul class="wwd-list">
{chr(10).join(rows)}
  </ul>
</section>
{logo_wall(A)}
{cta(L)}'''

def page_culture(L, A):
    boxes = [('Partnerships that matter', 'Platforms, institutions, and organisations that create access, credibility, and distinctive opportunities. Proof: TED, and a pipeline of new and impactful partnerships.'),
             ('Moments that matter', 'Events, formats, and spaces where the relevant conversations are happening. Live programming, salons, and original formats such as Offstage.'),
             ('Voices that matter', 'Thinkers, speakers, creators, and specialists who bring authority, perspective, and cultural relevance to a conversation.'),
             ('Creativity that matters', "Freedom Works' global network of independent creatives, bringing culturally fluent perspectives across markets, disciplines, and communities.")]
    bx = '\n'.join(f'<div class="box"><h2>{esc(k)}</h2><p>{esc(v)}</p></div>' for k, v in boxes)
    ted = f'<img class="ted-logo" src="{A("logos/ted.webp")}" alt="Including TED" width="1280" height="471">'
    offers = [
        ('<h3>Cultural partnerships</h3>', 'Strategic partnerships and cultural access', ted,
         'We connect brands and organisations with established cultural institutions, platforms and intellectual property, and build bespoke opportunities across content, events, influential voices, and audience engagement. This includes partnerships with TED, one of the world\u2019s leading platforms for ideas, whose ecosystem of voices, content, and events gives brands a credible role in the conversations shaping their industry.'),
        (f'<h3 class="c3n"><span class="c3-inline">{c3_logo()}</span>: Offstage</h3>', 'Event sponsorship and partnerships', '',
         'Culture3\u2019s curated event series for C-suite leaders, decision makers and cultural voices, held at key moments such as Cannes. Brands sponsor an intimate, moderated conversation built around their industry, with access to a carefully curated room of people and perspectives.'),
        (f'<h3 class="c3n">A <span class="c3-inline">{c3_logo()}</span> Conversation</h3>', 'Sponsored conversations and cultural partnerships', '',
         'A focused, programmed discussion on a question that matters to a brand\u2019s industry, at moments such as SXSW London. We find the topic, partners, and speakers, with the option to extend the conversation into editorial content.'),
        ('<h3>Brand partnerships</h3>', 'Brand strategy, content, and experiences', '',
         'We work directly with brands and organisations on bespoke cultural partnerships, from original film and editorial series to curated events and live experiences, to give them a credible role in culture and reach new audiences.')]
    ol = '\n'.join(f'      <li><div class="ok">{h}<p class="os">{esc(sub)}</p>{extra}</div><p class="ov">{esc(d)}</p></li>' for h, sub, extra, d in offers)
    return f'''<section class="page-hero c3-hero wrap">
  <h1>Culture gets <span class="thin">you noticed.</span></h1>
  <div class="intro"><div class="stack">
    <p>AI can talk about culture. It can never be in it. Culture3 puts brands in the rooms that matter: offstage dinners with cultural leaders, onstage with TED, amplified beyond it through organic and paid media. Physical. Nuanced. Human.</p>
  </div></div>
</section>
<div class="sizzle wrap"><video class="lazyvid" muted loop playsinline preload="none" poster="{A("media/poster-culture3.webp")}" data-src="{A("film/sizzle-culture.mp4")}" aria-hidden="true"></video></div>
<section class="c3-direct c3-about wrap" aria-labelledby="c3a">
  <div class="l"><h2 class="c3-about-logo" id="c3a">{c3_logo()}</h2></div>
  <div class="r">
    <p class="lead">Bringing cultural access, strategic partnerships, relevant voices, and culturally fluent creativity together to build propositions, formats, and opportunities that let a brand take part in culture. It draws on the wider Freedom Works network where needed.</p>
  </div>
</section>
<section class="band tight wrap flush-top" aria-label="What Culture3 brings">
  <div class="boxes four">
{bx}
  </div>
</section>
{strip3(A, "c3-pwc-earth", "c3-offstage", "c3-pwc-skyline", ("50% 40%", "50% 45%", "50% 40%"))}
<section class="c3-method band wrap" aria-labelledby="c3m">
  <div class="split split-head">
    <div class="l"><p class="sec-lbl"><span class="mk" aria-hidden="true"></span>Our methodology</p><h2 class="h2" id="c3m">Where to show up. Who to show up with. <span class="thin">What to build.</span></h2></div>
  </div>
  <ol class="c3-steps">
    <li><span class="sn">01</span><h3>Strategy</h3><p>We find the cultural opportunities, audiences, and moments that fit a brand\u2019s commercial or cultural ambitions.</p></li>
    <li><span class="sn">02</span><h3>Access</h3><p>We connect brands with established cultural institutions, communities, and influential voices.</p></li>
    <li><span class="sn">03</span><h3>Programming</h3><p>We develop and curate events, conversations, and experiences that bring cultural ideas to life.</p></li>
    <li><span class="sn">04</span><h3>Content</h3><p>We make original film, editorial series, and content that builds cultural relevance and keeps audiences engaged.</p></li>
  </ol>
</section>
<section class="band dark" aria-labelledby="c3o">
  <div class="wrap">
    <div class="split split-head">
      <div class="l"><h2 class="h2" id="c3o">Culture3 <span class="thin">offerings</span></h2></div>
    </div>
    <ul class="c3-offers">
{ol}
    </ul>
  </div>
</section>
{cta(L)}'''

def page_work(L, A):
    return f'''<section class="page-hero tight wrap">
  <h1>Work that <span class="thin">matters.</span></h1>
  <div class="intro"><div class="stack"><p>Creative work should move the numbers a board cares about: sales, share, demand, and value. Here\u2019s what ours has done:</p></div></div>
</section>
<div class="sizzle wrap"><video class="lazyvid" muted loop playsinline preload="none" poster="{A("media/still-mountain.webp")}" data-src="{A("film/sizzle-work.mp4")}" aria-hidden="true"></video></div>
<section class="work wrap flush-top">
  <div class="grid">
    {chr(10).join(tile(p, L, A, 'h2') for p in PROJECTS)}
  </div>
</section>
{impact_html(L, A, logos=False, heading='The numbers', intro=False)}
{clients_wall()}
{cta(L)}'''

def page_project(i, L, A):
    p = PROJECTS[i]; nx = PROJECTS[(i + 1) % len(PROJECTS)]
    if p.get('vimeo'):
        vid, h = p['vimeo']
        poster = f'<img src="{A("media/"+p["img"]+".webp")}" alt="">' if p['img'] else f'<div class="typo"><span class="tn">{esc(p["camp"])}</span></div>'
        if p.get('loop'):
            poster += f'<video class="lazyvid" muted loop playsinline preload="none" data-src="{A("film/loop-"+p["loop"]+".mp4")}" aria-hidden="true"></video>'
        film = f'<div class="film" data-vimeo="{vid}"' + (f' data-h="{h}"' if h else '') + f'>{poster}<button class="play" type="button" aria-label="Play the {esc(p["client"])} film"><svg width="18" height="18" viewBox="0 0 18 18" aria-hidden="true"><path d="M4 2l12 7-12 7z" fill="currentColor"/></svg><span>Play film</span></button></div>'
    elif p['img'] and p.get('loop'):
        # no film to play: the still with its loop running over it
        film = f'<div class="film still-loop"><img src="{A("media/"+p["img"]+".webp")}" alt="{esc(p["client"])}, {esc(p["camp"])}"><video class="lazyvid" muted loop playsinline autoplay preload="none" data-src="{A("film/" + (p["herofilm"] if p.get("herofilm") else "loop-" + p["loop"]) + ".mp4")}" aria-hidden="true"></video></div>'
    elif p['img']:
        film = f'<img class="wide" src="{A("media/"+p["img"]+".webp")}" alt="{esc(p["client"])}, {esc(p["camp"])}">'
    else:
        film = f'<div class="film static"><div class="typo"><span class="tn">{num_html(p["n"] or p["client"])}</span><span class="tc">{esc(p["l"])}</span></div></div>'
    extra = ''.join(f'<li>{esc(e)}</li>' for e in p['extra'])
    extra = f'<ul>{extra}</ul>' if extra else ''
    body = ''
    if p['copy'] or p['n']:
        res = f'<div class="res"><span class="n" data-count>{num_html(p["n"])}</span><span class="l">{esc(p["l"])}</span>{extra}</div>' if p['n'] else ''
        body = f'<section class="proj-body wrap"><p class="brief">{esc(p["copy"])}</p>{res}</section>'
    secs = ''
    for lbl, head, paras, items in p.get('sections', []):
        li = ''.join(f'<li>{esc(x)}</li>' for x in (items or []))
        secs += f'<div class="cs-sec"><h2><span class="lbl">{esc(lbl)}</span>{esc(head)}</h2><div class="cs-body">' + ''.join(f'<p>{esc(x)}</p>' for x in paras) + (f'<ul>{li}</ul>' if li else '') + '</div></div>'
    if secs: secs = f'<section class="cs-sections wrap">{secs}</section>'
    gal = ''.join(f'<img src="{A("media/"+g+".webp")}" alt="" loading="lazy">' for g in p.get('gallery', []))
    if gal: gal = f'<div class="cs-gallery wrap" aria-hidden="true">{gal}</div>'
    q = ''
    if p['quote']:
        qtxt = esc(p["quote"][0]).replace('\n', '<br><br>')
        src = f'<span class="src">{esc(p["quote"][3])}</span>' if len(p["quote"]) > 3 else ''
        q = f'<section class="voice proj-quote wrap" aria-label="Client quote"><blockquote>\u201c{qtxt}\u201d</blockquote><p class="who">{esc(p["quote"][1])}<span>{esc(p["quote"][2])}</span>{src}</p></section>'
    return f'''<section class="proj-hero wrap">
  {case_logo(p, A)}
  <h1>{esc(p["camp"])}</h1>
</section>
<div class="proj-img wrap">{film}</div>
{body}
{secs}
{gal}
{q}
<nav class="wrap" aria-label="Next project"><a class="next" href="{L("work/"+nx["slug"]+"/")}"><span class="k">Next project</span><span class="t">{esc(nx["client"])}</span></a></nav>
{cta(L)}'''

def page_thinking(L, A):
    used = [t for t in TAGS if any(p['tag'] == t for p in POSTS)]
    btn = '<button type="button" aria-pressed="true" data-f="all">All</button>' + ''.join(f'<button type="button" aria-pressed="false" data-f="{t}">{esc(TAGS[t])}</button>' for t in used)
    return f'''<section class="page-hero tight wrap intro-left">
  <h1>Thinking</h1>
  <div class="intro"><div class="stack"><p>{len(POSTS)} articles on creativity, AI, talent, and the agency model.</p></div></div>
</section>
<section class="thinking wrap">
  {topic_nav(L, None)}
  {post_cards(POSTS, L, A, with_data=True)}
</section>
{cta(L)}'''

def opens_with_image(html, blocks=3):
    """True when one of the article's first few blocks already holds a picture (so adding the cover would show it twice)."""
    for i, m in enumerate(re.finditer(r'<(p|h[1-6]|ul|ol|blockquote|figure|div)\b[^>]*>(.*?)</\1>', html, re.S)):
        if i >= blocks: break
        if '<img' in m.group(2): return True
    return False

def page_article(p, L, A, strip_images=False):
    body = markdown.markdown(p['body_md'], extensions=['extra'])
    body = localise_inline(body, A)
    body = re.sub(r'<img ', '<img loading="lazy" ', body)
    e = IMGMAP.get(p['slug']) or {}; loc = local_img(p['slug'])
    src = e.get('src') or ''
    hit = next((c for c in (src, src.replace('&', '&amp;')) if c and c in body), None)   # the body's own copy, however its address is written
    if loc and hit:
        body = body.replace(hit, A(loc))
    elif loc and e.get('from') == 'cover' and not opens_with_image(body):
        body = f'<p><img loading="lazy" src="{A(loc)}" alt=""></p>' + body      # add the cover only when the article doesn’t already open with a picture
    if strip_images:
        body = re.sub(r'<p>\s*<img[^>]*src="http[^"]*"[^>]*>\s*</p>', '', body); body = re.sub(r'<img[^>]*src="http[^"]*"[^>]*>', '', body)
    tag = TAGS.get(p['tag'], 'Thinking')
    body = link_first_service(body, L)
    topic_link = f'<a href="{L("thinking/" + TOPIC_SLUG[p["tag"]] + "/")}">{esc(tag)}</a>' if p['tag'] in TOPIC_SLUG else esc(tag)
    return f'''<article>
  <header class="article-head wrap">
    <p class="k">{topic_link}</p>
    <h1>{esc(p["title"])}</h1>
    <p class="meta">By {byline(p, L)}. {month(p["date"])}. Originally published by The Liberty Guild, now Freedom Works. <a href="{esc(p["originalUrl"])}">Read the original</a></p>
  </header>
  <div class="article-body wrap"><div class="prose">
{body}
  {share_row(p)}
  </div></div>
</article>
{next_step(p, L)}
{more_on_topic(p, L, A)}
<a class="sticky-cta" href="{L("contact/")}" data-cta="article-sticky-talk-to-us">Talk to us <span aria-hidden="true">\u2192</span></a>
{cta(L)}'''

def slug_name(n):
    import unicodedata
    n = unicodedata.normalize('NFKD', n).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]+', '-', n.lower()).strip('-')

def svc_by_name(name):
    from service_pages import SERVICE_PAGES
    return next((x for x in SERVICE_PAGES if x['name'] == name), None)

def byline(p, L):
    a = p['author']
    if a == 'Freedom Works':
        return f'<a href="{L("agency/")}">Freedom Works</a>'
    role = AUTHOR_ROLE.get(a)
    return f'<a href="{L("agency/")}#{slug_name(a)}">{esc(a)}</a>' + (f', {esc(role)}' if role else '')

SVC_PHRASES = [(r'brand strategy', 'Brand strategy'), (r'brand positioning', 'Brand positioning'), (r'communications strategy|comms strategy', 'Communications strategy'),
               (r'brand architecture', 'Brand architecture'), (r'brand identity', 'Brand identity'), (r'rebrand(?:ing|s)?\b', 'Brand development and rebranding'),
               (r'visual identity|brand guidelines', 'Visual identity and brand guidelines'), (r'product launch|brand launch', 'Brand and product launches'),
               (r'campaign strategy', 'Campaign strategy and development'), (r'virtual production', 'Virtual production'), (r'post-production', 'Post-production'),
               (r'AI production|AI produced|fully AI', 'AI production'), (r'in-house (?:creative|agenc(?:y|ies)|teams?)', 'In-house creative')]

def link_first_service(body, L):
    """One in-text link per article: the first natural mention of a service, outside headings, quotes, and existing links."""
    parts = re.split(r'(<[^>]+>)', body); depth = 0
    for i, part in enumerate(parts):
        if part.startswith('<'):
            tag = re.match(r'</?\s*([a-zA-Z0-9]+)', part)
            if tag and tag.group(1).lower() in ('a', 'h1', 'h2', 'h3', 'h4', 'blockquote', 'figcaption'):
                depth += -1 if part.startswith('</') else 1
            continue
        if depth > 0 or not part.strip(): continue
        for rx, name in SVC_PHRASES:
            m = re.search(r'\b(' + rx + r')', part, re.I)
            sp_ = svc_by_name(name) if m else None
            if sp_:
                parts[i] = part[:m.start(1)] + f'<a href="{L(sp_["path"])}">{m.group(1)}</a>' + part[m.end(1):]
                return ''.join(parts)
    return body

def share_row(p):
    url = urllib.parse.quote(DOMAIN + '/thinking/' + p['slug'] + '/', safe=''); t = urllib.parse.quote(p['title'], safe='')
    return (f'<div class="share" aria-label="Share this article"><span class="lbl">Share</span>'
            f'<a href="https://www.linkedin.com/sharing/share-offsite/?url={url}" target="_blank" rel="noopener" data-share="linkedin">LinkedIn</a>'
            f'<a href="https://twitter.com/intent/tweet?url={url}&amp;text={t}" target="_blank" rel="noopener" data-share="x">X</a>'
            f'<a href="mailto:?subject={t}&amp;body={url}" data-share="email">Email</a>'
            f'<button type="button" data-copy="{esc(DOMAIN + "/thinking/" + p["slug"] + "/")}" data-share="copy">Copy link</button>'
            f'<span class="copied" role="status" aria-live="polite"></span></div>')

def next_step(p, L):
    main, second = TOPIC_SVC.get(p['tag'], ('Creative', 'Brand strategy'))
    a, b = svc_by_name(main), svc_by_name(second)
    if not a: return ''
    rel = f'<a href="{L(a["path"])}">{esc(main)}</a>' + (f', <a href="{L(b["path"])}">{esc(second)}</a>' if b else '')
    return (f'<aside class="next-step wrap" aria-labelledby="ns-h"><div class="ns-in"><h2 id="ns-h">Put this thinking <span class="thin">to work.</span></h2>'
            f'<p>Explore {esc(main[0].lower() + main[1:]) if not main.startswith("AI") else esc(main)}, or tell us about your brief.</p>'
            f'<div class="ns-btns"><a class="ct-btn" href="{L(a["path"])}" data-cta="article-explore-service">Explore {esc(main if main.startswith("AI") else main.lower())} <span aria-hidden="true">\u2192</span></a>'
            f'<a class="ct-btn ghost" href="{L("contact/")}" data-cta="article-talk-to-us">Talk to us</a></div>'
            f'<p class="rel">Related services: {rel}</p></div></aside>')

def more_on_topic(p, L, A):
    same = [x for x in POSTS if x['tag'] == p['tag'] and x is not p]
    same.sort(key=lambda x: x['date'], reverse=True)
    picks = same[:3]
    if not picks: return ''
    t = TAGS.get(p['tag'], 'Thinking')
    return (f'<section class="more-on wrap" aria-labelledby="mo-h"><div class="mo-head"><h2 class="h2" id="mo-h">More on <span class="thin">{esc(t[0].lower() + t[1:]) if not t.startswith("AI") else esc(t)}</span></h2>'
            f'<p class="mo-links"><a class="sec-link" href="{L("thinking/" + TOPIC_SLUG[p["tag"]] + "/")}">All {esc((t if t.startswith("AI") else t.lower()).replace("the agency model", "agency model"))} articles</a> <a class="sec-link" href="{L("thinking/")}">All articles</a></p></div>'
            f'{post_cards(picks, L, A)}</section>')

def topic_nav(L, current):
    items = [('All', 'thinking/', current is None)] + [(TAGS[t], 'thinking/' + TOPIC_SLUG[t] + '/', current == t) for t in TOPIC_SLUG if any(x['tag'] == t for x in POSTS)]
    cur_ = ' aria-current="page"'
    return '<nav class="filters topic-nav" aria-label="Thinking topics">' + ''.join(f'<a href="{L(h)}"{cur_ if on else ""}>{esc(n)}</a>' for n, h, on in items) + '</nav>'

def page_topic(tag):
    def fn(L, A, **k):
        posts = sorted([x for x in POSTS if x['tag'] == tag], key=lambda x: x['date'], reverse=True)
        return f"""<section class="page-hero tight wrap intro-left">
  <p class="sec-lbl"><span class="mk" aria-hidden="true"></span><a href="{L("thinking/")}">Thinking</a></p>
  <h1>{esc(TAGS[tag])}</h1>
  <div class="intro"><div class="stack"><p>{esc(TOPIC_INTRO[tag])}</p><p class="count">{len(posts)} articles</p></div></div>
</section>
<section class="thinking wrap">
  {topic_nav(L, tag)}
  {post_cards(posts, L, A)}
</section>
{cta(L)}"""
    return fn

def page_dni(L, A):
    return legal_shell('Diversity <span class="thin">and inclusion</span>', 'Our statement on diversity, inclusion, and the freedom to be yourself.', legal_md('diversity-inclusion', L))

def page_msa(L, A):
    return legal_shell('Modern slavery <span class="thin">statement</span>', 'How we guard against slavery and human trafficking in our business and supply chain.', legal_md('modern-slavery-statement', L))

def page_contact(L, A):
    return f'''<section class="contact contact-page" aria-labelledby="ct">
  <div class="wrap">
    <h1 id="ct">Let’s make <span class="thin">work that matters.</span></h1>
    {contact_cards(big=True, hl='h2', L=L)}
    <div class="ct-office"><p class="sec-lbl"><span class="mk" aria-hidden="true"></span>Visit us</p><address>{"<br>".join(OFFICE_ADDRESS)}</address></div>
  </div>
</section>'''

def page_404(L, A):
    return f'''<section class="nf wrap">
  <h1 class="h2">This page <span class="thin">doesn’t exist.</span></h1>
  <p class="lead-light">It may have moved when we became Freedom Works.</p>
  <p><a class="sec-link" href="{L("")}">Go to the homepage</a> &nbsp; <a class="sec-link" href="{L("work/")}">See the work</a></p>
</section>'''

F = lambda t: f'<span class="fill">[{t}]</span>'     # a detail Freedom Works must supply before launch

def legal_page(title_html, intro, sections, updated):
    body = ''.join(f'<h2>{h}</h2>' + ''.join(x if x.startswith('<') else f'<p>{x}</p>' for x in ps) for h, ps in sections)
    return f"""<section class="page-hero tight wrap legal-hero"><h1 class="h2">{title_html}</h1><p class="lead-light">{intro}</p></section>
<section class="legal-body wrap"><div class="prose">{body}<p class="updated">Last updated: {updated}</p></div></section>"""

def legal_md(name, L):
    """Render one of Freedom Works' legal texts (src/legal/<name>.md). Edit those files to change the wording."""
    t = open(os.path.join(ROOT, 'src', 'legal', name + '.md'), encoding='utf-8').read()
    t = re.sub(r'(?m)^(#{1,5}) ', lambda m: '#' + m.group(1) + ' ', t)           # document headings sit under the page title
    h = markdown.markdown(t, extensions=['tables'])
    decl = (f'<div class="cookie-declaration"><script id="CookieDeclaration" src="https://consent.cookiebot.com/{COOKIEBOT_ID}/cd.js" async></script></div>' if COOKIEBOT_ID
            else '<p class="note">The full, up-to-date list of the cookies this website uses will appear here once our cookie consent tool is live.</p>')
    for k, v in {'{privacy}': L('privacy/'), '{cookies}': L('cookies/'), '{terms}': L('terms/'),
                 '<p>{declaration}</p>': decl,
                 '<p>{settings}</p>': '<p><button type="button" class="sec-link cookie-settings" data-cookie-settings>Change your cookie settings</button></p>'}.items():
        h = h.replace(k, v)
    return re.sub(r'(<table>.*?</table>)', r'<div class="tbl-scroll">\1</div>', h, flags=re.S)

def legal_shell(title_html, intro, body):
    return f"""<section class="page-hero tight wrap legal-hero"><h1 class="h2">{title_html}</h1><p class="lead-light">{intro}</p></section>
<section class="legal-body wrap"><div class="prose">{body}</div></section>"""

def page_privacy(L, A):
    return legal_shell('Privacy <span class="thin">policy</span>', 'How Freedom Works collects and uses your personal data, and your rights.', legal_md('privacy', L))

def page_cookies(L, A):
    return legal_shell('Cookie <span class="thin">policy</span>', 'How this website uses cookies, and how to change your consent at any time.', legal_md('cookies', L))

def page_terms(L, A):
    return legal_shell('Terms <span class="thin">of use</span>', 'The terms that apply when you use the Freedom Works website.', legal_md('terms', L))

# ---------------- chrome ----------------
def header(L, A, active, theme='light'):
    cur = ' aria-current="page"'
    cta_attr = ' data-cta="header-talk-to-us"'
    dd = ''.join(f'<li><a href="{L(sp_)}">{esc(n)}</a></li>' for n, sp_ in L2_SERVICES)
    def nav_item(p, t):
        a = f'<a href="{L(p)}"{cur if p == active else ""}{cta_attr if p == "contact/" else ""}>{t}</a>'
        if p != 'services/': return a
        return (f'<div class="nav-dd">{a}<button class="dd-btn" type="button" aria-expanded="false" aria-controls="dd-svc" aria-label="Show services">{CHEVRON}</button>'
                f'<div class="dd-panel" id="dd-svc"><ul>{dd}</ul></div></div>')
    links = ''.join(nav_item(p, t) for p, t in NAV)
    sub = '<ul class="sub">' + ''.join(f'<li><a href="{L(sp_)}">{esc(n)}</a></li>' for n, sp_ in L2_SERVICES) + '</ul>'
    hs = ' class="has-sub"'
    big = ''.join(f'<li{hs if p == "services/" else ""}><a href="{L(p)}"{cur if p == active else ""}>{t}</a>{sub if p == "services/" else ""}</li>' for p, t in NAV)
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-head" data-theme="{theme}">
  <a class="mark" href="{L("")}" aria-label="Freedom Works home"><img class="lg-white" src="{A("brand/logo-white-480.png")}" alt="Freedom Works logo" width="480" height="86"><img class="lg-indigo" src="{A("brand/logo-indigo-480.png")}" alt="Freedom Works logo" aria-hidden="true" width="480" height="86"></a>
  <nav aria-label="Main">{links}</nav>
  <button class="menu-btn" type="button" aria-expanded="false" aria-controls="menu"><span class="bars" aria-hidden="true"></span>Menu</button>
</header>
<div class="overlay" id="menu" role="dialog" aria-modal="true" aria-label="Menu">
  <div class="top"><img src="{A("brand/logo-linen-480.png")}" alt="Freedom Works" width="480" height="86" loading="lazy"><button class="menu-btn" type="button" data-close>Close</button></div>
  <ul>{big}</ul>
</div>'''

def footer(L, A):
    links = ''.join(f'<a href="{L(p)}">{t}</a>' for p, t in NAV[:6])
    return f'''<footer class="foot wrap">
  <div class="brand"><img src="{A("brand/logo-linen-480.png")}" alt="Freedom Works" width="480" height="86" loading="lazy"><span>A global creative agency.<br>Calibre, Culture, Craft.</span><address class="f-addr">{"<br>".join(OFFICE_ADDRESS)}</address></div>
  <div class="links">{links}<a href="https://www.linkedin.com">LinkedIn</a><a href="https://www.instagram.com">Instagram</a></div>
  <div class="fsvc"><p class="fh">Services</p>{''.join(f'<a href="{L(sp_)}">{esc(n)}</a>' for n, sp_ in L2_SERVICES)}</div>
  <div class="legal"><a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a><span>\u00a9 {datetime.date.today().year} Freedom Works, London</span><a href="{L("privacy/")}">Privacy</a><a href="{L("cookies/")}">Cookies</a><a href="{L("terms/")}">Terms</a><a href="{L("modern-slavery-statement/")}">Modern slavery statement</a><a href="{L("diversity-inclusion/")}">Diversity and inclusion</a><button type="button" class="cookie-settings" data-cookie-settings>Cookie settings</button></div>
</footer>
<div class="foot-mark" aria-hidden="true"><img src="{A("brand/logo-white.png")}" alt="Freedom Works logo" width="1600" height="287" loading="lazy"></div>'''

DARK_TOP = ('', 'contact/', '404')   # pages that open on a dark ground: the header starts in its light-on-dark state
FLOURISH_JS = open(SP('flourish.js')).read()
SHADERS_JS = open(SP('shaders.js')).read()
SCRIPT = '''<script>
(function(){
  var v=document.querySelector('.hero video'),b=document.querySelector('.pause');
  function st(p){if(b){b.setAttribute('aria-label',p?'Play film':'Pause film');b.classList.toggle('is-paused',p);}}
  if(v){v.playbackRate=.7;if(window.matchMedia('(prefers-reduced-motion: reduce)').matches){v.pause();v.removeAttribute('autoplay');v.preload='none';st(true);}}   /* the poster stays underneath the film, so reduced motion shows the still */
  if(b&&v){b.addEventListener('click',function(){if(v.paused){v.play();st(false);}else{v.pause();st(true);}});}
  document.querySelectorAll('.filters').forEach(function(f){f.addEventListener('click',function(e){var t=e.target.closest('button');if(!t)return;
    f.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===t?'true':'false');});
    var k=t.getAttribute('data-f');document.querySelectorAll('.cards li[data-tag]').forEach(function(li){li.hidden=!(k==='all'||li.getAttribute('data-tag')===k);});});});
})();
</script>
<script>''' + FLOURISH_JS + '''</script>
<script>''' + SHADERS_JS + '''</script>'''

ORG = {"@context": "https://schema.org", "@type": "Organization", "name": "Freedom Works", "alternateName": "FRE3DOM WORKS",
       "description": "A global creative agency built on Calibre, Culture and Craft: brand strategy, identity, creative, production, and in-house creative, from 600+ award winning independent creatives handpicked for every brief.",
       "slogan": "Freedom makes better work.",
       "url": DOMAIN, "logo": DOMAIN + "/assets/brand/logo-indigo.png", "address": {"@type": "PostalAddress", "streetAddress": "Johnson Building, Johnson Gardens, 77 Hatton Garden", "addressLocality": "London", "postalCode": "EC1N 8JS", "addressCountry": "GB"}, "email": "hello@freedom.works", "contactPoint": {"@type": "ContactPoint", "contactType": "new business", "email": "hello@freedom.works", "url": DOMAIN + "/contact/"},
       "subOrganization": {"@type": "Organization", "name": "Culture3", "url": DOMAIN + "/culture3/", "description": "Culture3 puts brands in the rooms that matter, bringing cultural access, strategic partnerships, relevant voices, and culturally fluent creativity together, from Offstage dinners to partnerships with TED."}}

def crumbs(path, title):
    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": DOMAIN + "/"}]
    parts = [x for x in path.strip('/').split('/') if x]
    names = {'work': 'Work', 'agency': 'About', 'the-guild': 'The Guild', 'services': 'Services', 'culture3': 'Culture3', 'thinking': 'Thinking', 'contact': 'Contact'}
    for i, part in enumerate(parts):
        nm = names.get(part, title) if i < len(parts) - 1 or part in names else title
        items.append({"@type": "ListItem", "position": i + 2, "name": nm, "item": DOMAIN + "/" + "/".join(parts[:i + 1]) + "/"})
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}

# ---------------- service pages (SEO: one page per service / sub-service) ----------------
SERVICE_PAGES_LIVE = True   # flip to True to publish the service pages, add them to the sitemap and link them from Services
DRAFTS = [False]
STAGING = bool(os.environ.get('REPL_ID') or os.environ.get('STAGING') == '1')
# Video hosting: set VIDEO_CDN (e.g. https://freedomworks.b-cdn.net) in Netlify to serve every .mp4 from Bunny instead of the site.
# Upload the site's assets/film and assets/media .mp4 files to Bunny under the same paths (/assets/film/..., /assets/media/...).
VIDEO_CDN = os.environ.get('VIDEO_CDN', '').rstrip('/')
# Leadership details not supplied yet stay hidden (roles 'to confirm', '00 Stat to come', 'Portrait to come'). Set to False to show the gaps.
HIDE_PENDING = True
# Cookiebot: set COOKIEBOT_ID in Netlify (or put the ID here as the default). Manual blocking mode: all tracking already runs through
# Google Consent Mode, and auto-blocking would hide the HubSpot form and Vimeo films from visitors who decline cookies.
COOKIEBOT_ID = os.environ.get('COOKIEBOT_ID', 'c9e759c8-bb2b-436a-9904-497e636e9d29')
# Analytics: Braidr's Google Tag Manager container (GA4 lives inside it). Off on Replit review copies so test traffic never reaches the figures.
GTM_ID = os.environ.get('GTM_ID', 'GTM-5326PCK7')
ANALYTICS_ON = bool(GTM_ID) and GTM_ID.lower() != 'off' and not os.environ.get('REPL_ID')
CONTACT_EMAIL = 'hello@freedom.works'   # review copies (Replit) are hidden from search engines
CASE_PAGES = True    # long case study pages. Set False to hide them (tiles then play the film in a pop-up instead).
import sys as _sys
_sys.path.insert(0, SP(''))
from service_pages import SERVICE_PAGES, Q as SVC_QUOTES

def related_posts(keywords, n=3):
    def score(p):
        hay = (p['title'] + ' ' + (p.get('description') or '')).lower()
        return sum(1 for k in keywords if k in hay)
    pool = [p for p in POSTS if 'b corp' not in p['title'].lower()]   # certification has lapsed: never suggest these
    ranked = sorted(pool, key=lambda p: (-score(p), p['date']), reverse=False)
    picked = [p for p in ranked if score(p) > 0][:n]
    return picked if len(picked) == n else (picked + [p for p in POSTS if p not in picked])[:n]

def svc_crumbs(sp):
    trail = [('Home', ''), ('Services', 'services/')]
    if sp.get('parent'): trail.append((sp['parent']['name'], sp['parent']['path']))
    trail.append((sp['name'], sp['path']))
    return trail

def page_service(sp, L, A):
    trail = svc_crumbs(sp)
    crumbs_html = ''.join((f'<li><a href="{L(p)}">{esc(n)}</a></li>' if i < len(trail) - 1 else f'<li aria-current="page">{esc(n)}</li>') for i, (n, p) in enumerate(trail))
    # optical sizing: equal visual area per logo (narrow marks taller, wide wordmarks shorter)
    logos = svc_logos(sp, A)
    about = ''.join(f'<p>{esc(x)}</p>' for x in sp['about'][1:])
    stats = ''.join(f'<li><b data-count>{num_html(n)}</b><span>{esc(t)}</span><em>{esc(c)}</em></li>' for n, t, c in sp['stats'][:3])
    stats_ul = f'<ul class="svc-stats">{stats}</ul>' if stats else ''
    steps = ''.join(f'<li><span class="n">{i+1:02d}</span><h3>{esc(n)}</h3><p>{esc(t)}</p></li>' for i, (n, t) in enumerate(sp['process']))
    if sp['level'] == 2:
        links = sp['children']; svc_label = 'Services' if links else 'What\u2019s included'
        caps = sp.get('extra_caps', [])
        def cap_row(c):
            n, d = (c if isinstance(c, (tuple, list)) else (c, ''))
            return f'<li class="plain"><span class="k">{esc(n)}</span><span class="d">{esc(d)}</span><span class="go" aria-hidden="true"></span></li>'
        extra = ((f'<li class="sub-head"><span>Also part of {esc(sp["name"].lower())}</span></li>' if links and caps else '') + ''.join(cap_row(c) for c in caps))
    else:
        par = sp['parent']; links = [c for c in par['children'] if c is not sp] + [par]; svc_label = 'Related services'; extra = ''
    rows = ''.join(f'<li><a href="{L(c["path"])}"><span class="k">{esc(c["name"]) if c is not sp.get("parent") else "All " + esc(c["name"].lower())}</span><span class="d">{esc(c["line"])}</span><span class="go" aria-hidden="true">\u2192</span></a></li>' for c in links) + extra
    projs = {p['slug']: p for p in PROJECTS}
    tiles = '\n'.join(tile(projs[s_], L, A) for s_ in relevant_cases(sp) if s_ in projs)
    quote_html = ''
    if sp['quotes']:
        qt, qn, qr = SVC_QUOTES[sp['quotes'][0]]
        quote_html = '<figure class="svc-quote"><blockquote>\u201c' + esc(qt) + '\u201d</blockquote><figcaption><b>' + esc(qn) + '</b>' + esc(qr) + '</figcaption></figure>'
    work_row = ''
    if tiles:
        work_row = ('<section class="svc-row wrap" aria-labelledby="s-work"><h2 class="svc-label" id="s-work">Work</h2><div class="svc-body">\n'
                    + '  <div class="grid svc-tiles">' + tiles + '</div>\n'
                    + f'  <a class="sec-link" href="{L("work/")}">See all work</a>\n</div></section>')
    if quote_html:
        work_row += ('\n<section class="svc-row wrap" aria-labelledby="s-say"><h2 class="svc-label" id="s-say">What clients say</h2><div class="svc-body">\n  '
                     + quote_html + '\n</div></section>')
    faqs = ''.join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in sp['faqs'][:4])
    by_slug = {x['slug']: x for x in POSTS}
    chosen = [next(x for x in POSTS if x['slug'].startswith(k)) for k in sp.get('articles', []) if any(x['slug'].startswith(k) for x in POSTS)] or related_posts(sp['keywords'])
    arts = post_cards(chosen[:3], L, A)
    return f'''<div class="svcpage">
{'<div class="draft-banner">Example page with starter copy, for review. Not yet live on the site.</div>' if DRAFTS[0] and not SERVICE_PAGES_LIVE else ''}
<header class="svc-top wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><ol>{crumbs_html}</ol></nav>
  <h1>{sp["h1"]}</h1>
  <div class="svc-top-row">
    <p class="svc-intro">{esc(sp["intro"])}</p>
    <div class="svc-cta"><a class="ct-btn" data-cta="service-talk-to-us" href="{L("contact/")}">{esc(sp["cta"])} <span aria-hidden="true">\u2192</span></a></div>
  </div>
  {('<div class="svc-logos"><p class="svc-label">Trusted by</p><ul>' + logos + '</ul></div>') if logos else ''}
</header>
{svc_hero_img(sp, L, A)}
<section class="svc-row wrap" aria-labelledby="s-exp"><h2 class="svc-label" id="s-exp">Our experience</h2><div class="svc-body">
  <p class="svc-lead">{esc(sp["about"][0])}</p>{about}
  {stats_ul}
</div></section>
<section class="svc-row wrap" aria-labelledby="s-how"><h2 class="svc-label" id="s-how">How we work</h2><div class="svc-body"><ol class="svc-steps">{steps}</ol></div></section>
<section class="svc-row wrap" aria-labelledby="s-svc"><h2 class="svc-label" id="s-svc">{svc_label}</h2><div class="svc-body"><ul class="svc-links">{rows}</ul></div></section>
{work_row}
<section class="svc-row wrap" aria-labelledby="s-th"><h2 class="svc-label" id="s-th">Thinking</h2><div class="svc-body svc-thinking">{arts}<a class="sec-link" href="{L("thinking/")}">All articles</a></div></section>
</div>
{cta(L)}'''

SVC_HERO_IMG = {'services/brand-identity/': 'still-snowfox-ramen'}   # page-specific stills (default: the case study poster)
SVC_HERO_CASE = {'services/brand-strategy/': 'tui', 'services/brand-identity/': 'snowfox-group', 'services/creative/': 'wizz-air',
                 'services/production/': 'brompton', 'services/in-house/': 'loveholidays'}

def svc_hero_img(sp, L, A):
    """Main service pages: a still from a relevant case study, with a caption linking to it."""
    slug = SVC_HERO_CASE.get(sp['path'])
    proj = next((q for q in PROJECTS if q['slug'] == slug), None)
    if not proj or not proj.get('img'): return ''
    img = SVC_HERO_IMG.get(sp['path'], proj['img'])     # a page can use its own still from the case study
    src = os.path.join(OUT, 'assets', 'media', img + '.webp'); wh = ''
    try:
        from PIL import Image
        w, h = Image.open(src).size; wh = f' width="{w}" height="{h}"'
    except Exception: pass
    href = L('work/' + slug + '/')
    return (f'<figure class="svc-hero wrap"><a href="{href}" tabindex="-1" aria-hidden="true"><img src="{A("media/" + img + ".webp")}" alt="{esc(proj["client"])}, {esc(proj["camp"])}"{wh} decoding="async"></a>'
            f'<figcaption><a href="{href}">From our work for {esc(proj["client"])} <span aria-hidden="true">\u2192</span></a></figcaption></figure>')

def relevant_cases(sp, n=2):
    """Work on a service page only comes from clients in its own logo strip: its own picks first where they match, then the rest in logo order."""
    logos = sp.get('logos') or [x['slug'] for x in LOGOWALL[:8]]
    by_logo = {}
    for case, logo in CASE_LOGO.items(): by_logo.setdefault(logo, []).append(case)
    relevant = [c for l in logos for c in by_logo.get(l, [])]
    picks = [c for c in sp['cases'] if c in relevant] + [c for c in relevant if c not in sp['cases']]
    return picks[:n]

def service_schema(sp):
    url = DOMAIN + '/' + sp['path']
    svc = {"@context": "https://schema.org", "@type": "Service", "name": sp['name'], "serviceType": sp['name'], "url": url,
           "description": sp['intro'], "areaServed": "Worldwide", "provider": {"@type": "Organization", "name": "Freedom Works", "url": DOMAIN + "/"}}
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in sp['faqs']]}
    bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": DOMAIN + "/" + p} for i, (n, p) in enumerate(svc_crumbs(sp))]}
    return [svc, bc]

def page_service_map(L, A):
    from service_pages import LEVEL2
    blocks = ''
    for l2 in LEVEL2:
        rows = f'<li><a href="{L(l2["path"])}"><span class="k">{esc(l2["name"])}</span><span class="d">Level 2 \u00b7 /{l2["path"]} \u00b7 {esc(l2.get("volume",""))} searches/month</span><span class="go" aria-hidden="true">\u2192</span></a></li>'
        rows += ''.join(f'<li><a href="{L(c["path"])}"><span class="k">\u2014 {esc(c["name"])}</span><span class="d">Level 3 \u00b7 {esc(c.get("volume",""))} searches/month</span><span class="go" aria-hidden="true">\u2192</span></a></li>' for c in l2.get('children', []))
        caps = [c[0] if isinstance(c, (tuple, list)) else c for c in l2.get('extra_caps', [])]
        if caps: rows += f'<li class="plain"><span class="k">Covered on the Level 2 page</span><span class="d">{esc(", ".join(caps))}</span><span class="go"></span></li>'
        blocks += f'<section class="svc-row wrap"><h2 class="svc-label">{esc(l2["name"])}</h2><div class="svc-body"><ul class="svc-links">{rows}</ul></div></section>'
    blocks += f'<section class="svc-row wrap"><h2 class="svc-label">Culture3</h2><div class="svc-body"><ul class="svc-links"><li><a href="{L("culture3/")}"><span class="k">Culture3</span><span class="d">Kept as one page (SEO advice: volume is for generic culture terms). Optimise it for all culture-related searches.</span><span class="go" aria-hidden="true">\u2192</span></a></li></ul></div></section>'
    return f'''<div class="svcpage">
<div class="draft-banner">Prototype for review: 22 service pages with starter copy. Not live on the site.</div>
<header class="svc-top wrap">
  <h1>Service <em>pages</em></h1>
  <div class="svc-top-row"><p class="svc-intro">Five Level 2 service pages and seventeen Level 3 sub-service pages, structured from the SEO expansion plan. Lower-volume services are covered on their Level 2 page. Open any page to review its layout and starter copy.</p></div>
</header>
{blocks}
</div>'''

def service_page_entries():
    if DRAFTS[0]:
        yield ('services/map/', 'Service pages prototype | Freedom Works', 'Prototype map of the service pages.', page_service_map, 'services/', [])
    for sp in SERVICE_PAGES:
        yield (sp['path'], sp['title'], sp['desc'], (lambda sp: lambda L, A: page_service(sp, L, A))(sp), 'services/', service_schema(sp))

def pages():
    """yield (path, title, description, body_fn, active, extra_schema)"""
    yield ('', 'Freedom Works | Global creative agency, London', 'A global creative agency built on Calibre, Culture and Craft. More than 600 award winning independent creatives and strategists, handpicked for every brief.', page_home, '', [{"@context": "https://schema.org", "@type": "WebSite", "name": "Freedom Works", "url": DOMAIN + "/", "inLanguage": "en-GB"}])
    yield ('agency/', 'About | Freedom Works', 'Freedom makes better work. Our DNA of Calibre, Culture, and Craft, and the leadership behind Freedom Works, a global creative agency.', page_agency, 'agency/', [])
    yield ('the-guild/', 'The Guild | Freedom Works', '600+ of the world\u2019s best independent creatives, strategists, and producers across 37 countries and cultures, handpicked for every brief.', page_guild, 'the-guild/', [])
    faq_schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}
    yield ('services/', 'Services | Freedom Works', 'Brand strategy, identity, creative, production, and in-house creative, plus Culture3 cultural partnerships, from the best creative department in the world.', page_services, 'services/', [])
    if SERVICE_PAGES_LIVE or DRAFTS[0]:
        yield from service_page_entries()
    yield ('culture3/', 'Culture3 | Freedom Works', 'AI can talk about culture. It can never be in it. Culture3 puts brands in the rooms that matter, from Offstage dinners to partnerships with TED.', page_culture, 'culture3/', [])
    yield ('work/', 'Work | Freedom Works', 'Work that matters for Nestl\u00e9, P&G, TUI, Burger King, King Arthur Baking, Wizz Air, M&S Food, and loveholidays.', page_work, 'work/', [])
    for i, p in enumerate(PROJECTS if CASE_PAGES else []):
        art = {"@context": "https://schema.org", "@type": "CreativeWork", "name": f"{p['client']}: {p['camp']}", "creator": {"@type": "Organization", "name": "Freedom Works"}}
        yield (f'work/{p["slug"]}/', f'{p["client"]}: {p["camp"]} | Freedom Works', case_desc(p), (lambda i: lambda L, A: page_project(i, L, A))(i), 'work/', [art])
    yield ('thinking/', 'Thinking | Freedom Works', 'Articles on creativity, AI, talent, and the agency model from Freedom Works.', page_thinking, 'thinking/', [])
    for t in TOPIC_SLUG:
        if any(x['tag'] == t for x in POSTS):
            yield (f'thinking/{TOPIC_SLUG[t]}/', f'{TAGS[t]} | Freedom Works', fit_desc(TOPIC_INTRO[t]), page_topic(t), 'thinking/', [])
    for p in POSTS:
        art = {"@context": "https://schema.org", "@type": "Article", "headline": p['title'], "datePublished": p['date'], "author": ({"@type": "Organization", "name": "Freedom Works", "url": DOMAIN + "/"} if p['author'] == 'Freedom Works' else dict({"@type": "Person", "name": p['author']}, **({"url": AUTHOR_LINKEDIN[p['author']], "sameAs": AUTHOR_LINKEDIN[p['author']]} if p['author'] in AUTHOR_LINKEDIN else {"url": DOMAIN + "/agency/"}))), "publisher": {"@type": "Organization", "name": "Freedom Works"}}
        desc = fit_desc(p['description'] or p['title'], p['body_md'])
        yield (f'thinking/{p["slug"]}/', f'{p["title"]} | Freedom Works', desc, (lambda p: lambda L, A, **k: page_article(p, L, A, **k))(p), 'thinking/', [art])
    yield ('contact/', 'Contact | Freedom Works', 'Talk to Freedom Works, a global creative agency. Tell us about your brief and we\u2019ll handpick the right team, from strategy to production.', page_contact, 'contact/', [])
    yield ('privacy/', 'Privacy policy | Freedom Works', 'How Freedom Works collects and uses your personal data, and your rights under data protection law.', page_privacy, '', [])
    yield ('cookies/', 'Cookie policy | Freedom Works', 'Which cookies the Freedom Works website uses, and how to change your cookie choices.', page_cookies, '', [])
    yield ('diversity-inclusion/', 'Diversity and inclusion | Freedom Works', 'The Freedom Works statement on diversity and inclusion: inclusivity is a reflex, not an initiative, and diversity is a catalyst for creativity and innovation.', page_dni, '', [])
    yield ('modern-slavery-statement/', 'Modern slavery statement | Freedom Works', 'The Freedom Works modern slavery statement, made under section 54 of the Modern Slavery Act 2015: our business, supply chain, risk assessment, and review.', page_msa, '', [])
    yield ('terms/', 'Terms of use | Freedom Works', 'The terms and conditions that apply to your use of the Freedom Works website.', page_terms, '', [])

def schema_tags(path, title, extra):
    out = [ORG] + ([crumbs(path, title.split(' | ')[0])] if path else []) + extra
    return '\n'.join(f'<script type="application/ld+json">{json.dumps(o, ensure_ascii=False)}</script>' for o in out)

PILL_IMG = {'agency/': 'agency', 'the-guild/': 'guild', 'services/': 'services', 'culture3/': 'culture', 'work/': 'work', 'thinking/': 'home'}
def add_pill(body, path, A):
    img = PILL_IMG.get(path)
    if not img: return body
    pill = f'<span class="pill" aria-hidden="true"><video autoplay muted loop playsinline src="{A("film/pill-"+img+".mp4")}"></video></span>'
    def f(mo):
        inner = mo.group(1)
        if ' ' in inner.split('<')[0]:
            first, rest = inner.split(' ', 1); return f'<h1>{first} {pill} {rest}</h1>'
        return f'<h1>{inner} {pill}</h1>'
    return re.sub(r'<h1>(.*?)</h1>', f, body, count=1, flags=re.S)

HTACCESS = """# Freedom Works: settings for Apache / cPanel hosting
Options -Indexes
DirectoryIndex index.html
ErrorDocument 404 /404.html

<IfModule mod_rewrite.c>
RewriteEngine On
# Always use HTTPS
RewriteCond %{HTTPS} !=on
RewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
# www.freedom.works -> freedom.works
RewriteCond %{HTTP_HOST} ^www\\.freedom\\.works$ [NC]
RewriteRule ^ https://freedom.works%{REQUEST_URI} [L,R=301]
# Old and alternative addresses
RewriteRule ^culture/?$ /culture3/ [L,R=301]
RewriteRule ^guild/?$ /the-guild/ [L,R=301]
RewriteRule ^approach/?$ /services/ [L,R=301]
RewriteRule ^voices-and-partners/?$ /culture3/ [L,R=301]
RewriteRule ^about/?$ /agency/ [L,R=301]
</IfModule>

<IfModule mod_mime.c>
AddType font/woff2 .woff2
AddType image/webp .webp
AddType video/mp4 .mp4
AddType image/svg+xml .svg
</IfModule>

<IfModule mod_deflate.c>
AddOutputFilterByType DEFLATE text/html text/css application/javascript application/json image/svg+xml text/plain application/xml
</IfModule>

<IfModule mod_expires.c>
ExpiresActive On
ExpiresByType text/html "access plus 0 seconds"
ExpiresByType text/css "access plus 1 hour"
ExpiresByType application/javascript "access plus 1 hour"
ExpiresByType image/webp "access plus 1 month"
ExpiresByType image/jpeg "access plus 1 month"
ExpiresByType image/png "access plus 1 month"
ExpiresByType image/svg+xml "access plus 1 month"
ExpiresByType video/mp4 "access plus 1 month"
ExpiresByType font/woff2 "access plus 1 year"
</IfModule>

<IfModule mod_headers.c>
Header set X-Content-Type-Options "nosniff"
Header set Referrer-Policy "strict-origin-when-cross-origin"
Header set X-Frame-Options "SAMEORIGIN"
</IfModule>
"""

NETLIFY_REDIRECTS = """/culture              /culture3/   301
/guild                /the-guild/  301
/approach             /services/   301
/voices-and-partners  /culture3/   301
/about                /agency/     301
/services/creative/creator-and-influencer/  /services/creative/  301
/services/creative/creator-and-influencer   /services/creative/  301
# The old Liberty Guild site was a single page: send everything on its domain to the new homepage.
# These only take effect once the old domain is added to this Netlify site as a domain alias.
# Old Liberty Guild policy pages go to their new equivalents
https://thelibertyguild.com/legal                 https://freedom.works/privacy/?utm_source=thelibertyguild.com&utm_medium=redirect&utm_campaign=rebrand  301!
https://thelibertyguild.com/slavery-act           https://freedom.works/modern-slavery-statement/?utm_source=thelibertyguild.com&utm_medium=redirect&utm_campaign=rebrand  301!
https://thelibertyguild.com/diversity-inclusion   https://freedom.works/diversity-inclusion/?utm_source=thelibertyguild.com&utm_medium=redirect&utm_campaign=rebrand  301!
https://www.thelibertyguild.com/legal                 https://freedom.works/privacy/?utm_source=thelibertyguild.com&utm_medium=redirect&utm_campaign=rebrand  301!
https://www.thelibertyguild.com/slavery-act           https://freedom.works/modern-slavery-statement/?utm_source=thelibertyguild.com&utm_medium=redirect&utm_campaign=rebrand  301!
https://www.thelibertyguild.com/diversity-inclusion   https://freedom.works/diversity-inclusion/?utm_source=thelibertyguild.com&utm_medium=redirect&utm_campaign=rebrand  301!
http://thelibertyguild.com/legal                 https://freedom.works/privacy/?utm_source=thelibertyguild.com&utm_medium=redirect&utm_campaign=rebrand  301!
http://thelibertyguild.com/slavery-act           https://freedom.works/modern-slavery-statement/?utm_source=thelibertyguild.com&utm_medium=redirect&utm_campaign=rebrand  301!
http://thelibertyguild.com/diversity-inclusion   https://freedom.works/diversity-inclusion/?utm_source=thelibertyguild.com&utm_medium=redirect&utm_campaign=rebrand  301!
http://www.thelibertyguild.com/legal                 https://freedom.works/privacy/?utm_source=thelibertyguild.com&utm_medium=redirect&utm_campaign=rebrand  301!
http://www.thelibertyguild.com/slavery-act           https://freedom.works/modern-slavery-statement/?utm_source=thelibertyguild.com&utm_medium=redirect&utm_campaign=rebrand  301!
http://www.thelibertyguild.com/diversity-inclusion   https://freedom.works/diversity-inclusion/?utm_source=thelibertyguild.com&utm_medium=redirect&utm_campaign=rebrand  301!
https://thelibertyguild.com/*      https://freedom.works/?utm_source=thelibertyguild.com&utm_medium=redirect&utm_campaign=rebrand  301!
https://www.thelibertyguild.com/*  https://freedom.works/?utm_source=thelibertyguild.com&utm_medium=redirect&utm_campaign=rebrand  301!
http://thelibertyguild.com/*       https://freedom.works/?utm_source=thelibertyguild.com&utm_medium=redirect&utm_campaign=rebrand  301!
http://www.thelibertyguild.com/*   https://freedom.works/?utm_source=thelibertyguild.com&utm_medium=redirect&utm_campaign=rebrand  301!
"""
if not CASE_PAGES:
    NETLIFY_REDIRECTS += ''.join(f"/work/{p['slug']}/  /work/  302\n" for p in PROJECTS)

_IMG_W = {}
def optimise_images():
    """Lighter images (SEO review, tab 2): 800px copies of the case-study stills for tiles, and WebP versions of the logos and awards."""
    from PIL import Image
    base = os.path.join(OUT, 'assets')
    def stale(src, dst): return not os.path.exists(dst) or os.path.getmtime(dst) < os.path.getmtime(src)
    media = os.path.join(base, 'media')
    for f in os.listdir(media):
        if f.startswith('poster-') and f.endswith('.webp') and not f.endswith('-800.webp'):
            src = os.path.join(media, f); dst = src[:-5] + '-800.webp'
            try:
                im = Image.open(src); _IMG_W[f[:-5]] = im.width
                if im.width > 820 and stale(src, dst):
                    im.convert('RGB').resize((800, round(im.height * 800 / im.width)), Image.LANCZOS).save(dst, 'WEBP', quality=78, method=6)
            except Exception: pass
    for folder, pat in ((os.path.join(base, 'logos', 'wall'), r'.+\.png$'), (os.path.join(base, 'brand'), r'award-.+\.png$'), (os.path.join(base, 'logos'), r'clients-.+\.png$')):
        if not os.path.isdir(folder): continue
        for f in os.listdir(folder):
            if not re.match(pat, f): continue
            src = os.path.join(folder, f); dst = src[:-4] + '.webp'
            if stale(src, dst):
                try: Image.open(src).save(dst, 'WEBP', quality=88, method=6)
                except Exception: pass

def webpify(doc):
    """Point pages at the WebP logos and awards wherever a WebP copy exists."""
    def sub(m):
        rel = m.group(2) + '.webp'
        return m.group(1) + rel if os.path.exists(os.path.join(OUT, 'assets', rel)) else m.group(0)
    return re.sub(r'(assets/)((?:logos/wall/[\w.-]+|brand/award-[\w-]+|logos/clients-[\w-]+))\.png', sub, doc)

def llms_txt():
    """llms.txt: a plain map of the site for AI assistants (agreed for all Tomorrow Group sites)."""
    from service_pages import SERVICE_PAGES
    U = lambda path: DOMAIN + '/' + path
    out = ['# Freedom Works', '',
           '> Freedom Works is a global creative agency offering brand strategy, brand identity, creative, production, and in-house creative. '
           'It brings together The Guild, a network of more than 600 award winning independent creatives, strategists, and producers across 37 countries and cultures, '
           'and Culture3, its cultural partnerships business, to build a handpicked team for every brief. Founded by Jon Williams. London.', '',
           '## About', f'- [About Freedom Works]({U("agency/")}): the model, our DNA, and the leadership team',
           f'- [The Guild]({U("the-guild/")}): 600+ independent creatives, strategists, and producers in 37 countries and cultures',
           f'- [Culture3]({U("culture3/")}): cultural partnerships, Offstage, A Culture3 Conversation, and TED partnerships',
           f'- [Contact]({U("contact/")}): hello@freedom.works', '', '## Services', f'- [All services]({U("services/")})']
    for sp in SERVICE_PAGES:
        out.append(f'- [{sp["name"]}]({U(sp["path"])}): {sp.get("line") or sp.get("intro", "")[:140]}')
    out += ['', '## Work', f'- [All work]({U("work/")})']
    for q in PROJECTS:
        res = (HOME_TILE_COPY.get(q['slug'], {}) or {}).get('result') if isinstance(HOME_TILE_COPY.get(q['slug']), dict) else None
        out.append(f'- [{q["client"]}: {q["camp"]}]({U("work/" + q["slug"] + "/")})' + (f': {res}' if res else ''))
    out += ['', '## Thinking', f'- [All articles]({U("thinking/")}): {len(POSTS)} articles']
    for t in TOPIC_SLUG:
        if any(x['tag'] == t for x in POSTS): out.append(f'- [{TAGS[t]}]({U("thinking/" + TOPIC_SLUG[t] + "/")}): {TOPIC_INTRO[t]}')
    out += ['', '## Optional', f'- [Sitemap]({DOMAIN}/sitemap.xml)', f'- [Privacy policy]({U("privacy/")})', '']
    return '\n'.join(out)

def build_site():
    optimise_images()
    os.makedirs(OUT, exist_ok=True)
    sync_thinking_images()
    for name in os.listdir(OUT):
        if name == 'assets': continue
        pth = os.path.join(OUT, name)
        shutil.rmtree(pth) if os.path.isdir(pth) else os.remove(pth)
    open(os.path.join(OUT, 'assets', 'site.css'), 'w').write(CSS.replace('url(../fonts/', 'url(fonts/'))
    urls = []
    LASTMOD.clear()
    for path, title, desc, fn, active, extra in list(pages()) + [('404', 'Page not found | Freedom Works', 'This page does not exist.', page_404, '', [])]:
        depth = 0 if path in ('', '404') else path.strip('/').count('/') + 1
        R = '../' * depth
        L = lambda p, R=R: (R + p) if (R + p) else './'
        A = lambda rel, R=R: (VIDEO_CDN + '/assets/' + rel) if (VIDEO_CDN and rel.endswith('.mp4')) else (R + 'assets/' + rel)
        body = add_pill(fn(L, A), path, A)
        if HIDE_PENDING and path == 'agency/': body = tidy_pending(body)
        body = presplit_headings(body)
        if VIDEO_CDN: body = re.sub(r'''(?<=["'(])(?:\.\./)*assets/((?:film|media)/[\w.-]+\.mp4)''', lambda m: VIDEO_CDN + '/assets/' + m.group(1), body)
        canon = DOMAIN + '/' + (path if path != '404' else '')
        _slug = path.strip('/').split('/')[-1] if path.startswith('thinking/') and path.count('/') == 2 else None
        if len(title) > 60 and title.endswith(' | Freedom Works'): title = title[:-len(' | Freedom Works')]   # Google shows the site name anyway
        seo_title = short_title(title)
        if len(seo_title) < 30 and not seo_title.endswith('| Freedom Works') and len(seo_title + ' | Freedom Works') <= 60: seo_title += ' | Freedom Works'
        _proj = next((q for q in PROJECTS if path == f"work/{q['slug']}/"), None)
        _src = local_img(_slug) if _slug and local_img(_slug) else (('media/' + _proj['img'] + '.webp') if _proj and _proj.get('img') else None)
        _share = share_jpg(_src)
        og_img = DOMAIN + '/assets/' + _share if _share else ''      # only the page's own picture (case-study still, article cover); otherwise no image
        og_h = '630'
        og_title = share_title(path, title)
        og_type = 'article' if _slug else 'website'
        for _e in extra:
            if _e.get('@type') == 'Article':
                _e.update(image=og_img, dateModified=_e.get('datePublished'), mainEntityOfPage={'@type': 'WebPage', '@id': canon},
                          publisher={'@type': 'Organization', 'name': 'Freedom Works', 'logo': {'@type': 'ImageObject', 'url': DOMAIN + '/assets/brand/logo-indigo.png'}})
            elif _e.get('@type') == 'CreativeWork':
                _e.update(image=og_img, url=canon)
        if _slug: body = re.sub(r'<img(?![^>]*\bloading=)', '<img loading="lazy" decoding="async"', body)
        LASTMOD[canon] = (next((q['date'][:10] for q in POSTS if q['slug'] == _slug), None) if _slug else None) or datetime.date.today().isoformat()
        robots = '<meta name="robots" content="noindex">\n' if (path == '404' or STAGING) else ''
        doc = f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<script>document.documentElement.classList.add('js','fp');setTimeout(function(){{document.documentElement.classList.remove('fp');if(!window.__fwReady)document.querySelectorAll('.rw').forEach(function(h){{h.classList.add('in')}})}},3500)</script>
{analytics_head()}<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{robots}<title>{esc(seo_title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canon}">
<meta property="og:title" content="{esc(og_title)}">
<meta property="og:description" content="{esc(desc)}">
{(f'<meta property="og:image" content="{og_img}">' + chr(10) + f'<meta property="og:image:width" content="1200">' + chr(10) + f'<meta property="og:image:height" content="{og_h}">' + chr(10) + f'<meta property="og:image:alt" content="{esc(og_title)}">') if og_img else ''}
<meta property="og:url" content="{canon}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Freedom Works">
<meta property="og:locale" content="en_GB">
<meta name="twitter:card" content="{"summary_large_image" if og_img else "summary"}">
<meta name="twitter:title" content="{esc(og_title)}">
<meta name="twitter:description" content="{esc(desc)}">
{f'<meta name="twitter:image" content="{og_img}">' if og_img else ''}
<link rel="icon" href="{A('favicon.png')}">
<link rel="apple-touch-icon" href="{A('apple-touch-icon.png')}">
<meta name="theme-color" content="#20243A">
<link rel="preload" href="{A('fonts/castel-500.woff2')}" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{A('fonts/castel-900i.woff2')}" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{A('site.css')}">
{schema_tags(path if path != '404' else '', title, extra)}
</head>
<body{' class="light-page"' if path else ''}>
{analytics_body()}{header(L, A, active, 'dark' if path in DARK_TOP else 'light')}
<main id="main">
{body}
</main>
{footer(L, A)}
{SCRIPT}
</body>
</html>'''
        doc = webpify(doc)
        if path == '404':
            open(os.path.join(OUT, '404.html'), 'w').write(doc); continue
        d = os.path.join(OUT, path); os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'index.html'), 'w').write(doc)
        urls.append(canon)
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>{u}</loc><lastmod>{LASTMOD.get(u, datetime.date.today().isoformat())}</lastmod></url>\n' for u in urls) + '</urlset>\n'
    open(os.path.join(OUT, 'sitemap.xml'), 'w').write(sm)
    open(os.path.join(OUT, '.htaccess'), 'w').write(HTACCESS)
    open(os.path.join(OUT, '_redirects'), 'w').write(NETLIFY_REDIRECTS)
    if STAGING: open(os.path.join(OUT, 'robots.txt'), 'w').write('# Review copy: keep search engines out\nUser-agent: *\nDisallow: /\n')
    else: open(os.path.join(OUT, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n')
    open(os.path.join(OUT, 'llms.txt'), 'w').write(llms_txt())
    return urls

# ---------------- single-file preview ----------------
def dedupe_data_uris(doc):
    """Preview only: store each embedded image once and point every use at it, so the single-file preview stays small."""
    keys = {}
    def key(u):
        if u not in keys: keys[u] = 'k%d' % len(keys)
        return keys[u]
    URI = r'data:[a-z]+/[a-z0-9.+-]+;base64,[A-Za-z0-9+/=]+'
    doc = re.sub(r'\bsrcset="([^"]*data:[^"]*)"', lambda m: 'data-pvset="' + re.sub(URI, lambda u: '{' + key(u.group(0)) + '}', m.group(1)) + '"', doc)
    doc = re.sub(r'\bdata-src="(' + URI + ')"', lambda m: 'data-pvd="' + key(m.group(1)) + '"', doc)
    doc = re.sub(r'\bdata-loop="(' + URI + ')"', lambda m: 'data-pvl="' + key(m.group(1)) + '"', doc)
    doc = re.sub(r'(?<![\w-])poster="(' + URI + ')"', lambda m: 'data-pvp="' + key(m.group(1)) + '"', doc)
    doc = re.sub(r'(?<![\w-])src="(' + URI + ')"', lambda m: 'data-pv="' + key(m.group(1)) + '"', doc)
    if not keys: return doc
    table = json.dumps({k: u for u, k in keys.items()}, separators=(',', ':'))
    js = ('<script>(function(){var P=' + table + ';'
          'document.querySelectorAll("[data-pv]").forEach(function(e){e.setAttribute("src",P[e.getAttribute("data-pv")]);});'
          'document.querySelectorAll("[data-pvp]").forEach(function(e){e.setAttribute("poster",P[e.getAttribute("data-pvp")]);});'
          'document.querySelectorAll("[data-pvset]").forEach(function(e){e.setAttribute("srcset",e.getAttribute("data-pvset").replace(/\\{(k\\d+)\\}/g,function(_,k){return P[k];}));});'
          'document.querySelectorAll("[data-pvd]").forEach(function(e){e.setAttribute("data-src",P[e.getAttribute("data-pvd")]);});'
          'document.querySelectorAll("[data-pvl]").forEach(function(e){e.setAttribute("data-loop",P[e.getAttribute("data-pvl")]);});'
          'document.querySelectorAll("video").forEach(function(v){if(v.querySelector("source[data-pv]"))v.load();});})();</script>')
    i = doc.find('<script', doc.find('<body'))
    return doc[:i] + js + doc[i:] if i > 0 else doc.replace('</body>', js + '</body>')

def build_preview(outfile, only=None, external=''):
    sync_thinking_images()
    PREVIEW_MODE[0] = True
    if only: DRAFTS[0] = True
    BLOBS = {'media/hero-web-1080.mp4': '/_blob/236cf964b36609499310f1b6f9c02187', 'media/hero-web-720.mp4': '/_blob/236cf964b36609499310f1b6f9c02187', 'film/loop-brompton.mp4': '/_blob/fb70b76b545e261752f1007b224a0914', 'film/loop-king-arthur.mp4': '/_blob/11e84b9dfd392c34df4f8b3147a360d3', 'film/loop-loveholidays.mp4': '/_blob/ac1fb7bc3428cecf55bc18d9cc9e8596', 'film/loop-ms-food.mp4': '/_blob/93309566a4d8f63db8a919b3d1458992', 'film/loop-rowse.mp4': '/_blob/5a03bc879616fac9846acb87fe98a31e', 'film/loop-wizz-air.mp4': '/_blob/1f51403c0de73ccf10b5ed55869d03f1', 'film/pill-agency.mp4': '/_blob/74058972cfd8865c67a4f89e9f932f00', 'film/pill-culture.mp4': '/_blob/d12b3caa145f76a6fb4e2a19ab09a925', 'film/pill-guild.mp4': '/_blob/f07b3083512f2227e577c4795467dcdb', 'film/pill-home.mp4': '/_blob/f45c7fb2d95de2ac00666ca81b2b8544', 'film/pill-services.mp4': '/_blob/d14e844937787a4596f58d55ecbe1419', 'film/pill-work.mp4': '/_blob/cb417937508046e10476efa86b1d2fad', 'film/sizzle-agency.mp4': '/_blob/2c922d0807b61703f91fb066ddec1d98', 'film/sizzle-culture.mp4': '/_blob/87a54696165b6b8eec18f96e0498d976', 'film/sizzle-guild.mp4': '/_blob/2f900cbdc062ccc3e0158b849feb2744', 'film/sizzle-services.mp4': '/_blob/0228e0f193eb87cac512554139ac10da', 'film/sizzle-work.mp4': '/_blob/dce94fc01016b3d6b5e60376216cbb53', 'film/sizzle-home.mp4': '/_blob/18036149359779457059a0361cec3ae8', 'film/loop-kitkat.mp4': '/_blob/3aed51c5c3115cb552326167924c704b', 'film/loop-tui.mp4': '/_blob/06f0c5fff0bcaa169fb85e218dea6611', 'film/loop-sma.mp4': '/_blob/7b602dba0e4702192183b810b3941f1a'}
    cache = dict(BLOBS)
    def data(rel):
        if rel not in cache:
            fp = os.path.join(SRC, 'assets', rel)
            ext = rel.rsplit('.', 1)[-1]
            mime = {'webp': 'image/webp', 'png': 'image/png', 'jpg': 'image/jpeg', 'mp4': 'video/mp4', 'woff2': 'font/woff2'}[ext]
            cache[rel] = f'data:{mime};base64,' + base64.b64encode(open(fp, 'rb').read()).decode()
        return cache[rel]
    def L(p):
        base = p.split('#')[0]
        if only and base not in only: return external + '#/' + p
        return '#/' + p
    A = lambda rel: ('asset:' + rel) if rel else 'asset:'
    routes = []
    for path, title, desc, fn, active, extra in pages():
        if only and path not in only: continue
        try: body = fn(L, A, strip_images=True)
        except TypeError: body = fn(L, A)
        body = add_pill(body, path, A)
        routes.append((path, title, body))
    sections = '\n'.join(f'<div class="route" data-route="{p}" data-title="{esc(t)}" hidden>\n{b}\n</div>' for p, t, b in routes)
    css = CSS
    for ph in PH:
        css = css.replace(f'url(media/{ph}.webp)', 'url(' + data('media/' + ph + '.webp') + ')')
    for mk in ['mark-red', 'mark-ink', 'mark-white']:
        css = css.replace(f'url({mk}.png)', 'url(' + data(mk + '.png') + ')')
    for f in ['castel-500', 'castel-900i', 'serif-400', 'serif-400i', 'cond-500', 'cond-600', 'hanken']:
        css = css.replace(f'url(../fonts/{f}.woff2)', f'url({data("fonts/" + f + ".woff2")})')
    for bi in ['icon-linen', 'icon-indigo', 'icon-peri', 'c3-icon-peri']:
        css = css.replace(f'url(brand/{bi}.png)', 'url(' + data('brand/' + bi + '.png') + ')')
    for f in []:
        css = css.replace(f'url(../fonts/{f}.woff2)', f'url({data("fonts/" + f + ".woff2")})')
    hdr = header(L, A, '')
    ftr = footer(L, A)
    doc = f'''<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"><meta name="robots" content="noindex"><title>Freedom Works</title><style>{css}</style></head><body>
{hdr}
<main>
{sections}
</main>
{ftr}
<script>window.__FW_PREVIEW=true;</script>
{SCRIPT}
<script>
(function(){{
  function show(){{
    var hp=location.hash.replace(/^#\\/?/,'').split('#'); var h=hp[0], anc=hp[1]||''; if(h && h.charAt(h.length-1)!=='/' && h.indexOf('/')===-1) h=h+'/';
    var rs=document.querySelectorAll('.route'), hit=null;
    rs.forEach(function(r){{ if(r.getAttribute('data-route')===h) hit=r; }});
    if(!hit) hit=document.querySelector('.route[data-route=""]')||document.querySelector('.route');
    rs.forEach(function(r){{ r.hidden=(r!==hit); }});
    document.title=hit.getAttribute('data-title'); var prg=document.querySelector('.progress'); if(prg) prg.style.display='none'; document.body.classList.toggle('light-page', hit.getAttribute('data-route')!=='');
    document.querySelectorAll('.site-head nav a').forEach(function(a){{ var t=a.getAttribute('href').replace('#/',''); if(t && h.indexOf(t)===0) a.setAttribute('aria-current','page'); else a.removeAttribute('aria-current'); }});
    rs.forEach(function(r){{ if(r!==hit) r.querySelectorAll('video').forEach(function(x){{ x.pause(); }}); }}); hit.querySelectorAll('video[autoplay]').forEach(function(x){{ x.muted=true; var pr=x.play(); if(pr) pr.catch(function(){{}}); }});
    var tgt=anc?hit.querySelector('#'+anc):null; if(tgt){{ setTimeout(function(){{ tgt.scrollIntoView(); }},60); }} else {{ window.scrollTo(0,0); }} if(hit.animate && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) hit.animate([{{opacity:0}},{{opacity:1}}],{{duration:280,easing:'ease'}});
  }}
  window.addEventListener('hashchange',show); show();
}})();
</script>
</body></html>'''
    # replace asset tokens
    doc = re.sub(r'asset:([A-Za-z0-9_./-]+\.(?:webp|png|jpg|mp4))', lambda m: data(m.group(1)), doc)
    doc = re.sub(r'\s*<source src="data:video/mp4;base64,[^"]*" media="\(max-width: 767px\)" type="video/mp4">', '', doc)
    doc = dedupe_data_uris(doc)
    open(outfile, 'w').write(doc)
    return os.path.getsize(outfile)

if __name__ == '__main__':
    urls = build_site()
    print('Built', len(urls), 'pages into site/')
