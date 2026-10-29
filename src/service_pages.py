"""Service pages (SEO structure: one page per service and sub-service).

Level 2 = a service (e.g. Brand strategy). Level 3 = a sub-service under it.
Each page: breadcrumbs, keyword H1, 30-60 word intro, client logos, CTA, then
experience copy, process, sub-services, testimonials, case studies, proof stats,
FAQs, related articles, and a closing CTA.

Starter copy for review. Pages are only published when SERVICE_PAGES_LIVE is True
in build.py.
"""

Q = {
    'gsk': ("In a sea of sameness, The Liberty Guild is a breath of fresh air. A thoroughly modern, no-nonsense approach to applied strategic creative thinking.", 'Nick Tate', 'ex VP Head of Next, Haleon Plc'),
    'rowse': ("The most integrated model I have seen when it comes to creative development. And yet it is so obvious that if you embed the consumer into the creative development process and are guided by the data and not the creative ego you are going to get better, more effective work.", 'Kirstie Jamieson', 'Marketing Director, Rowse Honey'),
    'snowfox': ("You delivered brilliantly throughout, provided amazing creativity and moral support and (most importantly) you were great fun to work with.", 'Simon Clough', 'Strategic Brand Consultant, Snowfox Group'),
    'mayfair': ("They deliver fantastic creative output at an incredible pace. Suffice to say, I\u2019m a huge fan of the team and their wonderful work.", 'Nick Keegan', 'Mayfair Equity Partners'),
    'nestle_ih': ("The Liberty Guild do more than just brilliant ideas delivered with beautiful precision, it\u2019s the soap box to elevate the in-house voice at the very heart of our brands. Bringing the best of outside, inside.", 'Tom Nixon', 'Head of Content Studios UK&I, Nestl\u00e9'),
    'cpw': ("The quality of the healthy debates we have is a proof of the senior and highly experienced individuals behind the team, allowing us to build on each other\u2019s points of view that yield nothing but better outputs.", 'Estrella Lopez-Brea', 'ex-Global Head of Insights, CPW'),
    'ka': ("Keep Rising has been transformative for King Arthur Baking. Not just creatively, but commercially. In a low interest category, The Guild helped us connect on a deeper emotional level.", 'Kim Stellavato', 'Brand Director, King Arthur Baking'),
    'brompton': ("We were looking for a partner who truly understood the spirit of Brompton, not just as a mode of transport, but as a way of moving through life with freedom, creativity, and purpose.", 'Chris Willingham', 'Global CMO, Brompton'),
    'lh_al': ("Since starting our brand journey with The Liberty Guild, we\u2019ve added nearly 15%pts of awareness and seen every brand metric we track increase at pace, while our competitors are flat or falling, all despite dramatically lower brand budgets.", 'Al Murray', 'CMO, loveholidays'),
    'lh_gemma': ("What\u2019s great about their offering is the global reach of their network. The ability to tap into creatives and strategists from across the globe whilst still having the expert support of a centrally managed account team gives us the best of both worlds.", 'Gemma Schmid', 'Director of Brand Marketing, loveholidays'),
    'nestle': ("I really couldn\u2019t have hoped for better. We can all collectively take pride in the achievement.", 'Tom Nixon', 'Head of Content Studios UK&I, Nestl\u00e9'),
    'tui': ("Their interpretation and understanding of our brief helped crystallise the strategic approach, which then went on to create some creative work that brought to life the proposition in a way that will allow us to flex across markets.", 'Rachel Moss', 'Head of International Marketing, TUI Group'),
}

BRAND_STRATEGY = {
    'path': 'services/brand-strategy/', 'level': 2, 'name': 'Brand strategy',
    'title': 'Global Brand Strategy | Freedom Works',
    'desc': 'Global brand strategy from senior strategists in a 600+ network, handpicked for your brief: positioning, architecture, and communications strategy.',
    'h1': 'Global <em>brand strategy</em>',
    'keyword': 'global brand strategy',
    'intro': 'Senior strategists, handpicked from The Guild for your brief, work out where your brand is coming from, where it needs to go and why. Then we turn it into a brand strategy the whole business can act on: a positioning, an architecture, and a brief that gets the work made.',
    'line': 'Positioning, communications strategy, and brand architecture.',
    'articles': ['introducing-whatstrat-senior-strategic', 'beach-reads-3-diy-strategist-how', 'in-the-agentic-era-travel-businesses'],
    'cta': 'Talk to us about brand strategy',
    'about_h': 'Strategy that <em>gets the work made</em>',
    'about': [
        'New brand? Taking one somewhere new? Or buffing a dusty one up a bit? We work out where it\u2019s coming from, where it needs to go and why.',
        'Every project gets a senior team chosen for this brief, not whoever happens to be free. Our strategists have led brand work for global networks, consultancies, and in-house teams, across food, and drink, travel, retail, and health.',
        'Strategy here isn\u2019t a document that sits on a shelf. It\u2019s the thinking that took King Arthur Baking from the #2 to the #1 flour brand in the US, and moved loveholidays from performance marketing to brand without losing demand.',
    ],
    'process': [
        ('Diagnose', 'We audit the brand, the category, and the audience, with research where it counts.'),
        ('Define', 'Where the brand should play and why it wins: positioning and architecture.'),
        ('Articulate', 'We turn the strategy into a platform, a story, and a tone the whole business can use.'),
        ('Brief', 'We write the brief that gets the work made, and stay with it through to launch.'),
    ],
    'subs_h': 'Brand strategy <em>services</em>',
    'extra_caps': [('Brand audits and roadmaps', 'Where your brand stands today, and the plan to get it where it needs to be.'), ('Strategic consultancy', 'Senior strategic thinking on call, for the decisions that shape the brand.'), ('Creative briefing', 'The brief that turns strategy into work: sharp, inspiring, and agreed.')],
    'quotes': ['gsk', 'ka', 'cpw'],
    'cases': ['king-arthur-baking', 'loveholidays', 'rowse-honey'],
    'stats': [('+100%', 'Sales uplift', 'King Arthur Baking'), ('+72%', 'Consideration', 'loveholidays'), ('98th', 'Percentile brand power', 'Rowse Honey'), ('600+', 'Strategists, creatives, and producers', 'The Guild')],
    'faqs': [
        ('What does brand strategy involve?', 'Brand strategy works out what a brand stands for, who it\u2019s for and how it wins, then turns that into a positioning, a brand architecture, and a brief that creative teams can act on. At Freedom Works, that strategy is built by a senior team handpicked from The Guild for your brief.'),
        ('How long does a brand strategy project take?', 'It depends on the scope. We work in short sprints with clear decision points, so you see the thinking early and often rather than waiting months for a big reveal.'),
        ('Do you work with in-house teams?', 'Yes. We can run the whole project, or plug senior strategists into your in-house team, your agencies, or both.'),
        ('Do you only do strategy?', 'No. Strategy usually leads into brand identity, creative, and production, and we can run all of it, so the thinking carries straight through into the work.'),
        ('Do you work internationally?', 'Yes. The Guild spans 37 countries and cultures, so we can build teams with the market and cultural knowledge your brief needs.'),
    ],
    'keywords': ['brand', 'strategy', 'position', 'marketing', 'cmo'],
}

POSITIONING = {
    'path': 'services/brand-strategy/brand-positioning/', 'level': 3, 'parent': BRAND_STRATEGY, 'name': 'Brand positioning',
    'title': 'Brand Positioning | Freedom Works',
    'desc': 'Brand positioning that finds the space your brand can own and the words to claim it. Senior strategists from a global network, handpicked for your brief.',
    'h1': 'Brand <em>positioning</em>',
    'keyword': 'brand positioning',
    'intro': 'We find the space in the market your brand can own, and the words to claim it. Positioning grounded in real insight, sharp enough to guide every decision and simple enough for the whole business to repeat.',
    'line': 'The space in the market your brand can own, and the words to claim it.',
    'articles': ['lbbonline-how-the-liberty-guild-distilled-down-the-essence-o', 'brands-taking-stands-aug2021', 'in-the-agentic-era-travel-businesses'],
    'cta': 'Talk to us about positioning',
    'about_h': 'Find the space <em>only you can own</em>',
    'about': [
        'A strong positioning makes every other decision easier: what to say, make, and leave out. A weak one turns everything into a debate.',
        'We start with the people you need to win and the category you compete in, then look for the truth about your brand that competitors can\u2019t copy. We test it, sharpen it, and write it down in language people actually use.',
        'It\u2019s how we repositioned Rowse Honey as the purpose led choice, with bee welfare at its heart: +24% new customers and a 98th percentile brand power score.',
    ],
    'process': [
        ('Listen', 'Interviews, data, and research to understand your audience, category, and competitors.'),
        ('Find the gap', 'The space your brand can credibly own, and why it matters to the people you need to win.'),
        ('Frame it', 'A clear positioning statement, proposition, and the reasons to believe it.'),
        ('Prove it', 'We test the positioning with real audiences and refine it until it holds up.'),
    ],
    'quotes': ['gsk', 'brompton'],
    'cases': ['rowse-honey', 'king-arthur-baking', 'brompton'],
    'stats': [('+24%', 'New customers', 'Rowse Honey'), ('98th', 'Percentile brand power', 'Rowse Honey'), ('#1', 'Flour brand in the US', 'King Arthur Baking')],
    'faqs': [
        ('What is brand positioning?', 'Brand positioning is the place your brand holds in people\u2019s minds compared with the alternatives: what you stand for, who you\u2019re for and why you\u2019re the better choice.'),
        ('How is positioning different from a tagline?', 'A tagline is one expression of a positioning. The positioning is the strategic idea underneath it, and it guides everything from product to tone of voice, not just the advertising.'),
        ('Can you reposition an established brand?', 'Yes. Repositioning is often about finding what\u2019s already true about a brand and making it matter more, as we did for Rowse Honey.'),
        ('How do you know a positioning is right?', 'It should be true to the brand, different from competitors and meaningful to the audience. We test it with real people before it goes anywhere near a campaign.'),
    ],
    'keywords': ['position', 'brand', 'purpose', 'differen'],
}

COMMS = {
    'path': 'services/brand-strategy/communications-strategy/', 'level': 3, 'parent': BRAND_STRATEGY, 'name': 'Communications strategy',
    'title': 'Communications Strategy | Freedom Works',
    'desc': 'Communications strategy that decides who to reach, what will move them and where. Channel agnostic planning from a global network of senior strategists.',
    'h1': 'Communications <em>strategy</em>',
    'keyword': 'communications strategy',
    'intro': 'We decide who you need to reach, what will move them and where to say it. Channel agnostic communications strategy that turns a brand idea into work people notice, from the first brief to the last week of the media plan.',
    'line': 'Who to reach, what will move them, and where to say it.',
    'articles': ['the-generative-moment-of-truth-why', 'being-found-is-the-easy-bit', 'allnewqueue-jul2020'],
    'cta': 'Talk to us about comms strategy',
    'about_h': 'The right message, <em>in the right places</em>',
    'about': [
        'Great ideas fail in the wrong place, at the wrong moment. Communications strategy gets the work to the people it\u2019s for, when they\u2019re open to it.',
        'We\u2019re channel agnostic. We start with the audience and the job the communication has to do, then decide what to make and where it should live: TV, out of home, social, creators, experiential, or all of them.',
        'It\u2019s how we helped loveholidays move from performance marketing to brand: +15pts awareness, +72% consideration, and 42% lower cost per click.',
    ],
    'process': [
        ('Audience', 'Who we need to reach, what they believe now, and what we need them to feel, think, or do.'),
        ('Message', 'The single idea and the proof points that will move them.'),
        ('Moments', 'Where and when the message will work hardest, across paid, owned, earned, and shared.'),
        ('Measure', 'Clear measures of success, built in from the start, so we know what\u2019s working.'),
    ],
    'quotes': ['lh_al', 'tui'],
    'cases': ['loveholidays', 'wizz-air', 'ms-food'],
    'stats': [('+15pts', 'Awareness', 'loveholidays'), ('\u201342%', 'Cost per click', 'loveholidays'), ('+11.4%', 'Demand, year on year', 'Wizz Air')],
    'faqs': [
        ('What is a communications strategy?', 'It\u2019s the plan for who you need to reach, what you need to say, and where and when to say it, so every piece of work has a clear job.'),
        ('How is it different from a media plan?', 'A media plan decides where to buy space. A communications strategy comes first: it decides what the work needs to achieve, and which channels, moments and formats will achieve it.'),
        ('Do you work with our media agency?', 'Yes. We often work alongside media agencies and in-house teams, so the strategy and the media plan pull in the same direction.'),
        ('Can you measure the impact?', 'We agree the measures of success up front and build them into the plan, from brand metrics to commercial results.'),
    ],
    'keywords': ['communication', 'media', 'channel', 'campaign', 'attention', 'social'],
}

ARCHITECTURE = {
    'path': 'services/brand-strategy/brand-architecture/', 'level': 3, 'parent': BRAND_STRATEGY, 'name': 'Brand architecture',
    'title': 'Brand Architecture | Freedom Works',
    'desc': 'Brand architecture that gives every brand in your portfolio a clear job. Portfolio strategy, mergers, and sub-brands from senior strategists worldwide.',
    'h1': 'Brand <em>architecture</em>',
    'keyword': 'brand architecture',
    'intro': 'We organise your brands so each one has a clear job. We untangle portfolios, merge or separate brands, and build a brand architecture that lets the business grow without confusing the people it sells to.',
    'line': 'A clear job for every brand in your portfolio.',
    'articles': ['beach-reads-6-free-aint-cheap-the', 'the-generative-moment-of-truth-why', 'in-the-agentic-era-travel-businesses'],
    'cta': 'Talk to us about brand architecture',
    'about_h': 'One clear system, <em>room to grow</em>',
    'about': [
        'Acquisitions, products, and sub-brands pile up. Soon customers can\u2019t tell how your brands relate, and every launch starts with a naming argument.',
        'We map what you have, work out what each brand needs to do for the business and the customer, and design the structure that makes the whole portfolio stronger: a branded house, a house of brands, or something in between.',
        'It\u2019s how we unified four Snowfox Group sushi brands under one strategic platform, strengthening their identity and commercial performance.',
    ],
    'process': [
        ('Map', 'An audit of every brand, sub-brand, and product name, and how customers actually see them.'),
        ('Model', 'Options for how the portfolio could be organised, tested against your growth plans.'),
        ('Decide', 'A clear recommendation, and the rules for using it.'),
        ('Roll out', 'Naming, identity, and a plan to move from today\u2019s structure to tomorrow\u2019s.'),
    ],
    'quotes': ['lh_gemma', 'cpw'],
    'cases': ['snowfox-group', 'nestle-sma', 'king-arthur-baking'],
    'stats': [('4', 'Brands, one platform', 'Snowfox Group'), ('2x', 'Baby Club sign-ups', 'Nestl\u00e9 SMA'), ('37', 'Countries in The Guild', 'The Guild')],
    'faqs': [
        ('What is brand architecture?', 'Brand architecture is the structure that defines how a company\u2019s brands, sub-brands and products relate to each other, and how they\u2019re named and presented.'),
        ('Should we be a branded house or a house of brands?', 'A branded house puts one master brand at the centre. A house of brands runs separate brands side by side. Most businesses sit somewhere in between, and the right answer depends on your growth plans and your customers.'),
        ('When do we need brand architecture work?', 'Usually after an acquisition or merger, before a major launch, or when a portfolio has grown faster than its structure.'),
        ('Do you handle naming and identity too?', 'Yes. Our brand identity team can create new names and visual systems once the structure is agreed.'),
    ],
    'keywords': ['architecture', 'portfolio', 'merger', 'sub-brand', 'brand'],
}


BRAND_STRATEGY['children'] = [POSITIONING, COMMS, ARCHITECTURE]
BRAND_STRATEGY['volume'] = 'Level 2 (SEO tab)'; POSITIONING['volume'] = '1,000+'; COMMS['volume'] = 'SEO tab'; ARCHITECTURE['volume'] = 'SEO tab'

def page(path, level, name, title, desc, h1, intro, line, cta, about, process, quotes, cases, stats, faqs, keywords, volume, parent=None, extra_caps=None):
    d = dict(path=path, level=level, name=name, title=title, desc=desc, h1=h1, intro=intro, line=line, cta=cta, about=about,
             process=process, quotes=quotes, cases=cases, stats=stats, faqs=faqs, keywords=keywords, volume=volume)
    if parent: d['parent'] = parent
    if extra_caps: d['extra_caps'] = extra_caps
    return d

# ---------------- BRAND IDENTITY ----------------
IDENTITY = page('services/brand-identity/', 2, 'Brand identity',
  'Brand Identity Design | Freedom Works',
  'Brand identity that makes your brand unmistakable: rebrands, naming, visual identity, and guidelines, from senior designers handpicked for your brief.',
  'Brand <em>identity</em>',
  'Once you know what your brand stands for, you have to look and sound like it. We create the name, the identity, the voice, and the visual world that make a brand unmistakable, and the guidelines that keep it this way, wherever it shows up.',
  'The name, the look, and the voice that make a brand unmistakable.',
  'Talk to us about brand identity',
  ['A brand identity is a promise you can see. Get it right and people know it’s you before they read a word.',
   'We build identities from the strategy up, so every choice, from the name to the typeface to the tone of voice, has a reason behind it. Then we test it in the real world: on pack, on screen, in a store, in a social feed.',
   'Our designers have built identities for global household names and fast growing challengers, and every project gets a senior team handpicked from The Guild for that brief.'],
  [('Discover', 'What the brand needs to say, who it needs to reach and what it’s up against.'),
   ('Explore', 'Distinct creative territories, tested early with the people who matter.'),
   ('Craft', 'The chosen direction, refined into a system: name, marque, type, colour, voice.'),
   ('Equip', 'Guidelines and tools that let every team use the identity well.')],
  ['brompton'], ['rowse-honey', 'snowfox-group'],
  [('98th', 'Percentile brand power', 'Rowse Honey'), ('+24%', 'New customers', 'Rowse Honey'), ('2,315', 'Lions, Pencils, and Effies', 'Won by the talent in The Guild')],
  [('What is a brand identity?', 'A brand identity is everything that makes a brand recognisable: its name, logo, typography, colour, imagery, tone of voice, and the rules that hold them together.'),
   ('How is brand identity different from branding?', 'Branding is the whole process of shaping how people see a brand. The identity is the visible and verbal expression of it: what people actually see, read, and hear.'),
   ('Do you create tone of voice too?', 'Yes. Verbal identity is part of every identity we build, from naming to the tone of voice that runs through every headline and help page.'),
   ('How long does a brand identity project take?', 'It depends on the scope, from a refresh to a full rebrand. We work in clear stages with decision points, so you always know what comes next.')],
  ['identity', 'design', 'brand', 'visual'], '4,890',
  extra_caps=[('Tone of voice', 'How your brand sounds, in a voice your whole team can write in.')])
REBRAND = page('services/brand-identity/brand-development-and-rebranding/', 3, 'Brand development and rebranding',
  'Rebranding and Brand Development | Freedom Works',
  'Rebranding and brand development that keeps what people love and fixes what holds you back, from senior strategists and designers worldwide.',
  'Brand development <em>and rebranding</em>',
  'A rebrand should make a brand more itself, not less. We work out what people love and what holds the brand back, then build an identity that keeps the equity, fixes the problems, and gives the business room to grow.',
  'Keep what people love. Fix what holds the brand back.',
  'Talk to us about a rebrand',
  ['The best rebrands feel inevitable afterwards. The worst throw away years of recognition for something that looks like everyone else.',
   'We start by finding the brand’s real equity: the colours, shapes, words, and memories people already connect with it. Then we decide what to keep, what to evolve, and what to retire, and test the new direction before anything launches.',
   'It’s how we repositioned Rowse Honey as the purpose led choice in its category, with bee welfare at its heart.'],
  [('Audit', 'What people recognise, what they value, and what’s getting in the way.'),
   ('Decide', 'What to keep, what to evolve, and what to retire.'),
   ('Design', 'The new identity, built from the brand’s real equity.'),
   ('Launch', 'A rollout plan that brings customers and staff with you.')],
  ['rowse'], ['rowse-honey', 'brompton'],
  [('+24%', 'New customers', 'Rowse Honey'), ('98th', 'Percentile brand power', 'Rowse Honey'), ('50th', 'Anniversary film', 'Brompton')],
  [('When should a brand rebrand?', 'Usually when the business has changed, the audience has moved on, or the identity no longer helps you stand out. A good rebrand starts with that reason, not with a new logo.'),
   ('What’s the difference between a refresh and a rebrand?', 'A refresh evolves what you have: sharper type, cleaner colour, updated imagery. A rebrand can change the name, the positioning, and the whole identity.'),
   ('How do you protect existing brand equity?', 'We research what people already recognise and value before designing anything, so the new identity builds on it rather than throwing it away.'),
   ('Can you manage the rollout too?', 'Yes. We plan the launch internally and externally, and our production teams can deliver the assets across every channel.')],
  ['rebrand', 'brand', 'identity'], '2,180', parent=IDENTITY)
NAMING = page('services/brand-identity/naming/', 3, 'Naming',
  'Brand Naming | Freedom Works',
  'Brand, product, and service names that people remember and lawyers approve: distinctive names, tested for meaning, sound, and availability.',
  'Brand <em>naming</em>',
  'A name is the first piece of your brand anyone meets, and the hardest to change. We create names for companies, products, and services that are distinctive, easy to say, and right for the story you want to tell.',
  'Names people remember, and lawyers approve.',
  'Talk to us about naming',
  ['A great name does a lot of work for free. It sets expectations, opens conversations, and gets remembered.',
   'We generate many options across different creative routes, then narrow them with linguistic checks, cultural screening in your key markets and initial availability searches before you fall in love with anything.',
   'Although it can stand alone, naming typically sits inside a wider identity process, so the name, the look, and the voice are orchestrated together.'],
  [('Brief', 'What the name needs to do, and the rules it must follow.'),
   ('Create', 'Many options across distinct creative routes.'),
   ('Screen', 'Linguistic, cultural, and initial availability checks.'),
   ('Choose', 'A shortlist presented in context, ready for legal clearance.')],
  ['snowfox'], ['snowfox-group', 'king-arthur-baking'],
  [('37', 'Countries in The Guild', 'For cultural and linguistic checks'), ('600+', 'Creatives, strategists, and producers', 'The Guild'), ('2,315', 'Lions, Pencils, and Effies', 'Won by the talent in The Guild')],
  [('How do you create a brand name?', 'We define what the name needs to do, explore many creative routes, then screen the strongest options for meaning, sound, cultural fit, and availability.'),
   ('Do you check trademarks?', 'We run initial availability searches so you only consider realistic options. Full legal clearance should always be done by a trademark lawyer.'),
   ('Can you name products as well as companies?', 'Yes, and naming systems for whole ranges, so new products have a clear place in the family.'),
   ('Will the name work internationally?', 'We check shortlisted names with native speakers in your key markets for meaning and pronunciation, drawing on The Guild across 37 countries and cultures.')],
  ['naming', 'name', 'brand'], '620', parent=IDENTITY)
VISUAL = page('services/brand-identity/visual-identity-and-brand-guidelines/', 3, 'Visual identity and brand guidelines',
  'Visual Identity and Brand Guidelines | Freedom Works',
  'Visual identity systems and brand guidelines that keep your brand consistent everywhere: logo, type, colour, imagery, and practical tools.',
  'Visual identity <em>and brand guidelines</em>',
  'We design visual identity systems, from logo and typography to colour, imagery, and motion, and the brand guidelines that keep them consistent across every team, agency, and market. Guidelines people actually use, not a PDF that gathers dust.',
  'A visual system, and the guidelines that keep it right.',
  'Talk to us about visual identity',
  ['A visual identity is a system, not a logo. It has to work on a billboard, a phone screen, a pack, and a slide.',
   'We design every part to work together, then document it in guidelines built for the people who use them: clear rules, real examples, templates, and assets, in formats your teams can open.',
   'The best guidelines leave room for creativity. Ours show what’s fixed, what’s flexible, and how to make great work within the system.'],
  [('Foundations', 'Logo, type, colour, and layout, designed as one system.'),
   ('Expression', 'Imagery, motion, and tone that bring the system to life.'),
   ('Guidelines', 'Clear rules and real examples, in usable formats.'),
   ('Tools', 'Templates and assets that make the right thing easy.')],
  ['snowfox'], ['rowse-honey', 'snowfox-group'],
  [('98th', 'Percentile brand power', 'Rowse Honey'), ('37', 'Countries in The Guild', 'The Guild'), ('600+', 'Creatives, strategists, and producers', 'The Guild')],
  [('What are brand guidelines?', 'Brand guidelines are the rules and tools that keep a brand consistent: how to use the logo, type, colour, imagery, and tone of voice, with real examples.'),
   ('What does a visual identity include?', 'Typically a logo, typography, colour palette, photography, and illustration style, layout principles, iconography, and motion.'),
   ('Can you create guidelines for an existing identity?', 'Yes. We often document and tighten up identities that have grown inconsistent over time.'),
   ('What format do the guidelines come in?', 'Whatever your teams will actually use: an online brand hub, a PDF, design-tool libraries, and templates for decks and social.')],
  ['visual', 'guidelines', 'identity', 'design'], '330', parent=IDENTITY)
IDENTITY['children'] = [REBRAND, NAMING, VISUAL]

# ---------------- CREATIVE ----------------
CREATIVE = page('services/creative/', 2, 'Creative',
  'Creative Campaigns and Content | Freedom Works',
  'Creative campaigns and content that move the numbers: brand platforms, launches, social, and creator work, from 600+ award winning creatives.',
  'Creative <em>campaigns and content</em>',
  'Your next brand platform. The socially native work you’re not getting from your agency of record. A difficult brief that needs fresh eyes. We develop ideas with the breadth to span channels and cultures, made by senior creatives handpicked for your brief.',
  'Ideas that span channels and cultures, and move the numbers.',
  'Talk to us about creative',
  ['Creative work should move the numbers a board cares about: sales, share, demand, and value.',
   'We start with the business problem, find the idea that solves it and build it to work everywhere your audience is: TV, out of home, social, creators, retail, and live.',
   'It’s the thinking behind Keep Rising for King Arthur Baking, Locos for Low Cost for Wizz Air and Magic Really Does Sell for M&S Food.'],
  [('Brief', 'The business problem, and what success looks like.'),
   ('Idea', 'One big idea with the breadth to span channels.'),
   ('Build', 'Campaigns, content, and assets for every channel.'),
   ('Learn', 'Measure what works, then make it work harder.')],
  ['lh_al'], ['king-arthur-baking', 'wizz-air'],
  [('2x', 'Sales uplift', 'King Arthur Baking'), ('+11.4%', 'Demand, year on year', 'Wizz Air'), ('+10.2%', 'Sales', 'M&S Food')],
  [('What does a creative agency do?', 'It turns a business problem into ideas people notice and act on, then makes them into campaigns and content across every channel.'),
   ('Do you work alongside our agency of record?', 'Yes. We’re often brought in for a specific brief, a fresh perspective or socially native work, alongside existing agencies.'),
   ('Can you deliver integrated, multi-channel campaigns?', 'Yes. Every idea is built to work across channels, and our production teams can make it for every format and market.'),
   ('How quickly can you start?', 'Fast. Because we handpick teams from The Guild for each brief, we can assemble the right people within days.')],
  ['creative', 'campaign', 'advertising', 'content'], '13,990',
  extra_caps=[('Integrated and multi-channel campaigns', 'One idea, built to work across every channel.'), ('Creative platforms and advertising concepts', 'Big ideas with years of life in them.'), ('Content ideas', 'Always on ideas that keep the brand present between campaigns.'), ('Creative sprints', 'A senior team on a tough brief, fast.')])
CREATOR = page('services/creative/creator-and-influencer/', 3, 'Creator and influencer',
  'Creator and Influencer Marketing | Freedom Works',
  'Creator and influencer campaigns that feel native, not bought: the right creators, real ideas, and content that performs, from strategy to production.',
  'Creator <em>and influencer</em> marketing',
  'People trust people more than brands. We find the creators your audience already listens to, build ideas they’re proud to make, and produce content that feels native to every platform, so it earns attention rather than interrupting it.',
  'The right creators, real ideas, and content that feels native.',
  'Talk to us about creator campaigns',
  ['Creator work fails when brands buy reach and script the life out of it. It works when creators have a real idea to run with.',
   'We match brands with creators on audience, values and craft, not just follower count, then develop formats that give them room to be themselves while staying on brief.',
   'As client demand grows, The Guild is being joined by a new generation of social native creators and AI artists.'],
  [('Find', 'Creators chosen for audience, values, and craft.'),
   ('Shape', 'Ideas and formats that give creators room to play.'),
   ('Make', 'Content produced to platform native standards.'),
   ('Measure', 'Reach, engagement, and what it did for the brand.')],
  [], [],
  [('600+', 'Creatives, strategists, and producers', 'The Guild'), ('37', 'Countries and cultures', 'The Guild'), ('2,315', 'Lions, Pencils, and Effies', 'Won by the talent in The Guild')],
  [('What is creator marketing?', 'Working with creators to make content for your brand that their audience actually wants to watch, rather than ads placed around it.'),
   ('How do you choose creators?', 'On audience fit, values, and the quality of their work, not just follower numbers. We vet every creator before recommending them.'),
   ('Do you handle contracts and usage rights?', 'Yes. We manage briefing, contracts, usage rights, and approvals so the work is safe to run.'),
   ('Can creator content run as paid media?', 'Yes. We plan for paid usage from the start, so the best performing content can be amplified.')],
  ['creator', 'influencer', 'social'], '3,030', parent=CREATIVE)
LAUNCH = page('services/creative/brand-and-product-launches/', 3, 'Brand and product launches',
  'Brand and Product Launch Campaigns | Freedom Works',
  'Brand and product launch campaigns that make an entrance: launch strategy, the big idea, and every asset you need to land it.',
  'Brand <em>and product launches</em>',
  'You only launch once. We plan and create launch campaigns for new brands, products, and services, from the strategy, and the big idea to every asset you need, so the market notices and the momentum carries on after launch day.',
  'Launch campaigns that make an entrance, and keep the momentum.',
  'Talk to us about a launch',
  ['A launch is a story with a deadline. Everything has to be ready, and it has to be worth talking about.',
   'We define who the launch is for and what it needs to make them do, then create the idea and build the campaign across every channel, timed to land together.',
   'For Brompton’s 50th anniversary, we launched forward rather than looking back, with a film that marked the moment.'],
  [('Plan', 'Audience, objective, and the launch moment.'),
   ('Create', 'The idea that makes the launch worth talking about.'),
   ('Build', 'Every asset, for every channel and market.'),
   ('Sustain', 'The follow-up that turns a launch into momentum.')],
  ['brompton'], ['brompton', 'wizz-air'],
  [('17', 'Broadcast ready assets in three weeks', 'Wizz Air'), ('+11.4%', 'Demand, year on year', 'Wizz Air'), ('50th', 'Anniversary film', 'Brompton')],
  [('What makes a successful launch campaign?', 'A clear audience, one idea worth talking about, and every channel landing together, followed by a plan to keep the momentum going.'),
   ('How far ahead should we start?', 'As early as possible. Ideally the launch idea and the product are developed together, but we can also move fast on tight timelines.'),
   ('Do you launch in multiple markets?', 'Yes. We build ideas that travel and adapt them for each market with local talent from The Guild.'),
   ('Can you produce everything for launch?', 'Yes. Our production teams make the film, photography, design, and digital assets in-house or alongside yours.')],
  ['launch', 'product', 'brand'], '750', parent=CREATIVE)
SOCIAL = page('services/creative/digital-and-social-creative/', 3, 'Digital and social creative',
  'Digital and Social Creative | Freedom Works',
  'Socially native creative that earns attention in the feed: platform first ideas, always on content, and social campaigns that perform.',
  'Digital <em>and social creative</em>',
  'Most brand work is still made for TV and cut down for social. We start with the feed. Platform native ideas, always on content, and social campaigns made by creatives who live on these platforms, built to earn attention, not interrupt it.',
  'Platform first ideas that earn attention in the feed.',
  'Talk to us about social creative',
  ['On social, you have a second to earn the next three. This needs ideas made for the platform, not adapted to it.',
   'We create for how people actually use each platform: the formats, the sound, the pace, and the culture, with social native creators and AI artists alongside traditional creatives.',
   'It’s how we helped loveholidays turn performance marketing into brand building, with +72% consideration and a 42% lower cost per click.'],
  [('Listen', 'What your audience watches, shares, and talks about.'),
   ('Create', 'Platform native ideas and formats.'),
   ('Produce', 'Content at the speed and volume social needs.'),
   ('Optimise', 'Test, learn, and scale what performs.')],
  ['lh_gemma'], ['loveholidays', 'wizz-air'],
  [('+72%', 'Consideration', 'loveholidays'), ('–42%', 'Cost per click', 'loveholidays'), ('+15pts', 'Awareness', 'loveholidays')],
  [('What is socially native creative?', 'Work made for how people use each platform, in its formats, pace, and culture, rather than TV ads cut down to fit.'),
   ('Do you make always on content?', 'Yes. We create content systems that keep the brand present between campaigns, without losing quality.'),
   ('Which platforms do you work on?', 'All the major ones, including TikTok, Instagram, YouTube, LinkedIn, and emerging platforms, chosen by where your audience actually is.'),
   ('Can social creative drive performance?', 'Yes. Good creative is the biggest lever in paid social; we build and test it to improve results.')],
  ['social', 'digital', 'content', 'platform'], '430', parent=CREATIVE)
CAMPAIGN = page('services/creative/campaign-strategy-and-development/', 3, 'Campaign strategy and development',
  'Campaign Strategy and Development | Freedom Works',
  'Campaign strategy and development, from the first brief to global and local rollout: one idea, built to work across channels and markets.',
  'Campaign <em>strategy and development</em>',
  'Great campaigns are planned, not just made. We develop the strategy behind the idea, build it into a campaign that works across channels, and adapt it for global and local markets, so every execution pulls in the same direction.',
  'One idea, planned to work across channels and markets.',
  'Talk to us about a campaign',
  ['A campaign is only as strong as the thinking under it. Without it, even great executions pull in different directions.',
   'We define the audience, the message, and the moments that matter, then develop the idea into a campaign framework that every channel and market can use, with room for local relevance.',
   'For Wizz Air, that meant the airline’s first fully AI powered campaign: 17 broadcast ready assets in three weeks.'],
  [('Strategy', 'Audience, message, and the moments that matter.'),
   ('Idea', 'The campaign idea and how it travels.'),
   ('Framework', 'Rules and assets for every channel and market.'),
   ('Rollout', 'Global consistency, local relevance.')],
  ['tui'], ['wizz-air', 'ms-food'],
  [('17', 'Broadcast ready assets in three weeks', 'Wizz Air'), ('+11.4%', 'Demand, year on year', 'Wizz Air'), ('+10.2%', 'Sales', 'M&S Food')],
  [('What is campaign strategy?', 'The plan behind a campaign: who it’s for, what it needs to change, the message, and where and when it should run.'),
   ('Do you run global and local campaigns?', 'Yes. We build ideas that travel, then adapt them with local talent from The Guild across 37 countries and cultures.'),
   ('How do you measure a campaign?', 'We agree measures of success up front, from brand metrics to sales, and build them into the plan.'),
   ('Can you work with our media agency?', 'Yes. We work alongside media partners so the creative and the media plan pull in the same direction.')],
  ['campaign', 'strategy', 'global'], '190 (+140 global and local)', parent=CREATIVE)
CREATIVE['children'] = [CREATOR, LAUNCH, SOCIAL, CAMPAIGN]

# ---------------- PRODUCTION ----------------
PRODUCTION = page('services/production/', 2, 'Production',
  'Creative Production for Brands | Freedom Works',
  'Creative production for brands: film and video, design, post-production, and virtual and AI production. One great idea, built into every asset you need.',
  'Creative <em>production</em>',
  'Give the idea the craft it deserves. We bring campaigns and content to life across channels and markets, through us or alongside your existing production team. Film and video, design, post-production, and virtual and AI production: one great idea, built into every asset, format, and market it needs.',
  'Film, design, post-production, and virtual and AI production.',
  'Talk to us about production',
  ['Big ideas shouldn’t need big budgets to get made.',
   'Our AI artists and virtual production specialists work alongside traditional crews, so we can choose the right way to make every piece: live action where it matters, AI and virtual production where they make the work better, faster, or more affordable.',
   'And with our global content amplification partner, we deliver scaled brilliance: one great idea, built out into every asset, format, and market it needs.'],
  [('Plan', 'The right production approach for every asset.'),
   ('Make', 'Live action, virtual and AI production, side by side.'),
   ('Finish', 'Edit, grade, sound, VFX, and motion.'),
   ('Scale', 'Every format, size, and market, ready to run.')],
  ['ka'], ['wizz-air', 'king-arthur-baking'],
  [('17', 'Broadcast ready assets in three weeks', 'Wizz Air'), ('+100%', 'Sales uplift', 'King Arthur Baking'), ('+10.2%', 'Sales', 'M&S Food')],
  [('What does a creative production agency do?', 'It turns creative ideas into finished films, photography, design, and digital assets, managing crews, talent, post-production, and delivery.'),
   ('Do you use AI in production?', 'Where it makes the work better, faster, or more affordable. Our AI artists work alongside traditional crews, and every piece is directed and finished by people.'),
   ('Can you produce content at scale?', 'Yes. With our global content amplification partner, we adapt one idea into every asset, format and market you need.'),
   ('Can you work with our production team?', 'Yes. We can run production end to end or work alongside your existing production team.')],
  ['production', 'film', 'content', 'ai'], '4,430',
  extra_caps=[('Content at scale', 'One idea, adapted into every asset, size, and market.'), ('Digital and social assets', 'Platform ready versions of every piece, built to perform.'), ('Campaign production', 'End to end production for integrated campaigns.')])
def prod(slug, name, title, desc, h1, intro, line, cta, about, process, quotes, cases, stats, faqs, keywords, volume):
    return page(f'services/production/{slug}/', 3, name, title, desc, h1, intro, line, cta, about, process, quotes, cases, stats, faqs, keywords, volume, parent=PRODUCTION)
FILM = prod('film-and-video', 'Film and video',
  'Film and Video Production for Brands | Freedom Works',
  'Film and video production for brands: commercials, brand films, and social content, made by award winning directors and crews worldwide.',
  'Film <em>and video production</em>',
  'From TV commercials to brand films and social content, we make film that people want to watch. Award winning directors and crews, handpicked for each project, with AI and virtual production on hand when they make the work better.',
  'Commercials, brand films, and social content people want to watch.',
  'Talk to us about film production',
  ['Film is still the most powerful way to make people feel something about a brand.',
   'We match every script with the right director and crew from our global network, plan the shoot around the idea and finish everything in post, from the hero film to every cut down and format.',
   'It’s how we made Keep Rising for King Arthur Baking and Life Unfolded for Brompton, and shot loveholidays’ At Your Fingertips on location in Unreal Engine.'],
  [('Treatment', 'The right director and approach for the script.'),
   ('Pre-production', 'Casting, locations, crews, and a shoot plan.'),
   ('Shoot', 'Live action, virtual, or AI, chosen for the idea.'),
   ('Post', 'Edit, grade, sound, and every cut down.')],
  ['brompton'], ['brompton', 'loveholidays'],
  [('+100%', 'Sales uplift', 'King Arthur Baking'), ('+72%', 'Consideration', 'loveholidays'), ('50th', 'Anniversary film', 'Brompton')],
  [('What kind of films do you make?', 'TV and cinema commercials, brand films, online video, social content, and internal films.'),
   ('Do you work with external directors?', 'Yes. We handpick directors and crews for each project from our global network and production partners.'),
   ('Can you deliver every format we need?', 'Yes. We plan cut downs and formats from the start so every channel gets a version made for it.'),
   ('How much does a brand film cost?', 'It depends on the idea, talent, and locations. We give you options at different budgets, including virtual and AI production routes.')],
  ['film', 'video', 'production'], '15,880')
PHOTO = prod('photography', 'Photography',
  'AI and Commercial Photography for Brands | Freedom Works',
  'AI and commercial photography for brands: AI-generated and AI-extended imagery alongside real shoots, crafted to your brand for every channel.',
  'AI and commercial <em>photography</em>',
  'We make brand imagery two ways, and usually both at once. AI artists generate and extend imagery at a speed and scale no shoot can match, and photographers handpicked for each brief capture the moments that need to be real. Everything is crafted to your brand and delivered in every crop and format.',
  'AI and camera imagery, crafted to your brand.',
  'Talk to us about photography',
  ['AI has changed what a photo shoot can be. One shoot can now become a whole campaign.',
   'Our AI artists build product shots, settings, and whole campaigns from scratch, or extend a real shoot into new locations, seasons and formats, all crafted to your brand, and checked by people.',
   'Where a moment needs to be real, we cast, style, and shoot it, with photographers handpicked from our global network.'],
  [('Direction', 'Art direction, mood, and the shot list, for AI, and camera.'),
   ('Generate', 'AI imagery built and extended to your brand.'),
   ('Shoot', 'Real moments, cast and styled, where they matter.'),
   ('Finish', 'Retouching and quality checks, in every crop and format.')],
  ['ka'], ['king-arthur-baking', 'rowse-honey'],
  [('+100%', 'Sales uplift', 'King Arthur Baking'), ('+24%', 'New customers', 'Rowse Honey'), ('37', 'Countries in The Guild', 'Photographers worldwide')],
  [],
  ['photography', 'photo', 'image', 'ai'], '7,640')
DESIGN = prod('design', 'Design',
  'Brand Design Services | Freedom Works',
  'Design for brands: campaign design, packaging, print, digital, and retail, crafted by senior designers handpicked for your brief.',
  'Brand <em>design</em>',
  'Campaign design, packaging, print, digital, and retail, crafted by senior designers handpicked for your brief. We make every touchpoint look like it belongs to the same brand, and like nobody else’s.',
  'Campaign, packaging, print, digital, and retail design.',
  'Talk to us about design',
  ['Design is where a brand becomes real: the pack in your hand, the poster on the platform, the page on your phone.',
   'Our designers work from the brand system and the campaign idea, crafting every piece by hand where it matters and building flexible templates where volume does.',
   'For Rowse Honey, design helped reposition the brand as the purpose led choice on shelf.'],
  [('Brief', 'The job each piece has to do.'),
   ('Design', 'Concepts crafted to the brand system.'),
   ('Refine', 'Detail, typography, and production ready files.'),
   ('Systemise', 'Templates for the pieces you’ll make again.')],
  ['mayfair'], ['rowse-honey', 'snowfox-group'],
  [('+24%', 'New customers', 'Rowse Honey'), ('98th', 'Percentile brand power', 'Rowse Honey'), ('600+', 'Creatives, strategists, and producers', 'The Guild')],
  [('What design services do you offer?', 'Campaign design, packaging, print, retail, digital, and presentation design, built on your brand system.'),
   ('Do you design packaging?', 'Yes, from new packs to range refreshes, including artwork-ready files.'),
   ('Can you create design templates?', 'Yes. We build templates for social, presentations, and campaigns so your team can make on-brand work quickly.'),
   ('Do you offer design support on demand?', 'Yes. See In-house creative for ongoing design support alongside your team.')],
  ['design', 'packaging'], '4,310')
VIRTUAL = prod('virtual-production', 'Virtual production',
  'Virtual Production for Brands | Freedom Works',
  'Virtual production for brand films and content: real time environments and LED volumes that create any location in the studio.',
  'Virtual <em>production</em>',
  'Shoot anywhere without leaving the studio. Virtual production combines real time 3D environments, LED volume walls, and traditional filmmaking, so big ideas can go anywhere, on budgets and timelines that make sense.',
  'Real time environments that take the shoot anywhere.',
  'Talk to us about virtual production',
  ['Some ideas need a desert, a city at night, or a world that doesn’t exist. Virtual production makes them possible without the travel.',
   'Our virtual production specialists work alongside directors and crews from previsualisation to on set supervision, building environments that look real on camera and give actors something real to react to.',
   'The latest loveholidays campaign was shot entirely this way, with every location built in Unreal Engine. And the light, the weather, and the time of day are all decisions, not risks.'],
  [('Previs', 'Plan the shots and build the world.'),
   ('Build', 'Real time 3D environments, ready for camera.'),
   ('Shoot', 'LED volume or green screen with live playback.'),
   ('Finish', 'Compositing, grade, and delivery.')],
  ['lh_al'], ['loveholidays', 'tui'],
  [('+72%', 'Consideration', 'loveholidays'), ('\u201342%', 'Cost per click', 'loveholidays'), ('+15pts', 'Awareness', 'loveholidays')],
  [('What is virtual production?', 'Filmmaking that uses real time 3D environments, often displayed on LED walls, so scenes can be shot in camera without travelling to locations.'),
   ('Is virtual production cheaper?', 'It can be, especially for multiple or hard-to-reach locations. We compare it with a traditional shoot for every project.'),
   ('What projects suit virtual production?', 'Anything with multiple locations, impossible settings, tight timelines, or a need for precise control of light and weather.'),
   ('Can you combine it with live-action and AI?', 'Yes. We choose the best way to make each shot, and often mix all three.')],
  ['virtual', 'production'], '870')
POST = prod('post-production', 'Post-production',
  'Post-Production for Brands | Freedom Works',
  'Post-production for brand films and content: edit, colour, sound, VFX, motion graphics, and versioning for every format and market.',
  'Post-<em>production</em>',
  'Post-production is where the film is really made. Editing, colour, sound design, VFX, motion graphics, and versioning, finished to broadcast standard by specialists handpicked for each project, and delivered in every format and market you need.',
  'Edit, colour, sound, VFX, and versioning for every format.',
  'Talk to us about post-production',
  ['The edit is where a film finds its rhythm, and the finish is what makes it feel premium.',
   'We bring together editors, colourists, sound designers, and VFX artists for each project, and plan versioning from the start so every cut down and language version is as good as the hero.',
   'Our AI workflows speed up versioning and adaptation, with every frame checked by people.'],
  [('Edit', 'Shape the story and the rhythm.'),
   ('Finish', 'Colour, sound, and VFX.'),
   ('Version', 'Cut downs, ratios, and languages.'),
   ('Deliver', 'Broadcast and platform ready files.')],
  ['brompton'], ['loveholidays', 'brompton'],
  [('+72%', 'Consideration', 'loveholidays'), ('50th', 'Anniversary film', 'Brompton'), ('+24%', 'New customers', 'Rowse Honey')],
  [('What does post-production include?', 'Editing, colour grading, sound design and mixing, VFX, motion graphics, versioning, and delivery.'),
   ('Can you post-produce footage we shot elsewhere?', 'Yes. We can take on post for footage from any shoot.'),
   ('Do you create versions for different markets?', 'Yes, including subtitles, voiceovers, end frames, and legal versions for each market.'),
   ('How fast can you turn around edits?', 'It depends on the scope; social cut downs can take days, a full campaign longer. We plan it with you up front.')],
  ['post', 'edit', 'vfx'], '330')
AI = prod('ai-production', 'AI production',
  'AI Production for Brands | Freedom Works',
  'AI production for brands: AI-generated film, imagery, and content at scale, directed and finished by award winning creatives.',
  'AI <em>production</em>',
  'We use AI where it makes the work better, faster, or more affordable, and not where it doesn’t. Our AI artists work alongside directors, designers, and editors to make film, imagery, and content at a speed and scale traditional production can’t match.',
  'AI made film, imagery, and content, directed by humans.',
  'Talk to us about AI production',
  ['AI changes how work gets made, not who it’s for. Taste and judgement matter more than ever.',
   'Our AI artists combine generative tools with traditional craft, from concept development and previs to finished film and imagery, with every piece directed, checked, and finished by people.',
   'For Wizz Air, that meant the airline’s first fully AI powered campaign: 17 broadcast ready assets in three weeks.'],
  [('Explore', 'AI assisted concepts and previs, fast.'),
   ('Direct', 'A creative lead for every AI project.'),
   ('Produce', 'Film, imagery, and content, generated and crafted.'),
   ('Finish', 'Human idea first, then post-production and QA.')],
  ['lh_al'], ['wizz-air', 'tui'],
  [('17', 'Broadcast ready assets in three weeks', 'Wizz Air'), ('+11.4%', 'Demand, year on year', 'Wizz Air'), ('600+', 'Creatives, strategists, and producers', 'The Guild')],
  [('What is AI production?', 'Using generative AI tools to create or extend film, imagery and content, directed, and finished by creative professionals.'),
   ('Is AI production safe for brands?', 'We use commercially licensed tools, check every output for quality and rights, and follow your brand and legal guidelines.'),
   ('Will AI replace your creatives?', 'No. AI speeds up making; ideas, taste, and judgement still come from people, which is why our AI artists work inside creative teams.'),
   ('Can AI production match broadcast quality?', 'For the right projects, yes. Wizz Air’s campaign delivered 17 broadcast ready assets in three weeks.')],
  ['ai', 'artificial', 'generative'], '100 (growing)')
PRODUCTION['children'] = [FILM, DESIGN, VIRTUAL, POST, AI]   # Photography removed: not a core service

# ---------------- IN-HOUSE AUGMENTATION ----------------
INHOUSE = page('services/in-house/', 2, 'In-house creative',
  'In-House Creative Support and Direction | Freedom Works',
  'Senior creative direction, strategy, and design support for in-house teams, on demand or embedded, from 600+ award winning creatives.',
  'In-house <em>creative</em>',
  'Boost your in-house team with freshness and firepower, on demand or embedded. We put award winning creative directors, strategists, and designers alongside your team within days, to crack briefs, develop campaigns, and strengthen design, so your team earns its place as a strategic partner.',
  'Senior creative firepower for in-house teams.',
  'Talk to us about in-house support',
  ['Many in-house teams carry a negative trust equity with the business they’ve served for years. Fresh senior talent changes that conversation.',
   'Through our plug and play services built for in-house agencies, we add creative direction, strategy, and design capacity exactly where you need it, for a single brief or as ongoing support. We can also give you strategy on demand over WhatsApp.',
   'M&S Food’s Christmas campaign was made with M&S Food’s in-house team, and SMA Baby Club with Nestlé’s Content Studio.'],
  [('Diagnose', 'Where your team needs support, and why.'),
   ('Match', 'Senior talent handpicked from The Guild.'),
   ('Embed', 'Working alongside your team, in your tools.'),
   ('Elevate', 'Stronger work, and a stronger in-house reputation.')],
  ['nestle_ih'], ['ms-food', 'nestle-sma'],
  [('+10.2%', 'Sales', 'M&S Food'), ('2x', 'Baby Club sign-ups', 'Nestlé SMA'), ('600+', 'Creatives, strategists, and producers', 'The Guild')],
  [('What is in-house creative support?', 'Adding senior external talent to an in-house creative team, for a single brief or ongoing, without replacing the team.'),
   ('Can you provide a creative director for our team?', 'Yes. We can place an award winning creative director with your team, for a single campaign or an ongoing role.'),
   ('How quickly can someone start?', 'Usually within days. We handpick talent from The Guild to match your brief and your team.'),
   ('Do you offer creative mentoring?', 'Yes. Our senior creatives mentor in-house teams to build skills and confidence that last after we leave.')],
  ['in-house', 'creative direction', 'team'], '10 (creative direction 2,940)',
  extra_caps=[('Creative direction', 'Award winning creative directors for a brief or an ongoing role.'), ('Strategic projects', 'Senior strategy for the briefs that matter most.'), ('Design projects', 'Extra design capacity, crafted to your brand system.'), ('Creative mentoring', 'Building your team’s skills and confidence.'), ('Ongoing creative support', 'Always on creative capacity, as and when you need it.'), ('Production excellence', 'Production expertise to raise the craft of every piece.')])
INHOUSE['children'] = []

SERVICE_PAGES = [BRAND_STRATEGY, POSITIONING, COMMS, ARCHITECTURE,
                 IDENTITY, REBRAND, NAMING, VISUAL,
                 CREATIVE, CREATOR, LAUNCH, SOCIAL, CAMPAIGN,
                 PRODUCTION, FILM, DESIGN, VIRTUAL, POST, AI,
                 INHOUSE]
LEVEL2 = [BRAND_STRATEGY, IDENTITY, CREATIVE, PRODUCTION, INHOUSE]


import re as _re
def _now_fw(t):
    return _re.sub(r'\b(The Liberty Guild|Liberty Guild)(\u2019s)?(?! \[now)', lambda m: m.group(1) + ' [now Freedom Works]' + (m.group(2) or ''), t, count=1)
Q = {k: (_now_fw(v[0]),) + tuple(v[1:]) for k, v in Q.items()}


# ---------------- Copy deck v2 (28 Oct): testimonials, proof and copy from the copywriters ----------------
# Added after the "[now Freedom Works]" step above, because these quotes already carry "[formerly The Liberty Guild]".
Q.update({
    'gsk_v2': ("In a sea of sameness, Freedom Works [formerly The Liberty Guild] is a breath of fresh air. A thoroughly modern, no-nonsense approach to applied strategic creative thinking.", 'Nick Tate', 'ex VP, Head of Next, Haleon plc'),
    'lh_al_v2': ("Since starting our brand journey with Freedom Works [formerly The Liberty Guild], we\u2019ve added nearly 15% pts of awareness and seen every brand metric we track increase at pace, while our competitors are flat or falling - all despite dramatically lower brand budgets.", 'Al Murray', 'CMO, loveholidays'),
    'snowfox_v2': ("You [Freedom Works] delivered brilliantly throughout, provided amazing creativity and moral support and (most importantly) you were great fun to work with.", 'Simon Clough', 'Strategic Brand Consultant, Snowfox Group'),
    'snowfox_plain': ("You delivered brilliantly throughout, provided amazing creativity and moral support and (most importantly) you were great fun to work with.", 'Simon Clough', 'Strategic Brand Consultant, Snowfox Group'),
    'brompton_v2': ("We were looking for a partner who truly understood the spirit of Brompton, not just as a mode of transport, but as a way of moving through life with freedom, creativity, and purpose. The Liberty Guild\u2019s fresh, unique global model and deep cultural insight made them the perfect fit to help us inspire a new wave of riders around the world.", 'Chris Willingham', 'Global CMO, Brompton'),
    'rowse_v2': ("The most integrated model I have seen when it comes to creative development. And yet it is so obvious that if you embed the consumer into the creative development process and are guided by the data and not the creative ego you are going to get better, more effective work.", 'Kirstie Jamieson', 'ex Marketing Director, Rowse Honey'),
    'ka_v2': ("Keep Rising has been transformative for King Arthur Baking. Not just creatively, but commercially. In a low interest category, The Guild helped us connect on a deeper emotional level. They captured our brand\u2019s purpose with humanity and craft, and the results speak for themselves: record market share, millions of new households, and the highest repeat rate in the category. Working with Freedom Works [previously The Liberty Guild] feels genuinely different. They bring strategic clarity, creative excellence, and a genuine partnership that makes the work, and the brand, rise higher.", 'Kim Stellavato', 'Senior Brand Director, King Arthur Baking'),
    'gemma_v2': ("What\u2019s great about their [Freedom Works] offering is the global reach of their network. The ability to tap into creatives and strategists from across the globe whilst still having the expert support of a centrally managed account team gives us the best of both worlds.", 'Gemma Schmid', 'ex-Director of Brand Marketing, loveholidays'),
    'tui_v2': ("Freedom Works [formerly The Liberty Guild] have been a delight to work with. Their interpretation and understanding of our brief helped crystallise the strategic approach, which then went on to create work that brought to life the proposition in a way that will allow us to flex across markets.", 'Rachel Moss', 'Head of International Marketing, TUI Group'),
    'wizz_v2': ("Locos is about letting go, embracing spontaneity, and leaning into life\u2019s fun side. Because low cost isn\u2019t only about saving money, it\u2019s about having the freedom to do more and live bigger. Wizz Air has, from its inception, been a digital-first company, so it makes sense that we would be at the leading edge of using new technology in all areas of our business. So making an all AI ad just made sense. Let\u2019s WIZZ!", 'Silvia Mosquera Gonz\u00e1lez', 'Commercial Officer Central, Wizz Air'),
    'nixon_v2': ("I can now assemble a team through The Liberty Guild within a few days that has more Cannes Lions and D&AD Pencils within it than all of our agency accounts put together.", 'Tom Nixon', 'Head of Content Studios UK&I'),
})
BRAND_STRATEGY['quotes'] = ['gsk_v2']
POSITIONING['quotes'] = ['gsk_v2']
POSITIONING['desc'] = 'Brand positioning that finds the space your brand can own and the words to claim it. Senior strategists, handpicked for your brief.'
COMMS['quotes'] = ['lh_al_v2']
ARCHITECTURE.update(stats=[('Four', 'Brands, one unifying brand platform', 'Snowfox Group')], cases=['snowfox-group'], quotes=['snowfox_v2'])
IDENTITY['quotes'] = ['brompton_v2']
REBRAND['quotes'] = ['rowse_v2']
NAMING.update(cases=['snowfox-group'], quotes=['snowfox_plain'])
VISUAL.update(stats=[('+24%', 'New customers', 'Rowse Honey'), ('$621m', 'Acquired by Zensho', 'Snowfox Group'), ('81%', 'Of B2B decision makers thought the identity was clear and differentiated', 'Nasstar')], quotes=['snowfox_plain'])
CREATIVE['quotes'] = ['ka_v2']
CREATOR.update(about=[CREATOR['about'][0], 'We match brands with creators based on audience, values and craft, not just follower count, then develop formats that give them room to be themselves while staying on brief.'], stats=[], cases=[], quotes=[])
LAUNCH['quotes'] = ['brompton_v2']
SOCIAL['quotes'] = ['gemma_v2']
CAMPAIGN['quotes'] = ['tui_v2']
PRODUCTION.update(cases=['wizz-air'], quotes=['wizz_v2'])
DESIGN.update(about=[DESIGN['about'][0], 'Our designers develop the brand system from the creative and strategic platform, crafting every piece by hand where it matters and building flexible templates where volume requires.'],
              stats=[('$621m', 'Acquired by Zensho', 'Snowfox Group'), ('81%', 'Of B2B decision makers thought the brand was clear and differentiated', 'Nasstar'), ('600+', 'Creatives, strategists, and producers', 'The Guild')])
VIRTUAL['stats'] = [('+72%', 'Consideration', 'loveholidays'), ('\u201342%', 'Cost per click', 'loveholidays'), ('1m+', 'Added to their ATOL licence', 'loveholidays')]
POST['stats'] = [('50th', 'Anniversary brand film, Life Unfolded', 'Brompton'), ('+72%', 'Consideration', 'loveholidays'), ('+24%', 'New customers', 'Rowse Honey')]
AI['stats'] = [('17', 'Broadcast ready assets in three weeks', 'Wizz Air'), ('+11.4%', 'Demand, year on year', 'Wizz Air')]
INHOUSE['quotes'] = ['nixon_v2']

# ---------------- Client logos per page (Emmaclare, copy deck v3) ----------------
POSITIONING['logos'] = ['rowse-honey']
COMMS['logos'] = ['loveholidays']
ARCHITECTURE['logos'] = ['snowfox-group', 'haleon']
IDENTITY['logos'] = ['snowfox-group', 'nasstar', 'rowse-honey']
REBRAND['logos'] = ['rowse-honey', 'king-arthur', 'wizz-air', 'snowfox-group']
NAMING['logos'] = ['snowfox-group']
CREATIVE['logos'] = ['nestle', 'p-and-g', 'tui', 'wizz-air', 'king-arthur']
CREATOR['logos'] = []          # none: no creator work to show yet
SOCIAL['logos'] = ['wizz-air', 'tui', 'nestle']
CAMPAIGN['logos'] = ['tui', 'king-arthur', 'rowse-honey', 'wizz-air']
PRODUCTION['logos'] = ['wizz-air', 'tui', 'rowse-honey']
FILM['logos'] = ['wizz-air', 'brompton', 'rowse-honey']
DESIGN['logos'] = ['snowfox-group', 'nasstar']
INHOUSE['logos'] = ['nestle', 'm-and-s-food']
BRAND_STRATEGY['logos'] = ['rowse-honey', 'king-arthur', 'snowfox-group', 'haleon']

# ---------------- Creator and influencer: no longer its own page, listed as "Also part of creative" ----------------
CREATIVE['children'] = [LAUNCH, SOCIAL, CAMPAIGN]
CREATIVE['extra_caps'] = [c for c in CREATIVE.get('extra_caps', []) if (c[0] if isinstance(c, (tuple, list)) else c) != 'Creator and influencer'] + [('Creator and influencer', CREATOR['line'])]
SERVICE_PAGES[:] = [x for x in SERVICE_PAGES if x is not CREATOR]
LAUNCH['logos'] = ['brompton']
CAMPAIGN['logos'] = ['tui', 'king-arthur', 'rowse-honey', 'wizz-air', 'loveholidays']

# ---------------- Client logos per page (Tom, 28 Oct, final) ----------------
BRAND_STRATEGY['logos'] = ['heineken', 'tui', 'burger-king']
POSITIONING['logos'] = ['tui', 'brompton', 'rowse-honey', 'burger-king']
COMMS['logos'] = ['loveholidays', 'king-arthur', 'heineken']
ARCHITECTURE['logos'] = ['snowfox-group', 'haleon']
IDENTITY['logos'] = ['snowfox-group', 'nasstar', 'brompton']
REBRAND['logos'] = ['rowse-honey', 'king-arthur', 'wizz-air', 'snowfox-group']
NAMING['logos'] = ['snowfox-group', 'burger-king']
VISUAL['logos'] = ['snowfox-group', 'rowse-honey']
CREATIVE['logos'] = ['nestle', 'p-and-g', 'tui', 'wizz-air', 'king-arthur', 'loveholidays', 'gin-mare', 'coca-cola', 'm-and-s-food', 'pharmacy2u', 'bayer']
LAUNCH['logos'] = ['brompton', 'tui', 'rowse-honey', 'haleon']
SOCIAL['logos'] = ['wizz-air', 'tui', 'nestle', 'p-and-g', 'brown-forman', 'loveholidays']
CAMPAIGN['logos'] = ['tui', 'king-arthur', 'rowse-honey', 'wizz-air', 'loveholidays']
PRODUCTION['logos'] = ['wizz-air', 'tui', 'rowse-honey', 'loveholidays', 'brompton', 'nestle', 'king-arthur']
FILM['logos'] = ['wizz-air', 'brompton', 'rowse-honey', 'nestle']
DESIGN['logos'] = ['snowfox-group', 'nasstar', 'brompton']
VIRTUAL['logos'] = ['loveholidays']
AI['logos'] = ['wizz-air', 'tui']
INHOUSE['logos'] = ['loveholidays']
