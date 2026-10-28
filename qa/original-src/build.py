import os, re, json, html, base64, shutil, datetime
ROOT = os.path.dirname(os.path.abspath(__file__))
def SP(*a): return os.path.join(ROOT, 'src', *a)
import markdown

SRC = os.path.join(ROOT, 'site')                    # existing home build + assets
OUT = os.path.join(ROOT, 'site')
THINK = SP('thinking')
PREVIEW_MODE = [False]
DOMAIN = 'https://freedom.works'

CSS = open(SP('base.css')).read() + open(SP('extra.css')).read() + open(SP('flourish.css')).read() + '\n.site-head{mix-blend-mode:normal;transition:background-color .3s ease}\n.site-head.solid{background:#000}\n'
CSS = CSS + open(SP('rebrand.css')).read()
HOME_MAIN = open(SP('home-main.html')).read()

NAV = [('work/', 'Work'), ('agency/', 'About'), ('services/', 'Services'), ('the-guild/', 'The Guild'),
       ('culture3/', 'Culture3'), ('thinking/', 'Thinking'), ('contact/', 'Talk to us')]
TAGS = {'ai-and-creativity': 'AI and creativity', 'on-the-model': 'On the model', 'talent-and-work': 'Talent and work',
        'culture-and-ads': 'Culture and advertising', 'purpose': 'Purpose'}

def esc(t): return html.escape(t, quote=True)
def month(d):
    dt = datetime.date.fromisoformat(d); return dt.strftime('%B %Y')

# ---------------- data ----------------
PROJECTS = [
    dict(slug='king-arthur-baking', img='poster-king-arthur', loop='king-arthur', client='King Arthur Baking', camp='Keep Rising', vimeo=('1156877036', ''),
         short='A brand platform that takes King Arthur out of a low-interest category.', res='From #3 to #1 flour brand in the US. Doubled sales.', stat='+100%',
         copy='Our Keep Rising platform helped King Arthur become the #1 flour brand in the US, driving a 100% sales uplift and adding 3.4m households. A leading FMCG example of emotional storytelling driving commercial growth.',
         n='+100%', l='Sales uplift', extra=['#1 flour brand in the US', '+3.2pt share gain', '+3.4m new households'],
         quote=("Keep Rising has been transformative for King Arthur Baking. Not just creatively, but commercially. In a low-interest category, The Guild helped us connect on a deeper emotional level. They captured our brand\u2019s purpose with humanity and craft, and the results speak for themselves: record market share, millions of new households, and the highest repeat rate in the category.", 'Kim Stellavato', 'Brand Director, King Arthur Baking'), home=True),
    dict(slug='wizz-air', img='poster-wizz-air', loop='wizz-air', client='Wizz Air', camp='Locos for Low-Cost', vimeo=('1156877642', ''),
         short="The airline's first fully AI-powered campaign, a human idea scaled by AI.", res='+11.4% demand, year on year', stat='+11.4%',
         copy="Wizz Air\u2019s first fully AI-powered campaign, created through our partnership with Monks, delivered 17 broadcast-ready assets in three weeks. A human idea scaled by AI. A new model for airlines needing fast, high-impact campaigns.",
         n='+11.4%', l='Increase in demand, year on year', extra=['17 TV, OOH and social assets', 'Delivered in three weeks'],
         quote=("Locos is about letting go, embracing spontaneity, and leaning into life\u2019s fun side. Because low-cost isn\u2019t only about saving money, it\u2019s about having the freedom to do more and live bigger. Wizz Air has, from its inception, been a digital-first company, so it makes sense that we would be at the leading edge of using new technology in all areas of our business. So making an all AI ad just makes sense.", 'Silvia Mosquera Gonz\u00e1lez', 'Commercial Officer Central, Wizz Air'), home=True),
    dict(slug='ms-food', img='poster-ms-food', loop='ms-food', client='M&S Food', camp='Magic Really Does Sell', vimeo=('1156877368', ''),
         short='A Christmas idea big enough to reunite Dawn French and Jennifer Saunders.', res='+10.2% sales', stat='+10.2%',
         copy="Working with M&S Food\u2019s in-house team, we created the idea to reunite Dawn French and Jennifer Saunders, delivering a Christmas campaign that lifted sales by 10.2%. Cultural storytelling turning into real retail impact.",
         n='+10.2%', l='Sales', extra=[],
         quote=("M&S outperformed the market in food in both volume and value for the second year running. The retailer\u2019s high-end food offer traditionally appeals to shoppers at Christmas, and 2022 was no exception despite increasing economic pressure on consumers.", 'Stuart Machin', 'Chief Executive, M&S'), home=True),
    dict(slug='loveholidays', img='poster-loveholidays', loop='loveholidays', client='loveholidays', camp='At Your Fingertips', vimeo=('1156877210', ''),
         short='From performance to brand, without losing demand.', res='+72% consideration, \u201342% cost per click, + a million people to their ATOL licence.', stat='+72%',
         copy='We helped loveholidays shift from performance to brand, lifting awareness +15pts and consideration +72%, driving demand that required 1m extra ATOL licences. Proof that brand and performance work better together in travel.',
         n='+72%', l='Consideration', extra=['\u201342% cost per click', '+15pts awareness', '1m extra ATOL licences'],
         quote=("Since starting our brand journey with The Liberty Guild, we\u2019ve added nearly 15%pts of awareness and seen every brand metric we track increase at pace, while our competitors are flat or falling, all despite dramatically lower brand budgets.", 'Al Murray', 'CMO, loveholidays'), home=True),
    dict(slug='rowse-honey', img='poster-rowse', loop='rowse', client='Rowse Honey', camp='The Squeeze That Protects the Bees', vimeo=('1156877553', ''),
         short='Repositioned as the purpose-led choice, with bee welfare at its heart.', res='+24% new customers', stat='+24%',
         copy='We repositioned Rowse Honey as a purpose-led choice, putting bee welfare at the heart of the brand. The work attracted +24% more new customers and delivered a 98th percentile brand power score. Proving that doing good can drive both growth and equity.',
         n='+24%', l='New customers', extra=['98th percentile brand power'], quote=None, home=True),
    dict(slug='brompton', img='poster-brompton', loop='brompton', client='Brompton', camp='Life Unfolded', vimeo=('1156876773', ''),
         short="Fifty years of Brompton, marked by launching forward rather than looking back.", res='50th anniversary film', stat='50',
         copy="There\u2019s a confidence that comes from knowing who you are. The film we created for Brompton\u2019s 50th anniversary leans into that. Life Unfolded doesn\u2019t look back, it launches the brand forward.",
         n='50', l='Years of Brompton, launched forward', extra=[],
         quote=("We were looking for a partner who truly understood the spirit of Brompton, not just as a mode of transport, but as a way of moving through life with freedom, creativity, and purpose. The Liberty Guild\u2019s fresh, unique global model and deep cultural insight made them the perfect fit to help us inspire a new wave of riders around the world.", 'Chris Willingham', 'Global CMO, Brompton'), home=True),
    dict(slug='snowfox-group', img=None, client='Snowfox Group', camp='One Platform to Grow', vimeo=None,
         short='Four sushi brands unified under one strategic platform.', res='$621m acquisition by Zensho', stat='$621m',
         copy='We unified four Snowfox sushi brands under one strategic platform, strengthening identity and commercial performance, contributing to a $621m acquisition by Zensho. A retail food example of brand architecture driving enterprise value.',
         n='$621m', l='Acquisition by Zensho', extra=['Four sushi brands, one platform'], quote=None, home=False),
    dict(slug='kitkat-f1', img='poster-kitkat', loop='kitkat', client='KitKat', camp='F1 Ident', vimeo=('1156877162', ''),
         short='', res='Watch the film', stat='', copy='', n='', l='', extra=[], quote=None, home=False),
    dict(slug='nestle-sma', img='poster-sma', loop='sma', client='Nestl\u00e9 SMA', camp='Go With Your Gut', vimeo=('1203806335', '054f9189f0'),
         short='Building trust long before parents choose formula.', res='2x Baby Club sign-ups', stat='2x',
         copy="Working with Nestl\u00e9\u2019s Content Studio, we helped SMA\u00ae shift the conversation from infant formula to genuine support, creating a campaign that brought its unique Baby Club services to life and positioned the brand as a trusted companion from pregnancy through to baby\u2019s first months.",
         n='2x', l='Baby Club sign-ups', extra=[],
         sections=[
          ('The brief', 'Build trust long before parents choose formula.', ["Around 70% of parents don\u2019t expect to formula feed when they first become pregnant. But almost all are looking for trusted advice, reassurance and expert guidance as they prepare for life with a new baby.", "SMA\u00ae already offered something genuinely different: a Baby Club providing access to qualified midwives, a 24/7 Careline, educational content and expert guidance throughout the parenting journey.", "Our challenge wasn\u2019t creating another baby club. It was showing parents that SMA\u00ae is there whenever they need someone to turn to."], None),
          ('The idea', 'Go With Your Gut.', ["Becoming a parent doesn\u2019t just bring questions. It brings a constant stream of opinions, from family, friends, social media, Google and experts. Everyone seems to have the right answer. But parents aren\u2019t looking for perfect answers. They\u2019re looking for someone they can trust.", "So the most valuable thing SMA\u00ae could give them wasn\u2019t more advice. It was the confidence to trust themselves. \u2018Go With Your Gut\u2019 encourages parents to trust their own instincts, knowing expert support is always there whenever they need reassurance.", "Rather than positioning SMA\u00ae Baby Club as another voice telling parents what to do, we positioned it as the trusted companion that helps parents feel confident in the decisions that are right for their family."], None),
          ('The execution', 'Real parents. Real moments.', ["Authenticity sat at the heart of the campaign. Rather than scripted performances, we worked with real parents whose experiences reflected the realities of early parenthood.", "The creative was designed to feel creator-led, intimate and relatable, capturing the emotional highs and lows that every parent experiences. This allowed SMA\u00ae to show up not as an advertiser, but as a trusted source of reassurance."], None),
          ('The Baby Club', 'Support that goes beyond nutrition.', ["The Baby Club brings together expert support designed around the questions parents ask every day.", "Each service demonstrates the same belief: parents don\u2019t need all the answers. They just need to know someone is there to help."], ['Midwife Live Chat', '24/7 Careline', 'Baby gut health education', 'Parenting podcast series']),
         ],
         gallery=['sma-1', 'sma-2', 'sma-3', 'sma-4'],
         quote=("I really couldn\u2019t have hoped for better. We can all collectively take pride in the achievement. Not just the creative but the fact we\u2019re here. Infant nutrition is one of Nestl\u00e9\u2019s most protected categories and notoriously hard to navigate in creatively. And also throw in the biggest global crisis Nestl\u00e9 has had in well over a decade on the most sensitive of products, the reception is amazing. It\u2019s testament to The Guild\u2019s Amplify product, the process and the amazing talent you brought to the table. Thank you.", 'Tom Nixon', 'Head of Content Studios UK&I, Nestl\u00e9'), home=False),
    dict(slug='tui', img='poster-tui', loop='tui', client='TUI', camp='Skip To The Good Bit', vimeo=('1203813505', '5dd01fa66a'),
         short='', res='Watch the film', stat='', copy='', n='', l='', extra=[],
         quote=("The Liberty Guild have been a delight to work with. Their interpretation and understanding of our brief helped crystallise the strategic approach, which then went on to create some creative work that brought to life the proposition in a way that will allow us to flex across markets. In conjunction with DEPT we went on to create an ad using AI. Liberty Guild project managed the whole process, making it seem like a breeze for me!", 'Rachel Moss', 'Head of International Marketing, TUI Group'), home=False),
]

VOICES = [
    ("In a sea of sameness, The Liberty Guild is a breath of fresh air. A thoroughly modern, no-nonsense approach to applied strategic creative thinking.", 'Nick Tate', 'VP Head of Next, GSK Consumer Healthcare'),
    ("We were looking for a partner who truly understood the spirit of Brompton, not just as a mode of transport, but as a way of moving through life with freedom, creativity, and purpose.", 'Chris Willingham', 'Global CMO, Brompton'),
    ("What\u2019s great about their offering is the global reach of their network. The ability to tap into creatives and strategists from across the globe whilst still having the expert support of a centrally managed account team gives us the best of both worlds.", 'Gemma Schmid', 'Director of Brand Marketing, loveholidays'),
    ("The Liberty Guild do more than just brilliant ideas delivered with beautiful precision, it\u2019s the soap box to elevate the in-house voice at the very heart of our brands. Bringing the best of outside, inside.", 'Tom Nixon', 'Head of Content Studios UK&I, Nestl\u00e9'),
    ("Its sheer audacity and its willingness to rip up the rule book to create a creative business for our new world.", 'The Drum', 'Grand Prix jury, The Drum Awards 2021'),
    ("Liberty Guild is a breath of fresh air having worked in the industry for over 20 years now. The process and the set-up is really adapted to the way consumer communication has evolved: fluid, media agnostic, agile, and very consumer driven.", 'Estrella Lopez-Brea', 'Global Head of Insights, CPW'),
]


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

FAQ = [
    ("Who are Freedom Works?", "A global creative agency built on Calibre, Culture and Craft. More than 500 award-winning independent creatives and strategists across 37 countries, led by a founder and leadership team who have run businesses, boutique agencies, global networks, production companies and start-ups."),
    ("How do you work?", "We run a distributed creative department. No buildings. No fixed teams. For every brief we build a bespoke team from our network, supported by insight from qual, quant or behavioural science research, with workflow optimised through our tech stack. We use AI when it helps, and we don't when it doesn't. We can run everything end to end, or plug into your in-house team."),
    ("How are you different to a legacy agency?", "We don't sell hours. We sell ideas. Our work is productised: fixed scope, fixed cost, fixed time, clear outputs. We work in short sprints, with proper decision points and evidence built in, and when clients want more, a subscription model makes it cheaper and easier."),
    ("What makes your talent better?", "Every project starts by finding the right people for the brief. Not whoever's free. Not whoever's cheapest. Our creatives value the freedom to work on their own terms, on briefs they choose, and between them they've won 2,315 Lions, Pencils and Effies."),
]

# ---------------- page bodies ----------------
def hs_form(uid='hs-form'):
    return f'''<div class="hs-wrap" data-hs-portal="{HS_PORTAL}" data-hs-form="{HS_FORM}">
      <div class="hs-target" id="{uid}"></div>
      <p class="hs-fallback"><a class="ct-btn" href="{HS_SHARE}" target="_blank" rel="noopener">Start your enquiry <span aria-hidden="true">\u2192</span></a></p>
    </div>'''

def contact_cards(big=False):
    return f'''<div class="ct-cards{" big" if big else ""}">
      <div class="ct-card form-card">
        <p class="ct-kicker"><span class="mk ink" aria-hidden="true"></span>New business</p>
        <h3>How can we help?</h3>
        {hs_form()}
      </div>
      <div class="ct-card mail-card">
        <p class="ct-kicker"><span class="mk ink" aria-hidden="true"></span>Everything else</p>
        <a class="mail" href="mailto:hello@freedom.works">hello@freedom.works</a>
      </div>
    </div>'''

def cta(L):
    return f'''<section class="contact" aria-labelledby="ct">
  <div class="wrap">
    <h2 id="ct">Let's make <span class="thin">work that matters.</span></h2>
    {contact_cards()}
  </div>
</section>'''

def vim_attrs(p):
    if not p.get('vimeo'): return ''
    vid, h = p['vimeo']
    return f' data-vimeo="{vid}"' + (f' data-h="{h}"' if h else '')

def tile(p, L, A):
    stat = p['stat'] or 'Play'
    if p['img']:
        media = f'<img src="{A("media/"+p["img"]+".webp")}" alt="{esc(p["client"])}, {esc(p["camp"])}" loading="lazy">'
    else:
        big = p['stat'] or p['client']
        media = f'<div class="typo" aria-hidden="true"><span class="tn">{esc(big)}</span><span class="tc">{esc(p["client"])}</span></div>'
    brief = f'<p>{esc(p["short"])}</p>' if p['short'] else ''
    loop = f' data-loop="{A("film/loop-"+p["loop"]+".mp4")}"' if p.get('loop') else ''
    return f'<a class="tile" href="{L("work/"+p["slug"]+"/")}" data-stat="{esc(stat)}"{vim_attrs(p)}{loop}><div class="media">{media}</div><h3>{esc(p["client"])}: {esc(p["camp"])}</h3>{brief}<p class="res">{esc(p["res"])}</p></a>'

def first_img(p):
    m = re.search(r'!\[[^\]]*\]\((https://[^)\s]+)\)', p['body_md'])
    return m.group(1) if m else ''

PH = []
IMG_MANIFEST = SP('thinking-images.json')
IMGMAP = json.load(open(IMG_MANIFEST, encoding='utf-8')) if os.path.exists(IMG_MANIFEST) else {}
TAG_VARIANT = {t: i % 3 for i, t in enumerate(TAGS)}
def local_img(slug):
    e = IMGMAP.get(slug)
    if e and os.path.exists(os.path.join(OUT, 'assets', e['file'])): return e['file']
    return None
def post_cards(posts, L, A=None, with_data=False):
    out = []
    for i, p in enumerate(posts):
        tag = TAGS.get(p['tag'], 'Thinking')
        da = f' data-tag="{p["tag"]}"' if with_data else ''
        typo = f'<span class="tc-in"><span class="mk" aria-hidden="true"></span><span class="tt">{esc(tag)}</span></span>'
        v = i % 3
        loc = local_img(p['slug'])
        remote = '' if PREVIEW_MODE[0] else first_img(p)
        if loc and A:
            img = f'<span class="cimg tv-{v}"><img src="{A(loc)}" alt="" loading="lazy">{typo}</span>'
        elif remote:
            img = f'<span class="cimg tv-{v}"><img src="{esc(remote)}" alt="" loading="lazy" onerror="this.parentNode.classList.add(\'tcard\');this.remove()">{typo}</span>'
        else:
            img = f'<span class="cimg tcard tv-{v}">{typo}</span>'
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
     "When anyone can generate, the edge is knowing good from great. The Guild is the global creative and strategic A-list. 500+ of the best independent minds across 37 countries, with 2,315 Lions, Pencils and Effies between them. Taste and judgement. Insight and evidence. Handpicked for your brief, on your work from day one.",
     'Calibre gets you cut through.'),
    ('Culture', 'Make it resonate.', 'Freedom from cultural isolation.', 'p-red', 'still-culture', 'In the brave new world of AI, human connections are crucial.',
     'AI can talk about culture. It can never be in it. Culture3 gives brands access to the real conversations, communities and moments shaping culture.',
     "AI can talk about culture. It can never be in it. Culture3 gives brands the access and partnerships to take part in the real conversations, communities and moments shaping culture right now. Physical. Nuanced. Human. We find where a brand has the right to show up, who it should show up with, and what part it can play.",
     'Culture gets you noticed.'),
    ('Craft', 'Make it beautiful.', 'Freedom from slop.', 'p-black', 'still-craft', 'Experience, taste and judgement just got even more differentiating.',
     "Machines do the making. Humans decide what ships, from first brief to final cut, and they know when something isn't good enough.",
     "Agentic production removes the old constraints of time, cost and scale. It doesn't remove the need for someone to say \"not good enough\". Our creative crew have made that call at the very top of the industry, and they stay with the work from first brief to final cut. Machines do the making. Humans decide what ships.",
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
             "Freedom from slop and a sea of sameness.", "Freedom from office-bound monotony.", "Freedom from convention.", "Freedom. Works."]
    one = ''.join(f'<span class="it"><span class="mk" aria-hidden="true"></span>{esc(t)}</span>' for t in lines)
    dup = one.replace('<span class="it">', '<span class="it" aria-hidden="true">')
    return f'<section class="ticker words" aria-label="Why Freedom Works"><div class="track">{one}{dup}</div></section>'

def logos_band(A, dark=False):
    strip = 'clients-white' if dark else 'clients-dark'
    cls = ' dark' if dark else ''
    mk = '' if dark else ' ink'
    return f'''<section class="logos-band{cls}" aria-label="Clients">
  <p class="lbl wrap"><span class="mk{mk}" aria-hidden="true"></span>Brands we've made work for</p>
  <div class="marquee" aria-label="Clients include Heineken, Wizz Air, Diageo, Nestlé, TUI, P&amp;G, Coca-Cola, GSK, M&amp;S Food, Brompton and loveholidays">
    <img src="{A("logos/"+strip+".png")}" alt=""><img src="{A("logos/"+strip+".png")}" alt="" aria-hidden="true">
  </div>
</section>'''

def strip3(A, a, b, c):
    return f'<div class="strip3" aria-hidden="true"><div class="a px"><img src="{A("media/"+a+".webp")}" alt="" loading="lazy"></div><div class="b px"><img src="{A("media/"+b+".webp")}" alt="" loading="lazy"></div><div class="c px"><img src="{A("media/"+c+".webp")}" alt="" loading="lazy"></div></div>'

HS_PORTAL, HS_FORM, HS_SHARE = '25281165', '0aad04dc-5ab6-4146-b353-f73841abc855', 'https://share-eu1.hsforms.com/1Cq0E3Fq2QUazU_c4QavIVQf1v2l'

IMPACT = [
    ('+100%', 'Sales uplift', 'King Arthur Baking', 'Keep Rising took King Arthur to the #1 flour brand in the US and added 3.4m new households.', 'king-arthur-baking'),
    ('+10.2%', 'Sales', 'M&S Food', "The Christmas idea that reunited Dawn French and Jennifer Saunders, made with M&S Food\u2019s in-house team.", 'ms-food'),
    ('+11.4%', 'Demand, year on year', 'Wizz Air', "The airline\u2019s first fully AI-powered campaign: 17 broadcast-ready assets in three weeks.", 'wizz-air'),
    ('+72%', 'Consideration', 'loveholidays', 'From performance to brand: +15pts awareness and demand that needed 1m people added to their ATOL licence.', 'loveholidays'),
    ('$621m', 'Valuation at IPO', 'Snowfox Group', 'Our platform unified Snowfox Group\u2019s four sushi brands, strengthening identity and performance, and contributed to its $621m acquisition by Zensho.', 'snowfox-group'),
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
    cards = ''.join(f'''<a class="im-card" href="{L("work/"+slug+"/")}"><span class="n" data-count>{esc(n)}</span><span class="t">{esc(t)}<em>{esc(c)}</em></span><span class="d">{esc(d)}</span><span class="go">See the case study</span></a>''' for n, t, c, d, slug in IMPACT)
    logos_html = f'''  <div class="im-logos">
    <p class="lbl wrap"><span class="mk" aria-hidden="true"></span>Brands we\u2019ve made work for</p>
    <div class="marquee" aria-hidden="true"><img src="{A("logos/clients-white.png")}" alt=""><img src="{A("logos/clients-white.png")}" alt=""></div>
  </div>''' if logos else ''
    return f'''<section class="impact dark" aria-labelledby="im">
  <div class="wrap">
    <div class="im-head">
      <h2 class="sec-title" id="im">{heading}</h2>
      {'<p>Creative work should drive fame in the boardroom as well: sales, market share, demand and value.</p>' if intro else ''}
    </div>
    <div class="im-grid">
      <div class="im-card big"><span class="n" data-count>2,315</span><span class="t">Lions, Pencils and Effies<em>Won by the talent in The Guild</em></span><span class="d">Cannes Lions, D&amp;AD, Effies. B Corp certified.</span></div>
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
    m = HOME_MAIN.replace('src="assets/', 'src="' + A('')).replace('poster="assets/', 'poster="' + A(''))
    hero = re.search(r'<section class="hero".*?</section>', m, re.S).group(0)
    doors = re.search(r'<section class="doors wrap".*?</section>', m, re.S).group(0)
    doors = re.sub(r'href="/(work|agency|the-guild|services|culture3|thinking|contact)(/[^"]*)?"', lambda mo: f'href="{L(mo.group(1) + "/")}"', doors)
    for a, b in {'craft.webp': 'still-lunch.webp', 'calibre.webp': 'still-calibre.webp', 'brompton.webp': 'still-craft.webp', 'culture.webp': 'still-culture.webp'}.items():
        doors = doors.replace('media/' + a, 'media/' + b)
    doors = doors.replace("Platforms, campaigns, content, and teams on demand. Fixed scope, fixed cost, fixed time.", "Brand strategy, identity, creative, production and in-house augmentation.")
    doors = doors.replace('<span class="name">Agency</span>', '<span class="name">About</span>')

    doors = doors.replace('<section class="doors wrap" aria-label="Explore Freedom Works">', '<section class="doors wrap" aria-labelledby="ex"><p class="sec-lbl" id="ex"><span class="mk" aria-hidden="true"></span>Explore Freedom Works</p>')
    pill = f'<span class="pill" aria-hidden="true"><video autoplay muted loop playsinline poster="{A("media/hero-poster.jpg")}"><source src="{A("film/pill-home.mp4")}" type="video/mp4"></video></span>'
    statement = f'''<section class="statement wrap indigo" aria-labelledby="st">
  <p class="sec-lbl">Welcome to Freedom Works</p>
  <h2 class="fw-head fw-lockup" id="st"><img src="{A("brand/lockup-freedom-makes-better-work.png")}" alt="Freedom makes better work" width="3482" height="552"></h2>
  <div class="intro-grid">
    <p class="intro-lead">And better work shows up where it counts. On screen, in culture and on your P&amp;L.</p>
    <p class="intro-body">Creativity doesn\u2019t thrive in rigid systems or office-bound models. It thrives when people are trusted and supported to do their best thinking. That freedom attracts better talent. Better talent produces better ideas. And better ideas grow your brand. Simple.</p>
  </div>
</section>
<section class="pillars3 wrap white" aria-label="The Guild, Culture3 and leadership">
  <div class="intro-three">
    <div class="col"><h3><span class="mk" aria-hidden="true"></span>The Guild</h3><p>We have the best creative department in the world: The Guild. More than five hundred A-list creatives, strategists and producers, with over 2,300 Lions &amp; Pencils between them, handpicked for each brief.</p><a class="sec-link" href="{L("the-guild/")}">Meet The Guild</a></div>
    <div class="col"><h3><span class="mk" aria-hidden="true"></span>Culture3</h3><p>Culture3 connects brands to culture through strategic partnerships, human voices and moments that matter. We help brands understand where to show up, who to show up with and how to make their participation meaningful.</p><a class="sec-link" href="{L("culture3/")}">Explore Culture3</a></div>
    <div class="col"><h3><span class="mk" aria-hidden="true"></span>Leadership</h3><p>We\u2019re led by a founder and a leadership team who have excelled with ideas, organisations and talent at the very top of the industry. Their vision and judgement runs through every piece of work we make.</p><a class="sec-link" href="{L("agency/")}#leadership">Meet the leadership</a></div>
  </div>
</section>'''
    reel = f'<section class="reel" aria-hidden="true"><video class="lazyvid" muted loop playsinline preload="none" poster="{A("media/poster-brompton.webp")}" data-src="{A("film/sizzle-home.mp4")}"></video></section>'
    work = f'''<section class="work wrap light" id="work" aria-labelledby="wk">
  <div class="sec-head"><h2 class="sec-title" id="wk"><em>work</em> that matters</h2><a class="sec-link" href="{L("work/")}">All work</a></div>
  <div class="grid">
    {chr(10).join(tile(p, L, A) for p in PROJECTS if p['home'])}
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
    <div class="dh-end"><p>That\u2019s our DNA. Humanity at the core, with an agentic engine behind it.</p><a class="sec-link" href="{L("agency/")}#dna">Explore our DNA</a></div>
  </div>
</section>'''
    guild = mosaic(A, '<span>500+ minds.</span> <span>37 countries.</span> <span>One brief at a time.</span>', 'The Guild is the creative and strategic A-list. For every project we handpick the people who fit your brief, your brand and your culture.', L('the-guild/'), 'Meet The Guild')
    marquee = '<section class="big-marquee light" aria-hidden="true"><div class="track">' + ''.join('<span class="h">Freedom</span><span class="t">works</span><span class="mkb"></span>' for _ in range(5)) + '</div></section>'
    slides = ''.join(f'<figure class="slide{" on" if i == 0 else ""}"><blockquote>\u201c{esc(q)}\u201d</blockquote><figcaption class="who">{esc(n)}<span>{esc(t)}</span></figcaption></figure>' for i, (q, n, t) in enumerate(VOICES))
    voices = f'<section class="voice voices wrap dark" aria-label="What clients say" aria-roledescription="carousel"><p class="sec-lbl"><span class="mk" aria-hidden="true"></span>What clients say</p>{slides}<div class="ctrl"><button type="button" data-prev aria-label="Previous quote">\u2039</button><button type="button" data-next aria-label="Next quote">\u203a</button><span class="count">1 / {len(VOICES)}</span></div><p class="was">Freedom Works was formerly The Liberty Guild.</p></section>'
    thinking = f'''<section class="thinking wrap light" aria-labelledby="th">
  <div class="sec-head"><h2 class="sec-title" id="th"><em>Thinking</em></h2><a class="sec-link" href="{L("thinking/")}">All articles</a></div>
  {post_cards(POSTS[:3], L, A)}
</section>'''
    return '\n'.join([hero, ticker(A), statement, reel, work, impact, logo_wall(A), hint, guild, doors, marquee, voices, thinking, cta(L)])

def page_agency(L, A):
    return f'''<section class="page-hero wrap">
  <h1>Freedom makes <span class="thin">better</span> work.</h1>
  <div class="intro"><div class="stack">
    <p>Freedom Works is a global creative agency. We make work that matters. Work that's grounded in culture, crafted for impact, and guided by the best creative minds in the industry.</p>
    <p>We believe freedom makes better work. Not as fancy words. In practice. In real life. Creativity doesn't thrive in rigid systems or office-bound models. It thrives when people are trusted and supported to do their best thinking.</p>
  </div></div>
</section>
<div class="sizzle wrap"><video class="lazyvid" muted loop playsinline preload="none" poster="{A("media/still-lunch.webp")}" data-src="{A("film/sizzle-agency.mp4")}" aria-hidden="true"></video></div>
<section class="band wrap">
  <div class="split">
    <div class="l"><h2 class="h2">Built for the <span class="thin">next ten years</span></h2></div>
    <div class="r prose">
      <p class="lead-light">Nearly ten years ago we built the agency model that everyone talks about. But the world has moved on. And so must we.</p>
      <p>As we build out an agency fit for the next ten years, AI is embedded for process and production. But for ideas, we have designed a business with humanity at its core.</p>
      <p>With The Guild, we have the best creative department in the world: more than five hundred A-list creatives, strategists and producers, with over 2,300 Lions and Pencils between them, handpicked for each brief.</p>
      <p>Culture3 connects brands to cultural opportunities through strategic partnerships, relevant voices and moments that give them a credible role in the conversations that matter. We help brands understand where to show up, who to show up with and what to build to make their participation meaningful.</p>
      <p>We\u2019re led by a founder and an entrepreneurial leadership team who have excelled with ideas, organisations and talent at the very top of the industry. Our vision and judgement runs through every piece of work we make.</p>
    </div>
  </div>
</section>
{strip3(A, "still-pie", "poster-loveholidays", "still-honey")}
<section class="band wrap" id="dna" aria-labelledby="dna-h">
  <div class="split" style="margin-bottom:48px">
    <div class="l"><h2 class="h2" id="dna-h">Our DNA</h2></div>
    <div class="r"><p class="lead-light">In a world where machines can do almost anything, the things they can't do just became a whole lot more important. Where the work belongs. Who decides what's worth making. How well it's made. That's our DNA. Humanity at the core, with an agentic engine behind it.</p></div>
  </div>
</section>
{dna_panels(A, full=True)}
<section class="band wrap" id="leadership" aria-labelledby="ld">
  <div class="split" style="margin-bottom:48px">
    <div class="l"><h2 class="h2" id="ld">Taste. Judgement. <span class="thin">Experience.</span></h2></div>
    <div class="r"><p class="lead-light">Anyone can generate a hundred ideas now. Knowing a great idea from an average one is where the value lies. That call gets made by people who've made it at the very top of the industry, on the biggest brands in the world. And they don't hand it off after the presentation. They stay on it until it deploys.</p></div>
  </div>
  <div class="leaders">
    <article class="lead-row"><div class="ph">Portrait to come</div><div class="lr-txt"><h3>Jon Williams</h3><p class="role">Founder and Chief Creative Officer</p><ul class="pstats"><li><b data-count>47</b>Agencies led</li><li><b data-count>105</b>Cannes Lions</li><li><b data-count>109</b>Effies</li><li><b data-count>51</b>D&amp;AD Pencils</li></ul><div class="bio"><p>Jon Williams is Founder and Chief Creative Officer of Freedom Works.</p><p>At Publicis he created HYPE for HP, the platform Cannes used as its benchmark for the Titanium Lion, and \u201cChoices\u201d for the DePaul Trust, the world\u2019s first true interactive TV spot. He went on to make the Carling iPint, the world\u2019s first native branded iPhone app, downloaded six million times.</p><p>As Chief Creative Officer of Grey London, then Grey EMEA across 47 agencies, he built the network\u2019s best-performing creative region: 105 Cannes Lions, 109 Effies and 51 D&amp;AD Pencils, plus a 2,000-strong talent platform.</p><p>In 2017 he founded The Liberty Guild, which now powers Freedom Works.</p><p>As well as having chaired or sat on pretty much every award show there is, Jon sits on the Creative UK council and has judged the Luma AI Dream Brief and the Advertising Turing Test. Fuelling his conviction that as machines make more, human taste and judgement matter more than ever.</p></div></div></article>
    <article class="lead-row"><div class="ph">Portrait to come</div><div class="lr-txt"><h3>Aim\u00e9e Luther</h3><p class="role"><span class="pending-tag">Role to confirm</span></p><ul class="pstats pending"><li><b>00</b>Stat to come</li><li><b>00</b>Stat to come</li><li><b>00</b>Stat to come</li></ul><div class="bio"><p>Aim\u00e9e\u2019s career isn\u2019t just a series of job titles and accolades. It\u2019s a masterclass in blending razor-sharp business acumen with a genuine commitment to making a difference.</p><p>She began ad-life as a graduate at Ogilvy &amp; Mather in 2000, before joining start-up agency BMB in 2006 and becoming Managing Director in 2013. There she ran the TUI business for a decade, producing some of the most decorated campaigns in the industry.</p><p>After launching Fortnight Collective in Europe, she joined The Liberty Guild, a fresh, scalable alternative to the traditional agency model. Alongside leading key client business, Aim\u00e9e guided the Guild to B Corp status and a place in the Sunday Times Best Places to Work 2026.</p><p>Aim\u00e9e has been a Founding Trustee of CALM since 2006, is the Chair of Words Matter and a Trustee of the Langa Township Pre-School Trust in Cape Town. She is also a Marketer in Residence and Honorary Teaching Fellow at Lancaster University. And whilst not a natural athlete, Aim\u00e9e has harrumphed around the London Marathon five times.</p></div></div></article>
    <article class="lead-row"><div class="ph">Portrait to come</div><div class="lr-txt"><h3>Holly Dillon</h3><p class="role"><span class="pending-tag">Role to confirm</span></p><ul class="pstats pending"><li><b>00</b>Stat to come</li><li><b>00</b>Stat to come</li><li><b>00</b>Stat to come</li></ul><div class="bio"><p>Holly leads the business across commercial strategy, growth, operations and delivery. She oversees senior client relationships and strategic partnerships, including partnerships with cultural organisations such as TED, connecting brands and businesses with the conversations, communities and moments shaping their industries.</p><p>With over 15 years of experience building businesses and leading international teams, Holly brings executive leadership experience from film and television production and storytelling, which informs her approach to business strategy, creative ambition and commercial growth. She works closely with C-suite leaders and senior decision-makers to identify commercial opportunities, build relationships and translate ambition into business growth.</p><p>Prior to Culture3, Holly launched and built Variety\u2019s branded content studio, developing partnerships with Netflix and Apple TV, and delivering award-winning work around NEON\u2019s Parasite.</p><p>Holly is also the founder of Get Your Skin Out, changing how visible skin conditions are represented across culture.</p></div></div></article>
    <article class="lead-row"><div class="ph">Portrait to come</div><div class="lr-txt"><h3>Jamila Saidi</h3><p class="role"><span class="pending-tag">Role to confirm</span></p><ul class="pstats pending"><li><b>00</b>Stat to come</li><li><b>00</b>Stat to come</li><li><b>00</b>Stat to come</li></ul><div class="bio"><p>Jamila leads on strategic growth, partnership development and commercial expansion, working with brands, businesses and entrepreneurs at the intersection of culture, creativity and commerce. Her background in marketing and international trade and investment promotion informs a commercially grounded approach to building lasting client relationships.</p><p>With over 20 years of experience as a global growth leader and commercial strategist, Jamila specialises in entering new markets, building high-value partnerships and scaling opportunities internationally. She works closely with founders, C-suite leaders and brand decision-makers to unlock growth that is both ambitious and culturally resonant.</p><p>Jamila brings deep expertise in retail, luxury, fashion, beauty, digital and the creative industries. She is a passionate advocate for digital trade as a growth enabler and champions female founders and SMEs across the creative economy.</p><p>Prior to joining Culture3, Jamila held senior leadership roles at the UK\u2019s Department for Business and Trade, and worked in international marketing roles at Lloyds Bank Private Banking, Merrill Lynch Global Wealth Management and Grant Thornton.</p></div></div></article>
    <article class="lead-row"><div class="ph">Portrait to come</div><div class="lr-txt"><h3>Lins Karnes</h3><p class="role">Growth Lead</p><ul class="pstats pending"><li><b>00</b>Stat to come</li><li><b>00</b>Stat to come</li><li><b>00</b>Stat to come</li></ul><div class="bio"><p>Lins\u2019 attention to detail keeps everyone in line and makes stuff actually happen. He\u2019s a rare multi-platform, multi-format, digital-native production leader with a degree in computer science.</p><p>He\u2019s worked with big tech, CMS, e-commerce and digital transformation for companies such as HP, Compaq, Ford, Harvard Business School and non-governmental agencies. He\u2019s headed up digital production at Wunderman, BHH and Saint@RKCR/Y&amp;R, improving creative output across digital and integrated, and delivering global, European and national programmes for clients such as Microsoft and Unilever.</p><p>His last gig before he came to co-found The Liberty Guild was MD of B-Reel, the world\u2019s leading mixed-media production company, where he drove technical innovation and creative excellence across TV, film, content, digital, integrated, experiential and product development.</p></div></div></article>
  </div>
</section>
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

def page_guild(L, A):
    return f'''<section class="page-hero wrap">
  <h1>The best creative <span class="thin">department in the world.</span></h1>
  <div class="intro"><div class="stack">
    <p>The Guild is the creative A-list: 500+ of the world's best independent creatives, strategists and producers across 37 countries, with 2,315 awards between them.</p>
    <p>We work with our clients to handpick a bespoke team from this community for every project, whatever or wherever required.</p>
  </div></div>
</section>
<div class="sizzle wrap"><video class="lazyvid" muted loop playsinline preload="none" poster="{A("media/still-calibre.webp")}" data-src="{A("film/sizzle-guild.mp4")}" aria-hidden="true"></video></div>
<section class="band tight dark" aria-label="The Guild in numbers">
  <div class="wrap">
    <div class="figures">
      <div><span class="n">500+</span><span class="l">Creatives, strategists and producers</span></div>
      <div><span class="n">37</span><span class="l">Countries and cultures</span></div>
      <div><span class="n">2,315</span><span class="l">Top awards, collectively</span></div>
      <div><span class="n">33%</span><span class="l">Female</span></div>
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
      <p>For every brief, we handpick a team from our network. We back them with qual, quant or behavioural research, and run the work through our own tech stack. We use AI when it helps, and not when it doesn\u2019t.</p>
      <p>We can run everything end to end, from brief to production, or plug straight into your in-house team. Same calibre of talent either way.</p>
    </div>
  </div>
</section>
<section class="band wrap" aria-labelledby="gt" style="padding-top:0">
  <div class="split">
    <div class="l"><h2 class="h2" id="gt">What makes our talent <span class="thin">better?</span></h2></div>
    <div class="r prose">
      <p class="lead-light">They\u2019ve already won big at Cannes, D&amp;AD and the Effies. Strategically and creatively, this is the global A-list.</p>
      <p>And they\u2019re not passing through. They\u2019re here because this is how they want to work. As client demand grows, they\u2019re being joined by a new generation of social-native creators and AI artists.</p>
      <p>Every project starts by finding the right people for the brief. Not whoever\u2019s free. Not whoever\u2019s cheapest.</p>
      <p>Get that right and the ideas get better. And they get there faster.</p>
    </div>
  </div>
</section>
{mosaic(A, '<span>Taste and judgement.</span> <span>Insight and evidence.</span>', 'Handpicked for your brief, on your work from day one. See what a Guild team can do for you.', L('services/'), 'Our services')}
<section class="voice dark quote-band" aria-label="What clients say">
  <blockquote>“The quality of the healthy debates we have is a proof of the senior and highly experienced individuals behind the team, allowing us to build on each other\u2019s points of view that yield nothing but better outputs.”</blockquote>
  <p class="who">Estrella Lopez-Brea<span>Global Head of Insights, CPW</span></p>
</section>
{cta(L)}'''

WHATWEDO = [
    ('Brand strategy', "Building a new brand from scratch? Taking an existing one somewhere new? Or just buffing a dusty one up a bit? We work out where it\u2019s coming from and where it needs to go. And why. From positioning and architecture to the brief that gets the work made.",
     ['Strategic consultancy', 'Brand audits and roadmaps', 'Brand positioning', 'Brand architecture', 'Communications strategy', 'Creative briefing'], 'still-calibre'),
    ('Brand identity', "Once you know what your brand stands for, you have to look and sound like it. We create the name, the identity, the voice and the visual world that make it unmistakable. And the guidelines that keep it that way.",
     ['Brand development and rebranding', 'Naming', 'Visual identity and brand guidelines', 'Tone of voice'], 'poster-ms-food'),
    ('Creative', "A box fresh global platform. Your next differentiating brand campaign. The socially native work you\u2019re just not getting from your AoR? A difficult brief that needs a fresh perspective? We develop ideas with the breadth to span channels and cultures. We can spin a \u2018creative hot shop\u2019 up literally anywhere.",
     ['Creative platforms', 'Campaign strategy and development', 'Advertising concepts', 'Integrated and multi-channel campaigns', 'Brand and product launches', 'Digital and social creative', 'Content ideas', 'Creator and influencer', 'Global and local campaigns', 'Creative sprints'], 'poster-wizz-air'),
    ('Production', "Give the idea the craft it deserves. We bring campaigns and content to life across channels and markets, through us or alongside your existing production team. Our AI artists and virtual production specialists work alongside traditional crews, so big ideas no longer need big budgets to get made. And with our global content amplification partner, we deliver scaled brilliance: one great idea, built out into every asset, format and market it needs.",
     ['Campaign production', 'Film and video', 'AI production', 'Virtual production', 'Photography', 'Animation and motion', 'Design', 'Digital and social assets', 'Post-production', 'Adaptation and localisation', 'Content at scale'], 'still-craft'),
    ('In-house augmentation', "Boost your in-house team with freshness and firepower on demand or embedded. Many in-house teams carry a \u2018negative trust equity\u2019 with the business for years. Through our plug-and-play services built for in-house agencies, we put award-winning creatives and strategists alongside your team within days, to crack briefs, develop campaigns and strengthen design. We can also give you \u2018strategy on demand\u2019 over WhatsApp. Together, they help your team earn its place as a strategic partner.",
     ['Strategic projects', 'Campaign development', 'Design projects', 'Creative direction', 'Creative mentoring', 'Production excellence', 'Ongoing creative support'], 'still-pie'),
]

def page_services(L, A):
    rows = []
    for i, (name, txt, caps, img) in enumerate(WHATWEDO):
        cap = ''.join(f'<li>{esc(c)}</li>' for c in caps)
        rows.append(f'<li class="wwd"><div class="kk"><span class="wn">{i+1:02d}</span><h2 class="k">{esc(name)}</h2></div><div class="v"><p>{esc(txt)}</p><ul class="caps">{cap}</ul></div><div class="wimg px"><img src="{A("media/"+img+".webp")}" alt="" loading="lazy"></div></li>')
    rows.append(f'<li class="wwd"><div class="kk"><span class="wn">06</span><h2 class="k">Culture3</h2></div><div class="v"><p>Culture3 connects brands to cultural opportunities through strategic partnerships, relevant voices and moments that give them a credible role in the conversations that matter. We help brands understand where to show up, who to show up with and what to build to make their participation meaningful.</p><ul class="caps"><li>Cultural strategy</li><li>Partnerships and cultural access</li><li>Cultural programming and experiences</li><li>Content development</li></ul><p><a class="sec-link" href="{L("culture3/")}">Explore Culture3</a></p></div><div class="wimg px"><img src="{A("media/still-culture.webp")}" alt="" loading="lazy"></div></li>')
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
{cta(L)}'''

def page_culture(L, A):
    boxes = [('Partnerships that matter', 'Platforms, institutions and organisations that create access, credibility and distinctive opportunities. Proof: TED, and a pipeline of new and impactful partnerships.'),
             ('Moments that matter', 'Events, formats and spaces where the relevant conversations are happening. Live programming, salons, and original formats such as Offstage.'),
             ('Voices that matter', 'Thinkers, speakers, creators and specialists who bring authority, perspective and cultural relevance to a conversation.'),
             ('Creativity that matters', "Freedom Works' global network of independent creatives, bringing culturally fluent perspectives across markets, disciplines and communities.")]
    bx = '\n'.join(f'<div class="box"><h3>{esc(k)}</h3><p>{esc(v)}</p></div>' for k, v in boxes)
    svc = [('Strategic cultural partners', 'Partner strategy, access and activation with the institutions that shape culture. TED, and a pipeline of new partnerships.'),
           ('Talent and voice curation', 'Speakers, thinkers, creators and specialists around your topic and ambition. TED talent, K\u016a KAI, our wider network.'),
           ('Live cultural programming', 'Events, conversations, panels and salons built around relevant topics and voices. Offstage, Culture3 Conversations.'),
           ('Original formats and IP', 'Repeatable editorial, film and event propositions built around a cultural opportunity. The PwC Chair Table.')]
    rows = '\n'.join(f'<li><span class="k">{esc(k)}</span><span class="v">{esc(v)}</span></li>' for k, v in svc)
    return f'''<section class="page-hero wrap">
  <h1>Culture gets <span class="thin">you noticed.</span></h1>
  <div class="intro"><div class="stack">
    <p>Culture3 connects brands to the partnerships, communities, moments and voices shaping culture. We identify where a brand can credibly participate, who it should show up with, and what role it can play in the conversation to make the work matter. Physical. Nuanced. Human.</p>
  </div></div>
</section>
<div class="sizzle wrap"><video class="lazyvid" muted loop playsinline preload="none" poster="{A("media/still-culture.webp")}" data-src="{A("film/sizzle-culture.mp4")}" aria-hidden="true"></video></div>
<section class="c3-about wrap" aria-label="About Culture3">
  <div class="c3-logo">{logo_slot("Culture3", "big")}</div>
  <p class="c3-p">Bringing cultural access, strategic partnerships, relevant voices and culturally fluent creativity together to build propositions, formats and opportunities that let a brand take part in culture. It draws on the wider Freedom Works network where needed.</p>
</section>
<section class="band tight wrap" aria-label="What Culture3 brings" style="padding-top:0">
  <div class="boxes four">
{bx}
  </div>
</section>
{strip3(A, "still-lunch", "still-culture", "still-mountain")}
<section class="c3-method band wrap" aria-labelledby="c3m">
  <div class="split" style="margin-bottom:40px">
    <div class="l"><p class="sec-lbl"><span class="mk" aria-hidden="true"></span>Our methodology</p><h2 class="h2" id="c3m">Where to show up. Who to show up with. <span class="thin">What to build.</span></h2></div>
  </div>
  <ol class="c3-steps">
    <li><span class="sn">01</span><h3>Strategy</h3><p>We find the cultural opportunities, audiences and moments that fit a brand\u2019s commercial or cultural ambitions.</p></li>
    <li><span class="sn">02</span><h3>Access</h3><p>We connect brands with established cultural institutions, communities and influential voices.</p></li>
    <li><span class="sn">03</span><h3>Programming</h3><p>We develop and curate events, conversations and experiences that bring cultural ideas to life.</p></li>
    <li><span class="sn">04</span><h3>Content</h3><p>We make original film, editorial series and content that builds cultural relevance and keeps audiences engaged.</p></li>
  </ol>
</section>
<section class="band dark" aria-labelledby="c3o">
  <div class="wrap">
    <div class="split" style="margin-bottom:40px">
      <div class="l"><h2 class="h2" id="c3o">Culture3 <span class="thin">offerings</span></h2></div>
    </div>
    <ul class="c3-offers">
      <li><div class="ok"><h3>Offstage</h3><p class="os">Event sponsorship and partnerships</p></div><p class="ov">Culture3\u2019s curated event series for C-suite leaders, decision-makers and cultural voices, held at key moments such as Cannes. Brands sponsor an intimate, moderated conversation built around their industry, with access to a carefully curated room of people and perspectives.</p></li>
      <li><div class="ok"><h3>A Culture3 Conversation</h3><p class="os">Sponsored conversations and cultural partnerships</p></div><p class="ov">A focused, programmed discussion on a question that matters to a brand\u2019s industry, at moments such as SXSW London. We find the topic, partners and speakers, with the option to extend the conversation into editorial content.</p></li>
      <li><div class="ok"><img class="ted-logo" src="{A("logos/ted.webp")}" alt="TED" width="1280" height="471"><h3 class="sr-only">TED Partnerships</h3><p class="os">TED Partnerships: strategic partnerships and cultural access</p></div><p class="ov">Bespoke partnerships with TED, one of the world\u2019s leading platforms for ideas. Access to TED\u2019s ecosystem of voices, content and events gives brands a credible role in the conversations shaping their industry.</p></li>
      <li><div class="ok"><h3>Cultural partners</h3><p class="os">Strategic partnerships and cultural access</p></div><p class="ov">We connect brands with established cultural institutions, platforms and intellectual property, and build bespoke commercial opportunities across content, events, influential voices and audience engagement.</p></li>
      <li><div class="ok"><h3>Custom brand partnerships</h3><p class="os">Brand strategy, content and experiences</p></div><p class="ov">We work directly with brands on bespoke cultural partnerships, from original film and editorial series to curated events and live experiences, to give them a credible role in culture and reach new audiences.</p></li>
    </ul>
  </div>
</section>
{cta(L)}'''

def page_work(L, A):
    return f'''<section class="page-hero wrap" style="padding-bottom:40px">
  <h1>Work that <span class="thin">matters.</span></h1>
  <div class="intro"><div class="stack"><p>Creative work should move the numbers a board cares about: sales, share, demand and value. Here\u2019s what ours has done.</p></div></div>
</section>
<div class="sizzle wrap"><video class="lazyvid" muted loop playsinline preload="none" poster="{A("media/still-mountain.webp")}" data-src="{A("film/sizzle-work.mp4")}" aria-hidden="true"></video></div>
<section class="work wrap" style="padding-top:24px">
  <div class="grid">
    {chr(10).join(tile(p, L, A) for p in PROJECTS)}
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
    elif p['img']:
        film = f'<img class="wide" src="{A("media/"+p["img"]+".webp")}" alt="{esc(p["client"])}, {esc(p["camp"])}">'
    else:
        film = f'<div class="film static"><div class="typo"><span class="tn">{esc(p["n"] or p["client"])}</span><span class="tc">{esc(p["l"])}</span></div></div>'
    extra = ''.join(f'<li>{esc(e)}</li>' for e in p['extra'])
    extra = f'<ul>{extra}</ul>' if extra else ''
    body = ''
    if p['copy'] or p['n']:
        res = f'<div class="res"><span class="n" data-count>{esc(p["n"])}</span><span class="l">{esc(p["l"])}</span>{extra}</div>' if p['n'] else ''
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
        q = f'<section class="voice proj-quote wrap" aria-label="Client quote"><blockquote>\u201c{esc(p["quote"][0])}\u201d</blockquote><p class="who">{esc(p["quote"][1])}<span>{esc(p["quote"][2])}</span></p></section>'
    return f'''<section class="proj-hero wrap">
  <p class="client">{esc(p["client"])}</p>
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
    return f'''<section class="page-hero wrap" style="padding-bottom:40px">
  <h1>Thinking</h1>
  <div class="intro"><div class="stack"><p>{len(POSTS)} articles on creativity, AI, talent and the agency model.</p></div></div>
</section>
<section class="thinking wrap">
  <div class="filters" role="group" aria-label="Filter articles">{btn}</div>
  {post_cards(POSTS, L, A, with_data=True)}
</section>
{cta(L)}'''

def page_article(p, L, A, strip_images=False):
    body = markdown.markdown(p['body_md'], extensions=['extra'])
    body = re.sub(r'<img ', '<img loading="lazy" ', body)
    e = IMGMAP.get(p['slug']); loc = local_img(p['slug'])
    if e and loc and e.get('src') and e['src'] in body:
        body = body.replace(e['src'], A(loc))
    elif loc and e and e.get('from') == 'cover':
        body = f'<p><img loading="lazy" src="{A(loc)}" alt=""></p>' + body
    if strip_images:
        body = re.sub(r'<p>\s*<img[^>]*src="http[^"]*"[^>]*>\s*</p>', '', body); body = re.sub(r'<img[^>]*src="http[^"]*"[^>]*>', '', body)
    tag = TAGS.get(p['tag'], 'Thinking')
    return f'''<article>
  <header class="article-head wrap">
    <p class="k">{esc(tag)}</p>
    <h1>{esc(p["title"])}</h1>
    <p class="meta">{esc(p["author"])}, {month(p["date"])}. Originally published by The Liberty Guild, now Freedom Works. <a href="{esc(p["originalUrl"])}">Read the original</a></p>
  </header>
  <div class="article-body wrap"><div class="prose">
{body}
  </div></div>
</article>
<nav class="wrap" aria-label="More thinking"><a class="next" href="{L("thinking/")}"><span class="k">More thinking</span><span class="t">All articles</span></a></nav>
{cta(L)}'''

def page_contact(L, A):
    return f'''<section class="contact contact-page" aria-labelledby="ct">
  <div class="wrap">
    <h1 id="ct" style="margin:0;font-family:var(--display);font-weight:900;text-transform:uppercase;line-height:.88;font-size:clamp(84px,15vw,280px)">Let's make <span class="thin" style="font-weight:200;display:block">work that matters.</span></h1>
    {contact_cards(big=True)}
  </div>
</section>'''

def page_404(L, A):
    return f'''<section class="nf wrap">
  <h1 class="h2">This page <span class="thin">doesn't exist.</span></h1>
  <p class="lead-light" style="margin-top:28px">It may have moved when we became Freedom Works.</p>
  <p><a class="sec-link" href="{L("")}">Go to the homepage</a> &nbsp; <a class="sec-link" href="{L("work/")}">See the work</a></p>
</section>'''

# ---------------- chrome ----------------
def header(L, A, active):
    links = ''.join(f'<a href="{L(p)}"{" aria-current=\"page\"" if p == active else ""}>{t}</a>' for p, t in NAV)
    big = ''.join(f'<li><a href="{L(p)}">{t}</a></li>' for p, t in NAV)
    return f'''<header class="site-head">
  <a class="mark" href="{L("")}" aria-label="Freedom Works home"><img class="lg-white" src="{A("brand/logo-white.png")}" alt="Freedom Works" width="1600" height="287"><img class="lg-indigo" src="{A("brand/logo-indigo.png")}" alt="" aria-hidden="true" width="1600" height="287"></a>
  <nav aria-label="Main">{links}</nav>
  <button class="menu-btn" aria-expanded="false" aria-controls="menu">Menu</button>
</header>
<div class="overlay" id="menu" role="dialog" aria-label="Menu">
  <div class="top"><img src="{A("brand/logo-linen.png")}" alt="Freedom Works"><button class="menu-btn" style="display:block" data-close>Close</button></div>
  <ul>{big}</ul>
  <p class="small">hello@freedom.works</p>
</div>'''

def footer(L, A):
    links = ''.join(f'<a href="{L(p)}">{t}</a>' for p, t in NAV[:6])
    return f'''<footer class="foot wrap">
  <div class="brand"><img src="{A("brand/logo-linen.png")}" alt="Freedom Works"><span>A global creative agency.<br>Calibre, Culture, Craft.</span></div>
  <div class="links">{links}<a href="https://www.linkedin.com">LinkedIn</a><a href="https://www.instagram.com">Instagram</a></div>
  <div class="legal"><span>Freedom Works, London</span><a href="mailto:hello@freedom.works">hello@freedom.works</a></div>
</footer>
<div class="foot-mark" aria-hidden="true"><img src="{A("brand/logo-white.png")}" alt="" loading="lazy"></div>'''

FLOURISH_JS = open(SP('flourish.js')).read()
SHADERS_JS = open(SP('shaders.js')).read()
SCRIPT = '''<script>
(function(){
  var v=document.querySelector('.hero video'),b=document.querySelector('.pause');
  if(v){v.playbackRate=.7;v.addEventListener('loadeddata',function(){var p=document.querySelector('.hero .poster');if(p)p.style.display='none';});}
  if(b&&v){b.addEventListener('click',function(){if(v.paused){v.play();b.setAttribute('aria-label','Pause film');}else{v.pause();b.setAttribute('aria-label','Play film');}});}
  var hd=document.querySelector('.site-head');function sc(){if(hd)hd.classList.toggle('solid',window.scrollY>24);}window.addEventListener('scroll',sc,{passive:true});sc();
  var m=document.getElementById('menu'),open=document.querySelector('.site-head .menu-btn');
  if(open&&m){open.addEventListener('click',function(){m.classList.add('open');open.setAttribute('aria-expanded','true');});
  m.querySelectorAll('[data-close], a').forEach(function(el){el.addEventListener('click',function(){m.classList.remove('open');open.setAttribute('aria-expanded','false');});});}
  document.querySelectorAll('.filters').forEach(function(f){f.addEventListener('click',function(e){var t=e.target.closest('button');if(!t)return;
    f.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===t?'true':'false');});
    var k=t.getAttribute('data-f');document.querySelectorAll('.posts li[data-tag], .cards li[data-tag]').forEach(function(li){li.hidden=!(k==='all'||li.getAttribute('data-tag')===k);});});});
})();
</script>
<script>''' + FLOURISH_JS + '''</script>
<script>''' + SHADERS_JS + '''</script>'''

ORG = {"@context": "https://schema.org", "@type": "Organization", "name": "Freedom Works", "alternateName": "FRE3DOM WORKS",
       "url": DOMAIN, "logo": DOMAIN + "/assets/brand/logo-indigo.png", "address": {"@type": "PostalAddress", "addressLocality": "London", "addressCountry": "GB"},
       "subOrganization": {"@type": "Organization", "name": "Culture3", "url": DOMAIN + "/culture3/", "description": "Culture3 connects brands to the partnerships, communities, moments and voices shaping culture."}}

def crumbs(path, title):
    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": DOMAIN + "/"}]
    parts = [x for x in path.strip('/').split('/') if x]
    names = {'work': 'Work', 'agency': 'About', 'the-guild': 'The Guild', 'services': 'Services', 'culture3': 'Culture3', 'thinking': 'Thinking', 'contact': 'Contact'}
    for i, part in enumerate(parts):
        nm = names.get(part, title) if i < len(parts) - 1 or part in names else title
        items.append({"@type": "ListItem", "position": i + 2, "name": nm, "item": DOMAIN + "/" + "/".join(parts[:i + 1]) + "/"})
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}

# ---------------- service pages (SEO: one page per service / sub-service) ----------------
SERVICE_PAGES_LIVE = False   # flip to True to publish the service pages, add them to the sitemap and link them from Services
DRAFTS = [False]
import sys as _sys
_sys.path.insert(0, SP(''))
from service_pages import SERVICE_PAGES, Q as SVC_QUOTES

def related_posts(keywords, n=3):
    def score(p):
        hay = (p['title'] + ' ' + (p.get('description') or '')).lower()
        return sum(1 for k in keywords if k in hay)
    ranked = sorted(POSTS, key=lambda p: (-score(p), p['date']), reverse=False)
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
    logos = ''.join(f'<li><img src="{A("logos/wall/"+x["slug"]+"-ink.png")}" alt="{esc(x["name"])}" style="height:{min(44, 1500 / x["w"]):.0f}px" loading="lazy"></li>' for x in LOGOWALL[:8])
    about = ''.join(f'<p>{esc(x)}</p>' for x in sp['about'][1:])
    stats = ''.join(f'<li><b>{esc(n)}</b><span>{esc(t)}</span><em>{esc(c)}</em></li>' for n, t, c in sp['stats'][:3])
    steps = ''.join(f'<li><span class="n">{i+1:02d}</span><h3>{esc(n)}</h3><p>{esc(t)}</p></li>' for i, (n, t) in enumerate(sp['process']))
    if sp['level'] == 2:
        links = sp['children']; svc_label = 'Services'
        extra = ''.join(f'<li class="plain"><span class="k">{esc(c)}</span></li>' for c in sp.get('extra_caps', []))
    else:
        par = sp['parent']; links = [c for c in par['children'] if c is not sp] + [par]; svc_label = 'Related'; extra = ''
    rows = ''.join(f'<li><a href="{L(c["path"])}"><span class="k">{esc(c["name"]) if c is not sp.get("parent") else "All " + esc(c["name"].lower())}</span><span class="d">{esc(c["line"])}</span><span class="go" aria-hidden="true">\u2192</span></a></li>' for c in links) + extra
    projs = {p['slug']: p for p in PROJECTS}
    tiles = '\n'.join(tile(projs[s_], L, A) for s_ in sp['cases'][:2] if s_ in projs)
    qk = sp['quotes'][0]; qt, qn, qr = SVC_QUOTES[qk]
    faqs = ''.join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in sp['faqs'][:4])
    by_slug = {x['slug']: x for x in POSTS}
    chosen = [next(x for x in POSTS if x['slug'].startswith(k)) for k in sp.get('articles', []) if any(x['slug'].startswith(k) for x in POSTS)] or related_posts(sp['keywords'])
    arts = ''.join(f'<li><a href="{L("thinking/"+x["slug"]+"/")}"><span class="t">{esc(x["title"])}</span><span class="m">{month(x["date"])}</span></a></li>' for x in chosen[:3])
    return f'''<div class="svcpage">
<div class="draft-banner">Example page with starter copy, for review. Not yet live on the site.</div>
<header class="svc-top wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><ol>{crumbs_html}</ol></nav>
  <h1>{sp["h1"]}</h1>
  <div class="svc-top-row">
    <p class="svc-intro">{esc(sp["intro"])}</p>
    <div class="svc-cta"><a class="ct-btn" href="{L("contact/")}">{esc(sp["cta"])} <span aria-hidden="true">\u2192</span></a><a class="svc-mail" href="mailto:hello@freedom.works">or email hello@freedom.works</a></div>
  </div>
  <div class="svc-logos"><p class="svc-label">Trusted by</p><ul>{logos}</ul></div>
</header>
<section class="svc-row wrap" aria-labelledby="s-exp"><h2 class="svc-label" id="s-exp">Our experience</h2><div class="svc-body">
  <p class="svc-lead">{esc(sp["about"][0])}</p>{about}
  <ul class="svc-stats">{stats}</ul>
</div></section>
<section class="svc-row wrap" aria-labelledby="s-how"><h2 class="svc-label" id="s-how">How we work</h2><div class="svc-body"><ol class="svc-steps">{steps}</ol></div></section>
<section class="svc-row wrap" aria-labelledby="s-svc"><h2 class="svc-label" id="s-svc">{svc_label}</h2><div class="svc-body"><ul class="svc-links">{rows}</ul></div></section>
<section class="svc-row wrap" aria-labelledby="s-work"><h2 class="svc-label" id="s-work">Work</h2><div class="svc-body">
  <div class="grid svc-tiles">{tiles}</div>
  <figure class="svc-quote"><blockquote>\u201c{esc(qt)}\u201d</blockquote><figcaption><b>{esc(qn)}</b>{esc(qr)}</figcaption></figure>
</div></section>
<section class="svc-row wrap" aria-labelledby="s-faq"><h2 class="svc-label" id="s-faq">Questions</h2><div class="svc-body faq">{faqs}</div></section>
<section class="svc-row wrap" aria-labelledby="s-th"><h2 class="svc-label" id="s-th">Thinking</h2><div class="svc-body"><ul class="svc-articles">{arts}</ul><a class="sec-link" href="{L("thinking/")}">All articles</a></div></section>
</div>
{cta(L)}'''

def service_schema(sp):
    url = DOMAIN + '/' + sp['path']
    svc = {"@context": "https://schema.org", "@type": "Service", "name": sp['name'], "serviceType": sp['name'], "url": url,
           "description": sp['intro'], "areaServed": "Worldwide", "provider": {"@type": "Organization", "name": "Freedom Works", "url": DOMAIN + "/"}}
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in sp['faqs']]}
    bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": DOMAIN + "/" + p} for i, (n, p) in enumerate(svc_crumbs(sp))]}
    return [svc, faq, bc]

def service_page_entries():
    for sp in SERVICE_PAGES:
        yield (sp['path'], sp['title'], sp['desc'], (lambda sp: lambda L, A: page_service(sp, L, A))(sp), 'services/', service_schema(sp))

def pages():
    """yield (path, title, description, body_fn, active, extra_schema)"""
    yield ('', 'Freedom Works | Global creative agency, London', 'A global creative agency built on Calibre, Culture and Craft. More than 500 award-winning independent creatives and strategists, handpicked for every brief.', page_home, '', [{"@context": "https://schema.org", "@type": "WebSite", "name": "Freedom Works", "url": DOMAIN + "/", "inLanguage": "en-GB"}])
    yield ('agency/', 'About | Freedom Works', 'Freedom makes better work. Our DNA of Calibre, Culture and Craft, and the leadership behind Freedom Works, a global creative agency.', page_agency, 'agency/', [])
    yield ('the-guild/', 'The Guild | Freedom Works', '500+ of the world\u2019s best independent creatives, strategists and producers across 37 countries, handpicked for every brief.', page_guild, 'the-guild/', [])
    faq_schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}
    yield ('services/', 'Services | Freedom Works', 'Brand strategy, brand identity, creative, production and in-house augmentation, from the best creative department in the world.', page_services, 'services/', [])
    if SERVICE_PAGES_LIVE or DRAFTS[0]:
        yield from service_page_entries()
    yield ('culture3/', 'Culture3 | Freedom Works', 'Culture3 connects brands to the partnerships, communities, moments and voices shaping culture. Physical. Nuanced. Human.', page_culture, 'culture3/', [])
    yield ('work/', 'Work | Freedom Works', 'Work that matters for King Arthur Baking, Wizz Air, M&S Food, loveholidays, Rowse Honey and Brompton.', page_work, 'work/', [])
    for i, p in enumerate(PROJECTS):
        art = {"@context": "https://schema.org", "@type": "CreativeWork", "name": f"{p['client']}: {p['camp']}", "creator": {"@type": "Organization", "name": "Freedom Works"}}
        yield (f'work/{p["slug"]}/', f'{p["client"]}: {p["camp"]} | Freedom Works', (p['copy'] or p['short'] or f'{p["client"]}: {p["camp"]}, a film by Freedom Works.')[:155], (lambda i: lambda L, A: page_project(i, L, A))(i), 'work/', [art])
    yield ('thinking/', 'Thinking | Freedom Works', 'Articles on creativity, AI, talent and the agency model from Freedom Works.', page_thinking, 'thinking/', [])
    for p in POSTS:
        art = {"@context": "https://schema.org", "@type": "Article", "headline": p['title'], "datePublished": p['date'], "author": {"@type": "Person", "name": p['author']}, "publisher": {"@type": "Organization", "name": "Freedom Works"}}
        desc = p['description'] or p['title']
        yield (f'thinking/{p["slug"]}/', f'{p["title"]} | Freedom Works', desc[:155], (lambda p: lambda L, A, **k: page_article(p, L, A, **k))(p), 'thinking/', [art])
    yield ('contact/', 'Contact | Freedom Works', "Let's make work that matters. Talk to Freedom Works.", page_contact, 'contact/', [])

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
"""

def build_site():
    os.makedirs(OUT, exist_ok=True)
    for name in os.listdir(OUT):
        if name == 'assets': continue
        pth = os.path.join(OUT, name)
        shutil.rmtree(pth) if os.path.isdir(pth) else os.remove(pth)
    open(os.path.join(OUT, 'assets', 'site.css'), 'w').write(CSS.replace('url(../fonts/', 'url(fonts/'))
    urls = []
    for path, title, desc, fn, active, extra in list(pages()) + [('404', 'Page not found | Freedom Works', 'This page does not exist.', page_404, '', [])]:
        depth = 0 if path in ('', '404') else path.strip('/').count('/') + 1
        R = '../' * depth
        L = lambda p, R=R: (R + p) if (R + p) else './'
        A = lambda rel, R=R: R + 'assets/' + rel
        body = add_pill(fn(L, A), path, A)
        canon = DOMAIN + '/' + (path if path != '404' else '')
        _slug = path.strip('/').split('/')[-1] if path.startswith('thinking/') and path.count('/') == 2 else None
        og_img = DOMAIN + '/assets/' + local_img(_slug) if _slug and local_img(_slug) else DOMAIN + '/assets/media/hero-poster.jpg'
        robots = '<meta name="robots" content="noindex">\n' if path == '404' else ''
        doc = f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{robots}<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canon}">
<meta property="og:title" content="{esc(title.split(' | ')[0])}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="{og_img}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{A('favicon.png')}">
<link rel="apple-touch-icon" href="{A('apple-touch-icon.png')}">
<meta name="theme-color" content="#20243A">
<link rel="preload" href="{A('fonts/castel-500.woff2')}" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{A('site.css')}">
{schema_tags(path if path != '404' else '', title, extra)}
</head>
<body{' class="light-page"' if path else ''}>
{header(L, A, active)}
<main>
{body}
</main>
{footer(L, A)}
{SCRIPT}
</body>
</html>'''
        if path == '404':
            open(os.path.join(OUT, '404.html'), 'w').write(doc); continue
        d = os.path.join(OUT, path); os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'index.html'), 'w').write(doc)
        urls.append(canon)
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>{u}</loc></url>\n' for u in urls) + '</urlset>\n'
    open(os.path.join(OUT, 'sitemap.xml'), 'w').write(sm)
    open(os.path.join(OUT, '.htaccess'), 'w').write(HTACCESS)
    open(os.path.join(OUT, '_redirects'), 'w').write(NETLIFY_REDIRECTS)
    open(os.path.join(OUT, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n')
    open(os.path.join(OUT, 'llms.txt'), 'w').write('# Freedom Works\n\n> A global creative agency built on Calibre, Culture and Craft. More than 500 award-winning independent creatives, strategists and producers across 37 countries, handpicked for every brief. Founded by Jon Williams, former CCO of Grey EMEA. London.\n\n## Pages\n' + ''.join(f'- {u}\n' for u in urls[:12]))
    return urls

# ---------------- single-file preview ----------------
def build_preview(outfile, only=None, external=''):
    PREVIEW_MODE[0] = True
    if only: DRAFTS[0] = True
    BLOBS = {'media/hero-web-1080.mp4': '/_blob/236cf964b36609499310f1b6f9c02187', 'media/hero-web-720.mp4': '/_blob/236cf964b36609499310f1b6f9c02187', 'film/loop-brompton.mp4': '/_blob/fb70b76b545e261752f1007b224a0914', 'film/loop-king-arthur.mp4': '/_blob/11e84b9dfd392c34df4f8b3147a360d3', 'film/loop-loveholidays.mp4': '/_blob/ac1fb7bc3428cecf55bc18d9cc9e8596', 'film/loop-ms-food.mp4': '/_blob/93309566a4d8f63db8a919b3d1458992', 'film/loop-rowse.mp4': '/_blob/5a03bc879616fac9846acb87fe98a31e', 'film/loop-wizz-air.mp4': '/_blob/1f51403c0de73ccf10b5ed55869d03f1', 'film/pill-agency.mp4': '/_blob/74058972cfd8865c67a4f89e9f932f00', 'film/pill-culture.mp4': '/_blob/2b49a765a37676971f18311969cd3044', 'film/pill-guild.mp4': '/_blob/f07b3083512f2227e577c4795467dcdb', 'film/pill-home.mp4': '/_blob/f45c7fb2d95de2ac00666ca81b2b8544', 'film/pill-services.mp4': '/_blob/d14e844937787a4596f58d55ecbe1419', 'film/pill-work.mp4': '/_blob/cb417937508046e10476efa86b1d2fad', 'film/sizzle-agency.mp4': '/_blob/2c922d0807b61703f91fb066ddec1d98', 'film/sizzle-culture.mp4': '/_blob/e479f60a47b723971ff474ef508bb1aa', 'film/sizzle-guild.mp4': '/_blob/2f900cbdc062ccc3e0158b849feb2744', 'film/sizzle-services.mp4': '/_blob/0228e0f193eb87cac512554139ac10da', 'film/sizzle-work.mp4': '/_blob/dce94fc01016b3d6b5e60376216cbb53', 'film/sizzle-home.mp4': '/_blob/18036149359779457059a0361cec3ae8', 'film/loop-kitkat.mp4': '/_blob/3aed51c5c3115cb552326167924c704b', 'film/loop-tui.mp4': '/_blob/06f0c5fff0bcaa169fb85e218dea6611', 'film/loop-sma.mp4': '/_blob/7b602dba0e4702192183b810b3941f1a'}
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
    for f in ['castel-500', 'castel-900i', 'serif-400', 'serif-400i', 'cond-500', 'cond-600', 'tungsten-900', 'tungsten-200', 'hanken']:
        css = css.replace(f'url(../fonts/{f}.woff2)', f'url({data("fonts/" + f + ".woff2")})')
    for bi in ['icon-linen', 'icon-indigo', 'icon-peri']:
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
    open(outfile, 'w').write(doc)
    return os.path.getsize(outfile)

if __name__ == '__main__':
    urls = build_site()
    print('Built', len(urls), 'pages into site/')
