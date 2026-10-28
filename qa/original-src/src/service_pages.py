"""Service pages (SEO structure: one page per service and sub-service).

Level 2 = a service (e.g. Brand strategy). Level 3 = a sub-service under it.
Each page: breadcrumbs, keyword H1, 30-60 word intro, client logos, CTA, then
experience copy, process, sub-services, testimonials, case studies, proof stats,
FAQs, related articles and a closing CTA.

Starter copy for review. Pages are only published when SERVICE_PAGES_LIVE is True
in build.py.
"""

Q = {
    'gsk': ("In a sea of sameness, The Liberty Guild is a breath of fresh air. A thoroughly modern, no-nonsense approach to applied strategic creative thinking.", 'Nick Tate', 'VP Head of Next, GSK Consumer Healthcare'),
    'cpw': ("The quality of the healthy debates we have is a proof of the senior and highly experienced individuals behind the team, allowing us to build on each other\u2019s points of view that yield nothing but better outputs.", 'Estrella Lopez-Brea', 'Global Head of Insights, CPW'),
    'ka': ("Keep Rising has been transformative for King Arthur Baking. Not just creatively, but commercially. In a low-interest category, The Guild helped us connect on a deeper emotional level.", 'Kim Stellavato', 'Brand Director, King Arthur Baking'),
    'brompton': ("We were looking for a partner who truly understood the spirit of Brompton, not just as a mode of transport, but as a way of moving through life with freedom, creativity, and purpose.", 'Chris Willingham', 'Global CMO, Brompton'),
    'lh_al': ("Since starting our brand journey with The Liberty Guild, we\u2019ve added nearly 15%pts of awareness and seen every brand metric we track increase at pace, while our competitors are flat or falling, all despite dramatically lower brand budgets.", 'Al Murray', 'CMO, loveholidays'),
    'lh_gemma': ("What\u2019s great about their offering is the global reach of their network. The ability to tap into creatives and strategists from across the globe whilst still having the expert support of a centrally managed account team gives us the best of both worlds.", 'Gemma Schmid', 'Director of Brand Marketing, loveholidays'),
    'tui': ("Their interpretation and understanding of our brief helped crystallise the strategic approach, which then went on to create some creative work that brought to life the proposition in a way that will allow us to flex across markets.", 'Rachel Moss', 'Head of International Marketing, TUI Group'),
}

BRAND_STRATEGY = {
    'path': 'services/brand-strategy/', 'level': 2, 'name': 'Brand strategy',
    'title': 'Global Brand Strategy | Freedom Works',
    'desc': 'Global brand strategy from senior strategists in a 500+ network, handpicked for your brief: positioning, architecture and communications strategy.',
    'h1': 'Global <em>brand strategy</em>',
    'keyword': 'global brand strategy',
    'intro': 'Senior strategists, handpicked from The Guild for your brief, work out where your brand is coming from, where it needs to go and why. Then we turn it into a brand strategy the whole business can act on: a positioning, an architecture and a brief that gets the work made.',
    'line': 'Positioning, communications strategy and brand architecture.',
    'articles': ['introducing-whatstrat-senior-strategic', 'beach-reads-3-diy-strategist-how', 'in-the-agentic-era-travel-businesses'],
    'cta': 'Talk to us about brand strategy',
    'about_h': 'Strategy that <em>gets the work made</em>',
    'about': [
        'Building a new brand from scratch? Taking an existing one somewhere new? Or just buffing a dusty one up a bit? We work out where it\u2019s coming from and where it needs to go. And why.',
        'Every project gets a senior team chosen for that brief, not whoever happens to be free. Our strategists have led brand work for global networks, consultancies and in-house teams, across food and drink, travel, retail and health.',
        'Strategy here isn\u2019t a document that sits on a shelf. It\u2019s the thinking that took King Arthur Baking from the #3 to the #1 flour brand in the US, and moved loveholidays from performance marketing to brand without losing demand.',
    ],
    'process': [
        ('Diagnose', 'We audit the brand, the category and the audience, backed by qual, quant or behavioural research where it counts.'),
        ('Define', 'We decide where the brand should play and why it wins: positioning, proposition and architecture.'),
        ('Articulate', 'We turn the strategy into a platform, a story and a tone the whole business can use.'),
        ('Brief', 'We write the brief that gets the work made, and stay with it through to launch.'),
    ],
    'subs_h': 'Brand strategy <em>services</em>',
    'extra_caps': ['Strategic consultancy', 'Brand audits and roadmaps', 'Creative briefing'],
    'quotes': ['gsk', 'ka', 'cpw'],
    'cases': ['king-arthur-baking', 'loveholidays', 'rowse-honey'],
    'stats': [('+100%', 'Sales uplift', 'King Arthur Baking'), ('+72%', 'Consideration', 'loveholidays'), ('98th', 'Percentile brand power', 'Rowse Honey'), ('500+', 'Strategists, creatives and producers', 'The Guild')],
    'faqs': [
        ('What does brand strategy involve?', 'Brand strategy works out what a brand stands for, who it\u2019s for and how it wins, then turns that into a positioning, a brand architecture and a brief that creative teams can act on. At Freedom Works, that strategy is built by a senior team handpicked from The Guild for your brief.'),
        ('How long does a brand strategy project take?', 'It depends on the scope. We work in short sprints with clear decision points, so you see the thinking early and often rather than waiting months for a big reveal.'),
        ('Do you work with in-house teams?', 'Yes. We can run the whole project, or plug senior strategists into your in-house team, your agencies, or both.'),
        ('Do you only do strategy?', 'No. Strategy usually leads into brand identity, creative and production, and we can run all of it, so the thinking carries straight through into the work.'),
        ('Do you work internationally?', 'Yes. The Guild spans 37 countries, so we can build teams with the market and cultural knowledge your brief needs.'),
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
        'A strong positioning makes every other decision easier: what to say, what to make, where to show up and what to leave out. A weak one turns everything into a debate.',
        'We start with the people you need to win and the category you compete in, then look for the truth about your brand that competitors can\u2019t copy. We test it, sharpen it and write it down in language people actually use.',
        'It\u2019s how we repositioned Rowse Honey as the purpose-led choice, with bee welfare at its heart: +24% new customers and a 98th percentile brand power score.',
    ],
    'process': [
        ('Listen', 'Interviews, data and research to understand your audience, category and competitors.'),
        ('Find the gap', 'The space your brand can credibly own, and why it matters to the people you need to win.'),
        ('Frame it', 'A clear positioning statement, proposition and the reasons to believe it.'),
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
    'desc': 'Communications strategy that decides who to reach, what will move them and where. Channel-agnostic planning from a global network of senior strategists.',
    'h1': 'Communications <em>strategy</em>',
    'keyword': 'communications strategy',
    'intro': 'We decide who you need to reach, what will move them and where to say it. Channel-agnostic communications strategy that turns a brand idea into work people notice, from the first brief to the last week of the media plan.',
    'line': 'Who to reach, what will move them and where to say it.',
    'articles': ['the-generative-moment-of-truth-why', 'being-found-is-the-easy-bit', 'allnewqueue-jul2020'],
    'cta': 'Talk to us about communications strategy',
    'about_h': 'The right message, <em>in the right places</em>',
    'about': [
        'Great ideas fail when they land in the wrong place, at the wrong moment, in the wrong format. Communications strategy is how we make sure the work reaches the people it\u2019s for, in the moments they\u2019re most open to it.',
        'We\u2019re channel-agnostic. We start with the audience and the job the communication has to do, then decide what to make and where it should live: TV, out of home, social, creators, experiential, or all of them.',
        'It\u2019s how we helped loveholidays move from performance marketing to brand: +15pts awareness, +72% consideration and 42% lower cost per click.',
    ],
    'process': [
        ('Audience', 'Who we need to reach, what they believe now, and what we need them to feel, think or do.'),
        ('Message', 'The single idea and the proof points that will move them.'),
        ('Moments', 'Where and when the message will work hardest, across paid, owned, earned and shared.'),
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
    'desc': 'Brand architecture that gives every brand in your portfolio a clear job. Portfolio strategy, mergers and sub-brands from senior strategists worldwide.',
    'h1': 'Brand <em>architecture</em>',
    'keyword': 'brand architecture',
    'intro': 'We organise your brands so each one has a clear job. We untangle portfolios, merge or separate brands, and build a brand architecture that lets the business grow without confusing the people it sells to.',
    'line': 'A clear job for every brand in your portfolio.',
    'articles': ['beach-reads-6-free-aint-cheap-the', 'the-generative-moment-of-truth-why', 'in-the-agentic-era-travel-businesses'],
    'cta': 'Talk to us about brand architecture',
    'about_h': 'One clear system, <em>room to grow</em>',
    'about': [
        'Acquisitions, new products and sub-brands pile up. Before long, customers can\u2019t tell how your brands relate, teams duplicate effort, and every launch starts with an argument about naming.',
        'We map what you have, work out what each brand needs to do for the business and the customer, and design the structure that makes the whole portfolio stronger: a branded house, a house of brands, or something in between.',
        'It\u2019s how we unified four Snowfox Group sushi brands under one strategic platform, strengthening their identity and commercial performance.',
    ],
    'process': [
        ('Map', 'An audit of every brand, sub-brand and product name, and how customers actually see them.'),
        ('Model', 'Options for how the portfolio could be organised, tested against your growth plans.'),
        ('Decide', 'A clear recommendation, and the rules for using it.'),
        ('Roll out', 'Naming, identity and a plan to move from today\u2019s structure to tomorrow\u2019s.'),
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
SERVICE_PAGES = [BRAND_STRATEGY, POSITIONING, COMMS, ARCHITECTURE]
