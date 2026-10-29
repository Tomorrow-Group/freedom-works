# Handover: Freedom Works design pass

This package contains the full project after the design pass. Run `pip3 install -r requirements.txt`, then `python3 build.py`. Read `CHANGELOG-design.md` for what changed and why, and `AUDIT.md` for the problems it fixed.

## Features from the original site: all ten restored

Some of the original's signature effects were removed in the design pass. They were all put back afterwards, rebuilt in the new system:

1. Animated film grain over the whole site (`body::after`; held still under reduced motion)
2. Headlines revealing word by word out of a mask. The mask is now padded, so italic swashes are no longer clipped, and screen readers get the whole line through `aria-label`.
3. A scarlet dot trailing the pointer over work tiles. The normal cursor now stays visible.
4. The media pill growing in with its headline
5. The Fw watermark behind inner-page headlines (periwinkle at 38%; text contrast re-checked)
6. Stronger parallax on work tiles, the Guild image grid and Explore thumbnails (±6%), with gentle parallax (±3%) on the other editorial images
7. Explore thumbnails in greyscale at 50%, turning to colour on hover (always in colour on touch screens)
8. Slow, staggered count-ups (2s, 160ms between cards)
9. Rows sliding 18px on hover (Calibre, Culture and Craft rows, and the Explore list)
10. "Talk to us" turning periwinkle when the header is solid on a dark ground

All of these are off or held still under reduced motion. The original code is still kept in `qa/original-src/` and `qa/legacy-css/` for reference.

## State of the project

- The site builds on Python 3.9 or newer.
- `SERVICE_PAGES_LIVE` is still `False`.
- Before/after screenshots are in `qa/before`, `qa/after` and `qa/compare`.
- Not done yet:
  - a real Lighthouse run on a Netlify preview
  - a test submission of the HubSpot form
  - the licensed Castel font files (drop them in with the same names)

## Notes for the Replit → Netlify review (28 Oct)

**Static or Replit-specific?** Fully static. `build.py` writes plain HTML, CSS and JS into `site/`. Replit only runs the build and a simple preview server (`.replit`). Netlify is already configured in `netlify.toml`:
- the build command
- `publish = "site"`
- Python 3.11
- cache and security headers

The only Replit-aware code is a safety switch: when `REPL_ID` is present (or `STAGING=1`), every page gets `noindex` and `robots.txt` disallows all.

**Redirects.** Already in Netlify's format: `build.py` generates `site/_redirects` (see `NETLIFY_REDIRECTS`). The old Liberty Guild site was a single page, so every address on `thelibertyguild.com` (with or without www, http or https) redirects to `https://freedom.works/` with a 301. This takes effect once the old domain is added to the Netlify site as a domain alias and its DNS points to Netlify.

**Videos.**
- **Case study films:** the 9 full-length films stream from Vimeo, not the site.
- **Self-hosted clips:** 25 short, silent clips are stored in the site, 28 MB in total:
  - the hero film (1080 and 720)
  - 6 page sizzles
  - 10 tile hover loops
  - 6 headline pills
  - the Snowfox film
- **To serve the clips from Bunny CDN:**
  1. Upload `site/assets/film/*.mp4` and `site/assets/media/*.mp4` to the Bunny storage zone, keeping the same paths (`/assets/film/…`, `/assets/media/…`).
  2. In Netlify → Site configuration → Environment variables, add `VIDEO_CDN` = the pull zone URL (e.g. `https://freedomworks.b-cdn.net`).
  3. Redeploy. Every video address on every page then points to Bunny. Images and fonts stay on Netlify.

**replit.app competing with freedom.works.** Already prevented in three ways:
1. Replit builds are `noindex` on every page, and their `robots.txt` disallows all crawling.
2. Every page carries a canonical tag pointing at `https://freedom.works/…`.
3. After launch, unpublish the Replit deployment.

SEO crawls of the Replit copy need "ignore robots.txt" switched on.

**Cookie consent.** Pending Cookiebot: we need the Cookiebot domain group ID, to add the script with Google Consent Mode v2 defaults ahead of GTM. Domains to register:
- `freedom.works`
- `www.freedom.works`
- the Netlify preview domain

## Analytics (Braidr's setup, 28 Oct)

- **Google Tag Manager GTM-5326PCK7** is on every page of the live build. GA4 (property 559567923) is configured inside the container by Braidr.
- **Where it's off:** Replit review copies (`REPL_ID` present) and the Claude preview. To change the container, set `GTM_ID` in Netlify; `GTM_ID=off` disables it.
- **Consent Mode v2:** defaults are set before GTM loads, with everything denied except functionality and security storage. When `COOKIEBOT_ID` is set in Netlify, the Cookiebot banner loads before GTM (manual blocking mode, so the HubSpot form and Vimeo films are never blocked) and updates Consent Mode when the visitor accepts.
- **Signals the site pushes to the dataLayer**, for Braidr to use as triggers. The `fw_` prefix avoids double-counting with their own tags.

  | dataLayer event | When | Parameters | Braidr event |
  |---|---|---|---|
  | `fw_form_submitted` | HubSpot `onFormSubmitted` | `form_location` | `form_submission` |
  | `fw_email_click` | any `mailto:` link | `email`, `page` | `click_email_address` |
  | `fw_video_play` | a case study film's play button | `video_title`, `page` | `view_case_study_video` |
  | `fw_cta_click` | any element with `data-cta` | `cta_name`, `cta_text`, `page` | `click_cta` |

- **CTA labels in use:**
  - `header-talk-to-us`: the header "Talk to us"
  - `service-talk-to-us`: service page CTAs
  - `start-enquiry`: the form fallback button
- **hello@freedom.works** is linked in the footer and under every contact form.

## SEO setup (28 Oct)

The full audit runs across all 176 pages. Everything is built in, so new pages get it automatically.

**Titles**
- Every page has one, 60 characters or under, with no duplicates.
- " | Freedom Works" is dropped when the title would run too long.
- Long article headlines get a natural short search title (the part before a colon, or the first sentence). The page itself keeps the full headline.

**Descriptions**
- Every indexable page has one, of about 70 to 160 characters.
- Short ones are topped up from the page's own opening sentences, skipping captions and headings.

**Headings and addresses**
- One H1 per page.
- A canonical tag on every page, pointing at `https://freedom.works/…`.

**Social sharing**
- `og:url`, `og:type`, `og:site_name` and `og:locale`, plus Twitter tags.
- Case studies and articles share with their own image: a 1200×630 JPEG auto-made in `assets/share/`.

**Structured data**
- Organization (with description and slogan), WebSite and BreadcrumbList.
- Service (19 pages).
- CreativeWork (case studies), with image and URL.
- Article (136), with image, publisher logo, `datePublished`, `dateModified` and `mainEntityOfPage`.

**Sitemap**
- `/sitemap.xml`: every indexable page, each with a `<lastmod>` date. Articles use their publication dates.

**Hidden from Google until launch**
- `robots.txt` allows everything on the live build.
- `STAGING=1` or Replit gives `noindex` on every page and `Disallow: /`.

**Known for later**
- Inline images in older Thinking articles are hotlinked (Substack S3, Unsplash) and have no width or height. That causes minor layout shift on those articles only. Fix by re-hosting them locally.

## In-article images and the rebrand note (28 Oct)

**In-article images are no longer hotlinked.**
- On every build, `fetch_thinking_images.py` saves a local copy of each image inside the Thinking articles. It saves them to `src/thinking-img/inline/` (WebP, max 1400px), with their sizes in `src/thinking-images.json`.
- `build.py` swaps the Substack and Unsplash addresses for these copies and adds `width` and `height`.
- Images that can't be fetched keep their original address.
- To stop depending on Substack at build time, commit `src/thinking-img/` and `src/thinking-images.json` to GitHub once.

**Old domain and rebrand note.**
- Every address on `thelibertyguild.com` (with or without www, http or https) 301s to the homepage, tagged `utm_source=thelibertyguild.com&utm_medium=redirect&utm_campaign=rebrand`. This takes effect once the domain is added to Netlify as a domain alias and its DNS points to Netlify.
- Visitors arriving with that tag see a one-time, dismissible note under the header: "Looking for The Liberty Guild? You’re in the right place. We’re now Freedom Works. About us".
- It is remembered in `localStorage`, so it shows only once per visitor.
- Tracked as `fw_rebrand_note_view` and `fw_rebrand_note_click`. The UTM tag also attributes these visits in GA4.
- The wording is in `src/flourish.js`.

**Cookiebot is live in the build:** domain group ID `c9e759c8-bb2b-436a-9904-497e636e9d29` (the default in `build.py`; override with `COOKIEBOT_ID` in Netlify). The snippet matches Cookiebot's manual-blocking script. It is off on Replit and in the Claude preview, like GTM.

## Performance and layout stability (28 Oct)

**Layout shift (CLS).** Under 0.1 ("good") on every page tested, even with fonts delayed by 1.2s.
- **Metric-matched stand-in fonts:** `FW Castel Fallback`, `FW Serif Fallback`, `FW Cond Fallback` and `Hanken Fallback`. They are local Times or Arial, with `size-adjust` and ascent and descent overrides measured from the brand fonts, so text doesn't reflow when the brand fonts arrive.
- **Headlines are split into words at build time** (`presplit_headings` in `build.py`), so the reveal never re-wraps them.
- **While the brand fonts load** (the `html.fp` class, max 1.8s), headlines wait unseen, then reveal.
- **With scripts off,** headlines show normally. Words only start hidden under `html.js`.
- **Large headlines** use `text-wrap: balance`.

**Mobile loading.**
- Only the two headline fonts (Castel regular and italic) are preloaded.
- The homepage hero still has phone and tablet sizes (`hero-poster-828.webp` at 12 KB, `hero-poster-1280.webp`).
- The hero film loads and plays after the page's `load` event (`data-play-after-load`), so it doesn't compete with first paint.

**Python.** Netlify builds with Python 3.11. Test every `build.py` change against 3.11: no reused quotes or backslashes inside f-string expressions.

## SEO review changes (29 Oct, from Ema's review)

**Navigation**
- Services is first, with a dropdown of the 5 main areas (`L2_SERVICES` in `build.py`).
- On mobile, the 5 areas are listed under Services.
- The footer has a Services column.

**Homepage**
- The H1 is "Freedom Works · Global creative agency": small, at the top of the hero.
- "Welcome to Freedom Works." is now an H2.

**Services hub**
- Every sub-service is linked.
- Moving client logo strip.

**Service pages**
- "See all work" links to /work/.
- The quote has its own "What clients say" section.
- Thinking shows as image cards.
- Sub-service pages say "Related services".
- The 5 main pages open with a case-study still and a caption link (`SVC_HERO_CASE`).

**Thinking**
- Five topic pages at `/thinking/<topic>/`, with intros in `TOPIC_INTRO`. "On the model" is now "The agency model" (`/thinking/the-agency-model/`).
- The Thinking page's topic buttons are now links.

**Articles**
- Topic link at the top.
- "By {name}, {role}" byline, linking to the person's bio on the About page (`#jon-williams` etc).
- Authors come only from `src/confirmed_authors.json`. Everything else is credited to Freedom Works.
- `AUTHOR_ROLE` holds the roles; Aimée's is pending.
- Share row: LinkedIn, X, email, copy link (tracked as `fw_share`).
- "Put this thinking to work" panel, with paired services by topic (`TOPIC_SVC`).
- "More on {topic}" cards.
- A sticky "Talk to us" on desktop (`data-cta="article-sticky-talk-to-us"`).
- One in-text link to a service on articles that naturally mention one (`SVC_PHRASES`).

**About**
- New plain opening paragraph.
- "Brands we've made work for" logo wall.
- Closing statement ("We make work that matters…").
- Each leader has a link point.

**Images**
- `optimise_images()` makes 800px copies of the case-study stills, used through srcset in tiles.
- WebP copies of all logos and awards, which pages use automatically (`webpify`).

**Other**
- Fuller `llms.txt`, generated from the site's own data, in the strict llmstxt.org format. Lighthouse 13.6 Agentic Browsing scores 3/3 (accessibility tree, CLS, llms.txt).
- Alt text on all logo images.
- 500+ everywhere.

**Still waiting on**
- LinkedIn and Instagram addresses (footer and contact page).
- Whether there's a publishable address (footer, contact and map).
- Ema's confirmation on the service page H1 size.

## Feedback round (29 Oct, afternoon)

- **The Guild:** 600+ everywhere: site copy, search descriptions, structured data, and llms.txt. The archive articles are unchanged.
- **About, leadership intro:** the paragraph's first line now starts level with the top of the headline's lowercase letters. The offset is `0.29 × --fs-h2 − 0.21 × --fs-lead`, from the fonts' metrics, applied above 900px wide.
- **About, DNA cards:** a card taller than the screen now scrolls fully into view before it pins, so the next card no longer covers its image and text (script in `src/flourish.js`).
- **Culture3 page:**
  - The logo now fills its column.
  - The three stills are frames from the Culture3 film: `c3-onstage`, `c3-offstage` and `c3-conversation` in `assets/media`.
  - `strip3()` now takes an optional focus point for each crop.

## Policy pages from the old site (29 Oct)

- **New pages:**
  - `/diversity-inclusion/` and `/modern-slavery-statement/`, with text in `src/legal/diversity-inclusion.md` and `src/legal/modern-slavery-statement.md`.
  - Rebranded from The Liberty Guild to Freedom Works, with typos fixed.
  - Linked in the footer.
- **Old addresses:**
  - `/legal`, `/slavery-act` and `/diversity-inclusion` on thelibertyguild.com now 301 to `/privacy/`, `/modern-slavery-statement/` and `/diversity-inclusion/`.
  - These rules sit before the catch-all homepage redirect.
- **The modern slavery statement still needs:**
  - the legal entity and company number
  - the financial year it covers
  - board approval and the date
  - a director's signature (red placeholders on the page)

## Leadership portraits and roles (29 Oct)

- **Roles:**
  - Jon Williams: Founder and Chief Creative Officer
  - Lins Karnes: Chief Delivery Officer
  - Aimée Luther: Managing Director
  - Holly Dillon: Chief Operating Officer, Culture3
  - Jamila Saidi: Chief Growth Officer, Culture3

  They're shown in that order, and Aimée's role also appears on her article bylines (`AUTHOR_ROLE`).
- **Portraits:**
  - `assets/media/team/<slug>-600.webp` and `-1200.webp`.
  - True black and white, cropped to 4:5, loaded by srcset.
  - To replace one, overwrite both files with the same names.
