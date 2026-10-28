# Freedom Works: design audit (Phase 1, before any edits)

Method: built with `python3 build.py` (Python 3.9), served `site/` locally and captured every template full-page at 1440, 1024, 768 and 390px in Chrome (52 screenshots in `qa/before/`; the brand-strategy service page was built with `SERVICE_PAGES_LIVE` switched on in memory only). An automated WCAG contrast sweep was run over every text node. CSS was measured for dead and conflicting rules.

The standard applied is agency-level craft (Pentagram, Collins, Koto, Mother). Items are ranked by visual impact. Each gives selector, page and breakpoint.

---

## 0. Blockers found before any design work

| # | Problem | Where | Evidence |
|---|---|---|---|
| 0.1 | **`build.py` does not run on Python below 3.12.** Line 668 puts a backslash inside an f-string expression, a syntax error on 3.9, 3.10 and 3.11. `netlify.toml` pins `PYTHON_VERSION = "3.11"`, so a Netlify deploy would fail on this line. | `build.py: header()` | `SyntaxError: f-string expression part cannot include a backslash` |
| 0.2 | **The approved headline artwork is distorted at every width.** `.fw-lockup img` carries `width="3482" height="552"` but no `height:auto`, so `max-width:100%` squeezes the width while the height stays 552px. | Home, `.statement .fw-lockup img`, all widths | Rendered ratio 2.40 (1440), 1.71 (1024), 1.28 (768) and 0.63 (390) against a true 6.31. At 390 the lockup is 10× too tall. |
| 0.3 | **The Contact page header is invisible on load.** `body.light-page` makes the logo, nav and "Talk to us" pill indigo, but the page opens on an indigo ground. | `/contact/`, `.site-head:not(.solid)`, all widths | Logo, links and the "Menu" button are indigo on indigo until you scroll past 24px. |
| 0.4 | **The HubSpot form is completely unbranded.** The v2 embed renders inside a script-written `<iframe>`, so none of the ~25 `.hs-form` rules reach it. You get default HubSpot blue labels, grey rounded inputs and a native grey "Submit" button. | Every page with the contact band, plus `/contact/` | DOM: `.hs-target > iframe.hs-form-iframe`, with no `<form>` in the page document. |

---

## 1. Typography (highest visual impact after the blockers)

1. **The trial Castel font is missing glyphs, so stats render in two typefaces.** `castel-500` and `castel-900i` contain only 74 glyphs: no `% $ : ;`, no curly quotes, no en or em dash, no accents. Every result number (`+100%`, `+10.2%`, `$621m`, `98th` is fine) mixes a Castel digit with an Instrument Serif `%` or `$`. Headlines with `’` do the same: "Brands we’ve made work for" (`.lw-head h2`) and "Nestlé" in `.cw-list`. *Impact cards (`.im-card .n`) on Home and Work, `.proj-body .res .n`, `.svc-stats b`, all widths.*
2. **No coherent type scale.** There are 60+ distinct `font-size` declarations. Display sizes are set three times: once in base/extra/flourish, again in rebrand, and a third time in the "extra-condensed face reads smaller" block. Nothing shares a ratio, and line-heights vary from .8 to .98 at random.
3. **The fallback stack is still active.** `!important` forces `font-family`, `font-weight:400` and `text-transform:none` onto 40+ selectors because the Tungsten-era rules (uppercase, weight 900) are still in the cascade underneath.
4. **Leads and intros are set in Hanken Light (300) at 24 to 46px** (`.intro-lead`, `.page-hero .intro p`, `.lead-light`, `.proj-body .brief`, `.c3-p`). A light grotesk at headline size is the most "template" thing on the site: it reads as a default, not a voice, and it fights the serif quotes and Castel headlines.
5. **Labels are too small and too many sizes.** Condensed caps run at 12, 13, 14, 15 and 16px. `.tile .res` at 12px wraps to two lines of tracked caps on every tile ("FROM #3 TO #1 FLOUR BRAND IN THE US. DOUBLED SALES."). `.c3-offers .os` is 12px, and `.im-card .go` and `.svc-label` are 12 to 13px.
6. **Body sizes are inconsistent and often under 17px.** Sizes include `.intro-three p` 16px, `.box p` 15px, `.tile p` 15px, `.im-card .d` 15px, `.lead-row .bio p` 16px, `.c3-steps p` 16px and `.panel .body` 17px at .85 opacity. Measure is uncontrolled: `.panel .body` 52ch, `.tile p` 48ch (half a tile empty at 1440), and `.prose` 64ch but at 18px.
7. **No wrap control anywhere.** There is no `text-wrap: balance` or `pretty`. Orphans and widows appear in headings: "Built for the *next ten* / *years*" (About, 1440), "Brands we’ve *made* / *work for*" (Home, 1440 and 1024), "Real parents. Real / moments." (Nestlé SMA, 1440), and "…Agentic Era and Why AI Has Changed Sports Marketing / Forever" (Thinking cards).
8. **Italic overhang is clipped or misaligned.** The word-reveal masks (`.rv .w {overflow:hidden}`) cut italic swashes. The rebrand "fix" adds negative margins, which shifts italic words left of the grid line: "*years*" on About sits about 12px outside the left margin at 1440.
9. **Hierarchy collapses on the home intro row.** `.intro-three h3` is Barlow caps at 24 to 30px over 14px body on white. It looks like a footer, not three pillars of the business.

## 2. Layout and grid

1. **No max container width.** `.wrap` is padding only, so at 1920+ line lengths and image widths grow without limit.
2. **Three different gutters.** Gaps of 16, 20, 24, 32 and 40px are used for the same 12-column intent. `.strip3` uses 16px, `.cards` 40/24, `.ct-cards` 20, `.im-grid` 40/32 and `.lw-grid` 0.
3. **Columns drift.** Page-hero intro sits at columns 7–12, `.split .r` at 7–12, `.c3-p` at 8–12, `.dh-lead` at 4–12, `.im-head p` at 8–12, `.lw-head` 1–7, `.svc-body` 4–12, `.intro-body` 8–12 and `.dh-rows .s` 8–12. Five start lines on one site, so nothing lines up when you scroll.
4. **The voices carousel on Home leaves 60% of the band empty at 1440.** `.voice blockquote {max-width:22ch}` sits in a full-width indigo section with nothing on the right.
5. **The contact "Everything else" card is a 400px-tall empty linen box** next to the form (`.mail-card`, all pages, 1440 and 1024).
6. **The hero mark crops at 768.** `.hero-mark img {height:46vh}` at 768×1024 is 470px tall, which pushes the F off the left edge and squeezes `.hero-side`.
7. **The home intro row stacks to one column at 900px**, so at 768 three short columns become one long white stripe (`.intro-three`).
8. **Strip3 offsets look accidental.** `.strip3 .c {margin-bottom:12vh}` puts the right image 108px higher at 1440, 77px at 768 and 0 on mobile, so it reads as a bug rather than a decision.
9. **The page-hero watermark (`.page-hero::before`, `icon-peri` at 22%) is a muddy grey on linen** and collides with the H1 media pill on Services, Culture3 and Thinking at 1024 and 1440.

## 3. Vertical rhythm and pacing

1. **Section padding uses about 12 unrelated values:** `var(--sec)` (14vh, so short on landscape laptops and huge on tall monitors), `clamp(56px,9vh,104px)`, `clamp(40px,7vh,88px)`, and inline `style="padding-top:0"`, `style="margin-bottom:48px"`, `style="padding-bottom:40px"`, `style="padding-top:24px"` in `build.py`. Viewport-height spacing makes rhythm change with window height rather than width.
2. **Impact bands end with no bottom padding.** `.impact {padding-block:var(--sec) 0}` assumes a logo strip follows, but `logos=False` everywhere, so "See the case study" sits 0px from the next section (Home and Work, all widths).
3. **Ground changes are too frequent on Home.** The sequence is indigo → indigo → **white** → video → linen → **#121212** → white → indigo → image → indigo → linen → indigo → linen → indigo → carbon. `#121212` is not a brand colour.
4. **Inner pages have no pace.** Every section uses the same `.split` (heading left, prose right) at the same padding, so About scrolls for about 12,500px with one rhythm.

## 4. Colour and contrast

Automated sweep, failing items on solid grounds:

| Element | Page | Ratio | Needs |
|---|---|---|---|
| `.film .play` text (carbon on Scarlet Ink) | every case study | 3.09 | 4.5 |
| `.panel.p-red .body` (carbon at .85 opacity on Scarlet Fire) | About | 4.15 | 4.5 |
| `.guild .over p` and `.sec-link` over the darkened mosaic | Home, The Guild | depends on the image; bright frames drop below 3:1 at 390 | 4.5 |
| Header nav and logo (indigo on indigo) | Contact | about 1 | 4.5 |

Other colour problems:

- `.impact {background:#121212}` and `.box {background:#161616}` (Culture3 boxes) are off-palette near-blacks.
- `.cw-list li::after` still uses `mark-red.png`, the retired "E3" Fre3dom mark (Work page client wall).
- `--mute` is redefined in eight places with four different values.
- Text on scarlet uses carbon at 85% opacity, which is the cause of the failure above.

## 5. Imagery and crops

1. Image ratios are random: tiles 16:10, cards 16:10, `.door .thumb` 4:3, `.wwd .wimg` 4:5, `.strip3` 4:5/16:10/4:5, `.panel .media` 4:3, `.sizzle` 21:9, `.reel` 21:8, `.cs-gallery` 4:5 and `.proj-img` 16:9. There is no system.
2. The Culture3 H1 pill shows a small square video in a light-grey capsule because the source film is not 2:1 and `object-fit` is applied to a box that has no background. It looks broken at 1440 and 1024.
3. Parallax over-scales images to 110% and shifts them ±6%, which crops faces in tiles and the mosaic noticeably.
4. `.door .thumb` uses a greyscale filter at 50% opacity. It looks disabled rather than editorial.

## 6. Components

- **Header:** stays fixed and turns solid indigo after 24px. It never hides, so it covers about 70px of reading space on long pages. There is no light or dark adaptation to the section underneath (see 0.3). The active state is a 2px periwinkle inset shadow, which is invisible on linen.
- **Mobile menu:** `role="dialog"` with no focus trap, no Esc key, no body scroll lock, and focus not moved into or out of the dialog. The email address is plain text, not a link.
- **Buttons:** there are three systems: `.btn` (unused), `.ct-btn`, and the header pill. Hover goes from indigo to Scarlet Fire with carbon text and no transition timing. The film play button is a different shape and colour.
- **Links:** `.sec-link` is a static 1px border. Inline links in prose use `border-bottom`, and other links have no hover state at all (`.foot .links a`, `.crumbs`, `.article-head .meta a`).
- **Focus:** a global `:focus-visible` outline in `var(--red)`. It is Scarlet Fire on dark grounds (fine) but sits on images and buttons with no offset strategy. Tiles have no visible focus on the image.
- **Work tiles:** the custom cursor disc sets `cursor:none` on tiles (a usability regression), titles are Hanken 500, and the result line is 12px caps.
- **Impact cards:** count-ups run for 2,000ms with a 160ms × index lag, so the last card finishes about 2.8 seconds after it is reached.
- **Quotes:** there are three quote treatments (`.voices`, `.quote-band`, `.proj-quote`) with different sizes and widths.
- **FAQ (`details`):** only on service pages. There is no open/close animation, and the summary has no focus or hover state.
- **Thinking cards:** fine at 1440, but titles are 24px Instrument Serif with no balance, and the tag appears twice (inside the type card and as `.k` below it).
- **Article:** the body is centred at 64ch but the header is left-aligned at 1100px, so the H1 and body don't share an edge. Pull quotes are 26px serif with a periwinkle rule, which is invisible on linen. Images are capped to the 64ch measure with no breakout. A 3px Scarlet Fire progress bar sits at the very top, above the header.
- **Case study:** the `.proj-hero` client label is 15px muted with no hierarchy. Results (`.res .n`) are huge but the `%` falls back to the serif (see 1.1). "Next project" is a plain bordered row.
- **Service page:** a good basis (12-column, calm), but its labels sit at columns 1–3 and its body at 4–12. That grid doesn't match the rest of the site, and it repeats the font and colour overrides.
- **404:** a single heading with two tiny links, then the footer. It reads as unfinished.
- **Footer:** `.foot` grid columns 1–4, 6–9 and 10–12 with 14px muted text. The giant wordmark runs a WebGL shader continuously while visible.

## 7. Motion

- There are five easing curves and about fifteen durations, from .2s to 1.4s.
- **Headline word reveals** use a 105% mask, 900ms transitions and staggers up to 630ms (about 1.5s in total). They clip italics and can't be read mid-animation.
- **Animated full-screen grain** (`.grain`, z-index 40, `steps(4)` at 1.2s) sits over everything, including body text and the white logo wall.
- Several things move automatically with no pause control: the auto-advancing quote carousel (9s), the prose ticker and the big marquee. Hover-pause doesn't count as a control (WCAG 2.2.2).
- Reduced motion is handled in some places but not all. `.tile img` scale, `.cards .cimg img` and the `.lw-grid` crossfades ignore it.

## 8. Scroll behaviour

- There is no smooth anchor scrolling and no `scroll-padding-top`, so `/agency/#leadership` lands under the fixed header.
- The DNA panels use `position:sticky` at 100svh. That's good, but each panel's content sits at the very bottom on short laptop screens.
- `requestAnimationFrame` runs every frame forever (cursor, parallax, progress bar), even on pages with none of those elements visible.

## 9. Consistency between pages

- The page-hero, `.proj-hero`, `.article-head`, `.svc-top` and `.contact-page` H1 all use different top padding (130 to 220px) and different H1 sizes.
- Section labels have three treatments: `.sec-lbl` with a periwinkle dot, `.svc-label` without, and `.cs-sec .lbl` in scarlet.
- The "next" navigation appears on case studies and articles but uses the same styling for different jobs.

## 10. Accessibility

- There is no skip link.
- The mobile menu dialog issues are listed under components.
- `.voices` has `aria-roledescription="carousel"` but no live region and no pause control. The slide count "1 / 6" is not announced.
- `.tile` links contain an h3 and two paragraphs. That's fine, but the hover-only Vimeo iframe has `aria-hidden` and `tabindex=-1`, which is correct.
- On `.filters`, the `aria-pressed` buttons work, but a 4px hit area makes them about 22px tall, under the 24px target size.
- In `.ct-card .ct-kicker .mk`, the periwinkle dot carries no meaning and is fine as decoration.
- The form loads in an iframe (see 0.4) and inherits HubSpot's own labels, which are accessible.

## 11. Performance

- The header logo is a 1600×287 PNG shown at 22px tall, and it ships twice (white plus indigo: 187KB). The footer adds `logo-linen` (132KB) plus `logo-white` again.
- WebGL shaders run on About (the red flow panel) and in the footer wordmark on every page, using continuous rAF while visible.
- The site CSS ships about 1,300 lines, of which about 25% is dead: `.proof`, `.dna`, `.pillars`, `.beliefs`, `.chapters`, `.team`, `.posts`, `.svc`, `.proofrows`, `.c3is`, `.pull`, `.logos-band`, `.clients`, `.btn`, `.giant`, `.ph-0`…`.ph-18`, `.ct-grid` and others. There are 48 `!important` flags.
- The `tungsten-*.woff2` `@font-face` rules are still declared, though nothing renders in them after the overrides.
- Thinking cards hotlink Substack images for every article (no `thinking-images.json` locally). That is out of scope for design, but it hurts LCP on `/thinking/`.
- Media mostly reserves space via aspect-ratio boxes (good). The lockup does not (see 0.2), and `.cards .cimg` reserves space but the remote image's ratio is cropped.

---

### What is already good and should be kept

- The brand palette and the four-family type pairing are strong.
- The DNA panels on About (sticky colour panels) are the best moment on the site.
- The service-page template has the calmest, most "designed" layout and is a good model for the rest.
- Real self-hosted hover loops on work tiles, View Transitions already declared, and reduced-motion respected in most places.
