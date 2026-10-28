# Design changelog: craft pass

What changed, why, and how it was checked. `AUDIT.md` has the problem list this responds to. Screenshots are in `qa/before/` and `qa/after/` (13 templates × 1440, 1024, 768 and 390px, full page), with side-by-side pairs in `qa/compare/`.

No copy, wording, page order, URLs, titles, meta descriptions, canonicals, structured data, HubSpot form embed, Vimeo playback, film assets or the `SERVICE_PAGES_LIVE` switch were changed. All 153 generated pages were diffed against a build of the original sources. Titles, meta tags, canonicals and JSON-LD are byte-identical. Visible text is identical apart from two deliberate additions: a "Skip to content" link, and SVG chevrons replacing the `‹ ›` glyphs on the quote arrows (the buttons keep their "Previous quote" and "Next quote" labels).

---

## Fixed before design work

| Problem | Fix |
|---|---|
| `build.py` failed on Python 3.9–3.11 (backslash inside an f-string). Netlify pins 3.11, so it would fail there too. | Rewrote the one line. Output is identical. Now builds on 3.9+. |
| The approved lockup *Freedom makes better work* was squashed at every width (rendered ratio 2.4 down to 0.63 against a true 6.31). | `height:auto` plus `aspect-ratio:3482/552`. It now renders at its true proportions at every width. |
| The Contact page header was indigo on indigo. | The header has a light and a dark state set at build time per page, then follows the ground beneath it as you scroll. |
| Under reduced motion the home hero went black: CSS hid the film, and a script had already hidden the poster. | The poster stays under the film. Under reduced motion the film is paused and not downloaded, and the pause button shows a play icon with the "Play film" label. |
| The HubSpot form ignored all brand styling (it renders in a same-origin iframe). | After `onFormReady`, a brand stylesheet is injected into the form's iframe and the iframe auto-sizes. The embed code, portal and form IDs are unchanged. |

## Phase 2: foundations

**One stylesheet.** `base.css`, `extra.css`, `flourish.css` and `rebrand.css` (about 1,185 lines with 48 `!important` flags, about 25% dead and three layers overriding each other) are replaced by `src/site.css` (about 830 lines, 5 `!important` flags, 1 unused selector kept on purpose). `build.py` now loads only that file. The originals are kept for reference in `qa/legacy-css/`.

The five remaining `!important` flags are deliberate: four in the reduced-motion override (which must beat everything) and one to make HubSpot's inline iframe width fluid.

**Tokens** (all in `:root`):
- **Type scale:** 12 fluid steps from 390 to 1440px using `clamp()`, each with its own line-height and tracking. Label 13→14, caption 14→15, small 15→16, body 17→19, lead 22→34, h4 23→32, quote 30→58, h3 42→68, h2 58→136, h1 70→212, stat 68→148, display 104→380.
- **Spacing:** a 4/8 scale (`--sp-1` to `--sp-10`) plus section tokens: `--sp-section-sm` 56→112, `--sp-section` 80→168, `--sp-section-lg` 104→216, and `--sp-block` 40→72 for the gap between a section head and its content. Spacing is now width-based, not viewport-height-based, so rhythm no longer changes with window height.
- **Grid:** 12 columns, `--gutter` 16→32px, `--margin` 20→72px, `--max` 1600px. `--inline` caps the content width on large screens. There are two canonical tracks: headline columns 1–6 with text 7–12, and label columns 1–4 with content 5–12.
- **Colour roles:** `--surface`, `--surface-2`, `--ink`, `--heading`, `--muted`, `--line`, `--line-strong`, `--accent`, `--dot`, `--focus`, `--btn-bg` and `--btn-ink`, defined for each ground: linen, white, indigo (dark), carbon (impact and footer), periwinkle and scarlet. Every section picks a ground; components only read roles. Every role pairing was checked for AA.
- **Radii:** 0, 2, 4 and pill.
- **Motion:** 3 curves (`--ease-out` for arrivals, `--ease-io` for wipes, `--ease-std` for state changes) and 3 durations (180, 360 and 720ms).

**Off-palette colours removed.** `#121212` (impact), `#161616` (Culture3 boxes) and `#0b0b0b` were replaced. Impact now sits on Carbon Black, and the boxes on white.

## Phase 3: typography

- **Super Castel only at display sizes:** h1, h2, h3, stats, the marquee and the footer wordmark. Leads, subheads, quotes and card titles are Instrument Serif, replacing Hanken Light at 24–46px, which read as a default rather than a voice. Labels are Barlow Condensed caps at one size (13→14px, tracking .1em). Body is Hanken at 17→19px with 1.6 line-height and a 60–70ch measure (articles use a 44rem column, about 68 characters).
- `text-wrap: balance` on all headings and `text-wrap: pretty` on paragraphs, list items and captions. This removes the widows the audit listed, such as "Built for the *next ten* / *years*" and "Brands we’ve *made* / *work for*".
- **Trial-font glyph gaps.** Castel has no `%` or `$`, so stats used to render half in Castel and half in a stray fallback. Stats are now marked up as number plus unit, and the unit is set as a deliberate raised serif unit (`+100%`, `$621m`, `33%`). This is markup only; the text is unchanged. When the licensed Castel arrives, the `.u` rule can simply be deleted.
- **Italic clipping fixed.** The word-mask reveal (`overflow:hidden` per word, plus negative-margin hacks) is gone, so italic swashes are never cut and never sit off the grid line.
- Quotes use a hanging opening mark (`text-indent:-.36em`) so the text edge aligns optically with the grid.

## Phase 4: layout and rhythm

- Every section now aligns to the 12-column grid. The five previous "text start" columns (4, 6, 7, 8 and 9) are now two.
- Section padding comes only from the three section tokens. Inline `style=` spacing in `build.py` (9 instances) became classes (`split-head`, `flush-top`, `page-hero.tight`).
- Image ratios now come from a short list: 16:10 (tiles, cards, doors, panels), 4:5 (portraits, service thumbnails, gallery) and 21:9 (sizzles, reel).
- The image strip (`.strip3`) sits on grid columns 1–3, 4–9 and 10–12 with deliberate top and bottom alignment, replacing the arbitrary `12vh` offset.
- **One card system.** Work tiles and Thinking cards share the same media box, title (serif h4 with drawn underline) and meta treatment. The result line on tiles is now readable sentence case with an accent dot, replacing 12px tracked caps that wrapped to two lines.
- **Home sequence.** The impact band now has bottom padding. The voices carousel uses label column 1–3 and quote column 4–12 instead of leaving 60% of the band empty. The Guild mosaic stacks under its text on mobile instead of overlaying busy photos.
- **Contact band.** The empty 400px "Everything else" box is now a light ruled column beside the form.
- **About.** DNA panels keep their sticky stacking, with text at full contrast (no 0.85 opacity on scarlet) and 16:10 media.
- **Case studies.** Brief on 1–6 and result on 8–12. Sections on 1–5 and 7–12. "Next project" is a full-width row with a moving arrow.
- **Service page** (built with the flag only): moved to the site's label 1–4 and content 5–12 track, and the stat units fixed.
- **404.** Now a designed page: indigo ground, display headline, links and a large periwinkle Fw mark.

## Phase 5: motion and scroll

- **One reveal:** opacity plus a 20px rise over 720ms with `--ease-out` and 70ms staggers (at most 4 steps). It applies only to elements below the fold at load, never nests, and never clips. Removed: the word-mask headline reveal (about 1.5s), animated full-screen grain, the custom cursor disc (`cursor:none` on tiles), and greyscale and 50% opacity on Explore thumbnails.
- **Count-ups** now take 800ms (was 2,000ms plus 160ms per card) and keep the unit markup intact.
- **Header** hides on scroll down, returns on scroll up, stays visible while it has keyboard focus, and turns solid with a hairline after 24px.
- **Smooth anchor scrolling** with `scroll-padding-top`, so `/agency/#leadership` lands below the header (checked: 88px from the top).
- **Page transitions** use `@view-transition {navigation:auto}` (a 280ms cross-fade, with the header excluded so it doesn't flash). This is progressive enhancement and off under reduced motion.
- **Parallax** is limited to editorial imagery (the image strip, DNA panel media and service thumbnails) at ±3% with a 1.06 scale, down from ±6% at 1.1 on everything including faces in tiles.
- **Hover states on every interactive element:** drawn underlines (links, nav, tile and card titles, "See the case study"), arrow nudges, a 12px slide for large list rows, an image scale of 1.035, button colour shifts and logo-wall colour reveals.
- **Reduced motion** is honoured globally: no reveals, no parallax, marquee and ticker stopped, the quote carousel starts paused, headline pill films are paused, and View Transitions are off.
- **No layout shift.** Measured CLS is 0.000 on all seven measured templates (see QA). This comes from reserved form height (523 or 707px via a container query), a reserved aspect ratio for article images, a metric-matched fallback for Hanken, and preloads for the five above-the-fold font files.

## Phase 6: components and details

- **Header and menu:** the logo uses 480px derivatives (5–7KB instead of 75–132KB). The menu button has a two-bar icon. The menu is a proper modal: focus moves to Close, Tab is trapped, Esc closes it, focus returns to Menu, the page behind is scroll-locked, the current page is marked, and the email address is now a link.
- **Buttons:** one pill system (indigo with linen text on light grounds, linen with indigo text on dark), with a Scarlet Fire hover and carbon text (4.9:1). The film Play button follows the same system: linen with indigo text, replacing carbon on Scarlet Ink, which failed at 3.09:1.
- **Quote carousel:** adds a pause/play button (WCAG 2.2.2), pauses on hover and on keyboard focus, and announces manual changes politely. Arrows are drawn SVG chevrons instead of `‹ ›` glyphs.
- **FAQ accordion:** a circular plus that rotates to a cross, with a smooth height animation where `interpolate-size` is supported.
- **Thinking filters:** 40px pills (previously text links with a 4px hit area), with a filled state for the active filter.
- **Article:** the header and body share one reading column. The meta line has a hairline. Pull quotes have a Scarlet Ink rule. Image-only paragraphs break out slightly wider than the text. The reading-progress bar is 2px Scarlet Ink.
- **Footer:** sits on the grid (1–4, 7–9 and 10–12), with hover underlines on links.
- **Details:**
  - periwinkle selection colour
  - slim indigo scrollbar
  - a skip link as the first tab stop
  - hairlines at 1px with role-based opacity
  - the retired "E3" mark (`mark-red.png`) removed from the client wall and replaced with a 0.16em accent dot
  - the favicon was already correct and is unchanged

## Phase 7: QA

**Contrast:** an automated sweep of every text node on 12 templates at 1440 and 390 found 0 failures. Before, it found 6 at 1440: the Play button at 3.09, the scarlet panel body at 4.15, Guild overlay text over bright frames, and the Contact header at about 1:1.

**axe-core** (WCAG 2.0/2.1/2.2 A and AA, plus best-practice) on 12 templates at 2 widths: 0 violations, except one `heading-order` notice on the sample article. That notice comes from an `h6` in the author's Markdown, and article content was left as written. Heading levels in templates were corrected: work-index tiles and Culture3 boxes now use h2, and the Contact page form card uses h2.

**Keyboard:** checked with scripted tests. The skip link is the first stop, focus rings are visible on every control, the menu traps and returns focus, and Esc closes it.

**Performance:** Lighthouse could not be run because this machine has no Node.js. Instead, the same lab conditions were reproduced in Chrome via DevTools Protocol: 390×844 at 2× DPR, 4× CPU slowdown, 1.6 Mbps with 150ms RTT, cache disabled, median of 2 runs. The before figures are the original sources built in the same way.

| Page | FCP before → after | LCP before → after | TBT | CLS before → after | Transfer before → after |
|---|---|---|---|---|---|
| Home | 2.80s → 2.08s | 3.68s → 2.08s | 34 → 0ms | 0.000 → 0.000 | 1075 → 751KB |
| About | 2.70s → 1.72s | 2.70s → 2.01s | 6 → 0ms | 0.010 → 0.000 | 915 → 632KB |
| Work | 2.83s → 1.68s | 2.83s → 2.74s | 4 → 0ms | 0.087 → 0.000 | 1247 → 832KB |
| Case study | 2.23s → 1.43s | 2.75s → 1.81s | 2 → 0ms | 0.000 → 0.000 | 981 → 652KB |
| Thinking | 2.65s → 1.68s | 6.05s → 1.68s | 7 → 0ms | 0.019 → 0.000 | 1092 → 666KB |
| Article | 2.03s → 1.29s | 3.51s → 2.29s | 6 → 0ms | 0.122 → 0.000 | 556 → 227KB |
| Contact | 2.00s → 1.24s | 2.00s → 1.24s | 0 → 0ms | 0.200 → 0.000 | 527 → 291KB |

These numbers map to roughly 90–100 on Lighthouse's mobile performance curve. Please confirm with a real Lighthouse run on the Netlify deploy preview.

---

## Restored after review

At the client's request, ten signature effects from the original site were reinstated, rebuilt on the new tokens:
- grain
- the word-by-word headline reveal
- the scarlet cursor dot
- the pill growing in with its headline
- the Fw watermark on inner-page heroes
- stronger parallax on tiles, the Guild grid and Explore thumbnails
- greyscale Explore thumbnails
- 2-second staggered count-ups
- 18px row slides on hover
- the periwinkle "Talk to us" when the header is solid

These supersede the "removed" notes in Phase 5. The fixes were kept:
- italics are not clipped
- the normal cursor stays visible
- headings keep a full accessible name
- everything is off or held still under reduced motion

After restoring them, QA still shows 0 contrast failures, CLS of 0.000, and 19 of 19 behaviour checks passing. Note that the word reveal runs about 1.4s on long headlines, longer than the 800ms the brief suggested.

## Judgement calls, chosen for accessibility or robustness

1. **Scarlet Fire on light grounds.** The rule is kept: red text on linen or white uses Scarlet Ink. Scarlet Fire appears as a fill (dots, panel, button hover) and as large stats on Carbon only.
2. **Film Play button.** It was Scarlet Ink with carbon text, which failed at 3.09:1. It is now linen with indigo text, and turns Scarlet Fire with carbon text on hover.
3. **Hover-only motion on tiles** (loops and Vimeo previews) stays pointer-only and is off under reduced motion. The click-to-play Vimeo behaviour is unchanged.
4. **Auto-advancing quotes** now have a visible pause control instead of only pausing on hover.
5. **Trial Castel glyphs.** Units are restyled rather than substituted. No characters were changed in the copy.
6. **The `h6` in one article** was left alone, because changing it would change authored content.
7. **WebGL shaders** (the About scarlet flow and the footer wordmark) were kept. They run only while visible and are skipped under reduced motion.

## Files

- `src/site.css`: new, the whole design system.
- `src/flourish.js`: rewritten for the motion language, header, menu, carousel and HubSpot dressing (form loading logic unchanged).
- `build.py`:
  - loads `site.css`
  - fixes the f-string line
  - header theme, skip link, `main#main`, menu markup, carousel pause control
  - stat unit markup
  - heading levels
  - inline spacing styles replaced with classes
  - small logo files and font preloads
- `src/home-main.html`: hero image priority hints and `srcset` (no copy changes).
- `site/assets/brand/`: new `logo-{white,indigo,linen}-480.png` and `icon-linen-600.png` (optimised derivatives; originals untouched).
- `README.md`: points to the new stylesheet and these notes.
- `qa/legacy-css/`: the four retired stylesheets.
