# Expert DNA v2: shared build spec (internal, for build agents)

Brand root: /home/user/Claude/expert-dna-brand
Old v1 (two halves, Schibsted) is in archive/ : do NOT use it.

## Mark (logo 0, "half moon and plug")
- Box 54 x 48 units. Half moon: path "M24 0 A24 24 0 0 0 24 48 Z" (the human brain, the expert).
- Plug: vertical bar x 30, width 3.5, height 48; prongs: rect x 38 y 14 w 16 h 3.5 and rect x 38 y 30.5 w 11 h 3.5.
- Python helper: _work/brand3.py exports mark_inner(brain_colour, plug_colour), horizontal(), stacked(), C (colours), WORD/REG Face objects with .path(text, cap_px, x0, baseline) for outlined text.
- Logo files: logo/svg/expertdna-{horizontal|horizontal-tagline|stacked|stacked-tagline|mark|wordmark|endorsed}-{colour-on-light|colour-on-dark|black|white|accent}.svg ; PNGs in logo/png.
- Colourways: light = ink half moon + accent plug + ink word; dark = white half moon + accent plug + white word; on an accent field use the black version.

## Colour (tokens/tokens.css, --edna-*)
ink #101114, white #FFFFFF (main light background), paper #F4F3F0 (secondary light surface), accent #FF5533, accent_tint #FFE1D8, accent_deep #B32F15 (small accent text on light only), grey #66655F (secondary text on light), grey_dark #A3A29C (secondary text on dark), line #E2E0DB, line_dark #2E3036, surface_dark #1A1B1F (raised surface on ink).
Rules: white is the default background, not paper. Text on accent is always ink. Never white or grey text on accent. Accent covers at most one third of a layout unless it is a full accent field (max one per set). No gradients, shadows, glow, rounded corners.

## Type
Hanken Grotesk (fonts/HankenGrotesk-Regular/Medium/Bold.ttf) for everything; IBM Plex Mono (fonts/IBMPlexMono-Regular/Medium.ttf) for small uppercase labels, numbers, captions only.
Headlines: Hanken Grotesk Medium (not Bold), letter-spacing -0.03em, line-height 1.02-1.08. Big display can use Medium at very large sizes; Bold only for small UI emphasis.
Labels: IBM Plex Mono Medium, uppercase, letter-spacing 0.12em, 11-14 px equivalent.
Body: Hanken Grotesk Regular, line-height 1.5.
PowerPoint names: "Hanken Grotesk" (Regular/Bold), "Hanken Grotesk Medium", "IBM Plex Mono", "IBM Plex Mono Medium".

## Motifs (derived from the mark; one main motif per layout)
1. Half moon: a large solid half disc cropped by an edge of the layout (ink on light, white or ink on dark, ink on accent). Means the human, the expert's mind.
2. Prongs: two horizontal bars with length ratio 16 : 11 and thickness = 3.5/48 of their implied mark height, optionally with the vertical plug bar. Means the connection to AI. Usually accent.
3. Thin rules: 1 px full-width lines (line colour) separating zones.
Layout: generous white space, asymmetric, square corners, flat.

## Content rules
- Never use long dashes (em dash or en dash) anywhere, including inside .pptx XML, HTML, SVG, filenames. Use colon, comma, period. Plain hyphen only for ranges.
- No invented numbers, metrics, testimonials, client names or claims. Placeholders in braces: {Client name}. Mock UI data must be neutral (e.g. "Client A", "{Name}", generic dates like "Tue", no percentages, no revenue).
- No stock photos, no icon packs, no emoji, no DNA helix or molecules, no brain clichés (circuit brain, glow, lightbulb, gears, robot).
- Prices are working numbers (placeholders): Book 7 EUR, Starter 29 EUR, each plugin 29 EUR, all 8 plugins 97 EUR, Setup Call 297 EUR.

## Products (facts from the brief only)
- Expert DNA Starter, 29 EUR, order bump. (Contents not specified in the brief. Working assumption: a starter set of Expert DNA files: offers and prices, ideal client, method, voice, stories, rules. Mark as assumption.)
- 8 plugins, each with a mini course, 29 EUR each:
  01 Lead: Who Is Ready to Buy
  02 Follow-Up: Follow Up Without Chasing
  03 Proposal: The Proposal You Don't Have to Write
  04 Session: The Hour After the Session
  05 Onboarding: The Intake You Don't Have to Run
  06 Content: Story Library
  07 CRM: The CRM That Updates Itself
  08 Ads: Ads Without an Agency
- All 8 plugins bundle, 97 EUR.
- Setup Call with a specialist, 297 EUR.
- Connect and Run Kit (contents not specified: assumption, connecting the plugins to the expert's own tools and running them).
- Growth course (contents not specified).
- Strategy session with Donatas Jonikas, PhD.
- Done For You (the work is done for the expert).
Core idea: AI without context works like a confused intern. The expert writes down what lives in their head (offers and prices, ideal client, method, voice, stories, rules) as plain Markdown files; AI works from those files instead of from the internet's average. Promise: Stay human. Automate the rest.
