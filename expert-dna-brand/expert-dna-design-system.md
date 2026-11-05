# Expert DNA design system

This file is the single source of truth for everything Expert DNA looks like: logo, colour, type, layouts, product visuals, slides, social posts, ads and web pages. People and AI agents both read it. If a decision is not written here, it is not made again from scratch each time: it is added here.

Version: 2.0. Date: 2026-11-05. Owner: Donatas Jonikas, PhD (StrategicPin, UAB Marketologai).

Version 2.0 replaces version 1.0 ("Two halves" mark, Schibsted Grotesk, paper background). Version 1.0 is kept in `archive/v1-two-halves/` for reference only and is not used.

---

## 1. How an AI uses this file

Before creating any visual, the AI follows this order:

1. Identify the format (slide, social post, ad, web page, product visual, email, plugin tile) and find its section below.
2. Take colours from section 4, type from section 5, grid, spacing and motifs from section 6. Introduce no other colours or fonts.
3. Use logo files from `logo/` exactly as supplied. Never redraw, retype or recolour the logo.
4. Check every text and background pair against section 4.3. Use only pairs marked "allowed".
5. Check the text against section 11 (voice) and section 12 (prohibitions).
6. Use only facts from section 2. Never invent numbers, testimonials, client names or claims. Missing data is written as a placeholder in braces, for example `{Client name}`.
7. For slides, start from `powerpoint/expert-dna-template.pptx` and pick a layout. Do not build slides from scratch.

---

## 2. Brand essence

Expert DNA is a digital product line for English-speaking coaches, consultants, course creators and trainers who work alone or with a small team. It teaches and equips them to get far more out of AI. AI without context works like a confused intern. The expert writes down what lives in their own head (offers and prices, ideal client, method, voice, stories, rules) as plain Markdown files, and the AI works from those files instead of from the internet's average. That written body of knowledge is the buyer's Expert DNA.

Promise: Stay human. Automate the rest. Clients pay the expert for expertise, personality, empathy and care. AI takes the busywork, so clients get more of the expert.

Personality in five words: clear, calm, modern, practical, human.

It must never feel like: hype, a guru, "AI magic", a biotech or lab brand, an old traditional company.

Product line (prices are working numbers, always placeholders):

- Book (title not final), 7 EUR, front offer
- Expert DNA Starter, 29 EUR, order bump
- 8 plugins, each with a mini course, 29 EUR each; all 8 for 97 EUR
- Setup Call with a specialist, 297 EUR
- Connect and Run Kit
- Growth course
- Strategy session with Donatas Jonikas, PhD
- Done For You
- Domain: expertdna.net

Relation to StrategicPin: a relative, not a twin. Shared: ink, flat colour, square corners, thin full-width rules, small mono labels, asymmetric layouts. Own: the mark, the accent, the typefaces, white as the main background.

---

## 3. Logo

### 3.1 The mark: "Half moon and plug"

A half moon (the expert's mind) next to a plug (the connection to AI). The expert plugs what is in their head into AI, and AI runs on it. The plug's two pins also read as lines of written text.

Construction (see `logo/logo-rules.png`), unit u = 6 on a 54 x 48 box:

- Half moon: half disc with radius 4u, flat side facing right.
- Gap of 1u, then the plug bar: 0.58u wide, full height 8u.
- Two pins, 0.58u thick, starting 0.75u right of the bar: the top pin 2.67u long at height 2.33u, the bottom pin 1.83u long at height 5.08u. The pin lengths stay in the ratio 16 to 11.
- In full colour the half moon is ink (white on dark) and the plug is accent.

### 3.2 Logo family

All files are in `logo/svg/` (master) and `logo/png/` (512, 1024 and 2048 px wide, transparent). All text is converted to outlines.

| Version | File name pattern | Use |
|---|---|---|
| Horizontal | expertdna-horizontal-{colourway} | Default: slides, ads, email, web header |
| Horizontal with tagline | expertdna-horizontal-tagline-{colourway} | Website, social profile |
| Stacked | expertdna-stacked-{colourway} | Square formats |
| Stacked with tagline | expertdna-stacked-tagline-{colourway} | Website footer |
| Mark | expertdna-mark-{colourway} | Favicon, avatar, small spaces |
| Wordmark | expertdna-wordmark-{colourway} | Where the mark already appears nearby |
| Endorsed | expertdna-endorsed-{colourway} | Book, presentations by Donatas: logo, a thin rule, "by Donatas Jonikas, PhD" |

| Colourway | Half moon | Plug | Wordmark | Background |
|---|---|---|---|---|
| colour-on-light | ink | accent | ink | white or paper |
| colour-on-dark | white | accent | white | ink |
| black | ink | ink | ink | white, paper, accent field, accent tint |
| white | white | white | white | ink, dark flat photo |
| accent | accent | accent | accent | ink only (one-colour print, merch) |

Rules:

- On an accent field the logo is always the black version.
- Slides and ads use the logo without tagline. Website and social profiles use the tagline version.
- The endorsement line is never part of the main logo.
- Favicons: `logo/favicon/` (16, 32, 48, 180, 512 px, favicon.ico, favicon.svg). Social avatar: `logo/favicon/social-avatar-512.png` (white half moon, accent plug on ink).
- Product visuals for sales pages carry no logo and no brand name.

### 3.3 Clear space and minimum size

- Clear space: 2u on every side (one quarter of the mark height).
- Minimum sizes: mark 16 px or 5 mm; horizontal 120 px or 30 mm wide; stacked 72 px or 20 mm wide; horizontal with tagline 220 px or 55 mm wide.

### 3.4 Misuse (rendered in `logo/logo-rules.png`)

Do not stretch, rotate, swap the half moon and the plug, use other colours, add gradients, add shadows or glow, change the pin lengths, or place it with low contrast.

---

## 4. Colour

### 4.1 Palette

| Name | Token | Hex | Use |
|---|---|---|---|
| Ink | --edna-ink | #101114 | Dark field, all main text on light |
| White | --edna-white | #FFFFFF | Main background |
| Paper | --edna-paper | #F4F3F0 | Secondary light surface: panels, before states |
| Accent: Signal red-orange | --edna-accent | #FF5533 | Plug, pins motif, buttons, one full field per set |
| Accent tint | --edna-accent-tint | #FFE1D8 | Callouts, highlighted rows |
| Accent deep | --edna-accent-deep | #B32F15 | Small accent text on light backgrounds only |
| Grey | --edna-grey | #66655F | Secondary text on light |
| Grey on dark | --edna-grey-dark | #A3A29C | Secondary text on ink |
| Line | --edna-line | #E2E0DB | Rules and borders on light |
| Line on dark | --edna-line-dark | #2E3036 | Rules and borders on ink |
| Surface dark | --edna-surface-dark | #1A1B1F | Raised cards on ink |

Tokens: `tokens/tokens.css`, `tokens/tokens.json`. Contrast data: `tokens/contrast.json`.

### 4.2 Accent rules (checkable)

- White is the default background. Paper is a secondary surface, never the whole page by default.
- The accent covers at most one third of any layout, unless the layout is a full accent field.
- A full accent field: at most once per set (one slide per deck section, one post per carousel, one ad per pair).
- Text on accent is always ink. Never white, paper or grey on accent.
- Small accent text on light backgrounds uses accent deep #B32F15.
- No gradients, shadows or glow, anywhere.

### 4.3 Contrast (WCAG 2.1, calculated)

AA normal text needs 4.5 to 1; AA large text (24 px and up, or 19 px bold and up) needs 3 to 1.

| Text | Background | Ratio | Status |
|---|---|---|---|
| Ink | White | 18.88 | allowed |
| Ink | Paper | 17.01 | allowed |
| Ink | Accent | 5.93 | allowed |
| Ink | Accent tint | 15.30 | allowed |
| White | Ink | 18.88 | allowed |
| White | Surface dark | 17.21 | allowed |
| Accent | Ink | 5.93 | allowed |
| Accent | Surface dark | 5.41 | allowed |
| Grey on dark | Ink | 7.38 | allowed |
| Grey on dark | Surface dark | 6.72 | allowed |
| Accent deep | White | 6.30 | allowed |
| Accent deep | Paper | 5.68 | allowed |
| Accent deep | Accent tint | 5.10 | allowed |
| Grey | White | 5.85 | allowed |
| Grey | Paper | 5.27 | allowed |
| Grey | Accent tint | 4.74 | allowed |
| Accent | White | 3.18 | large text only (24 px and up) |
| White | Accent | 3.18 | forbidden by brand rule |
| Accent | Paper | 2.87 | forbidden |
| Grey | Ink | 3.23 | forbidden, use grey on dark |
| Accent deep | Ink | 3.00 | forbidden |
| Grey on dark | White | 2.56 | forbidden |

---

## 5. Typography

### 5.1 Typefaces

- Hanken Grotesk (Regular, Medium, Bold): wordmark, headlines, body, buttons.
- IBM Plex Mono (Regular, Medium): small uppercase labels, numbers, captions.

Why Hanken Grotesk: in the modernisation study it gave the most current, light and calm result with the plug mark, it reads well in long paragraphs and has natural numerals for prices. Headlines use Medium, not Bold: the lighter weight is a large part of what keeps the brand modern.

Rules:

- Headlines: Medium, letter-spacing minus 0.03 em, line height 1.02 to 1.08.
- Body: Regular, line height 1.5.
- Bold only for small emphasis inside UI, never for headlines.
- Labels: IBM Plex Mono Medium, uppercase, letter-spacing 0.12 em.
- Mono is only for short items: labels, numbers, sources, captions. Never paragraphs.
- Fallback if fonts are missing: Arial and Courier New. Always send PDF, not .pptx.

Font files and install steps: `fonts/` and `fonts/FONTS.md`.

### 5.2 Scale

| Element | Font | Size | Weight | Line height |
|---|---|---|---|---|
| Slide title | Hanken Grotesk | 54 pt | Medium | 1.02 |
| Slide headline | Hanken Grotesk | 32 pt | Medium | 1.08 |
| Slide body | Hanken Grotesk | 16 pt | Regular | 1.4 |
| Slide caption | Hanken Grotesk | 12 pt | Regular | 1.35 |
| Slide label | IBM Plex Mono | 10 pt | Medium, caps | 1.2 |
| Large price or number | Hanken Grotesk | 60 pt | Medium | 1.0 |
| Web H1 | Hanken Grotesk | 64 px (40 px under 600 px) | Medium | 1.02 |
| Web H2 | Hanken Grotesk | 40 px (30 px mobile) | Medium | 1.08 |
| Web H3 | Hanken Grotesk | 24 px | Medium | 1.25 |
| Web body | Hanken Grotesk | 18 px | Regular | 1.55 |
| Web button | Hanken Grotesk | 16 px | Medium | 1.0 |
| Web label | IBM Plex Mono | 12 px | Medium, caps | 1.2 |
| Social headline (1080 px canvas) | Hanken Grotesk | 64 to 96 px | Medium | 1.04 |
| Product visual headline (2400 px canvas) | Hanken Grotesk | 120 to 180 px | Medium | 1.02 |

Slide body text is never smaller than 16 pt.

---

## 6. Grid, spacing and motifs

### 6.1 Grid

- Slides: 16:9, 13.333 x 7.5 in, side margins 0.75 in, 12 columns, gutter 0.2 in.
- Content on columns: 12; 6 and 6; 5 and 7 or 4 and 8; three cards of 4; four cards of 3.
- Web: 12 columns, max content width 1200 px, gutter 24 px, side padding 16 px mobile, 48 px desktop.
- Spacing scale (4 px base): 4, 8, 12, 16, 24, 32, 48, 64, 96, 128.

### 6.2 Motifs (from the mark)

One main motif per layout.

1. Half moon: a large solid half disc cropped by an edge of the layout. It stands for the human, the expert's mind. Ink on light, white or ink on dark, ink on accent.
2. Pins: two horizontal bars with lengths in the ratio 16 to 11, optionally with the vertical plug bar. They stand for the connection to AI. Usually accent. Always bleed off one edge or connect to something; never float alone in the middle.
3. Thin rules: 1 px full-width lines in line colour, from edge to edge.

Layout rules: generous white space (at least one third of a slide or post empty), asymmetric, square corners (border radius 0), flat. No frames around whole slides, no underlines under headlines, no decorative coloured strips.

---

## 7. Imagery

- No stock photography, ever.
- Allowed: real photos of Donatas Jonikas, real screenshots of plugin outputs and files, illustrations built from the mark's geometry (half discs, bars, squares).
- Illustration style: flat, one or two colours plus neutrals, no gradients.
- Every screenshot has a one-line caption in IBM Plex Mono saying what the viewer sees.
- Where a photo of a person is needed and none exists, leave a clearly labelled empty slot.

---

## 8. Product visuals (sales pages)

Files: `product-visuals/`. Every product (except the book) has the same five styles, so any page can pick one style and stay consistent:

| No. | Style | What it shows |
|---|---|---|
| S1 | Interface | A clean app or document window showing what the product produces |
| S2 | Statement | Full accent field, one large outcome headline, an ink half moon |
| S3 | What's inside | Dark field, an exploded stack of cards listing the contents |
| S4 | Before / After | Paper "before" with scattered fragments, white "after" with order, the plug as the divider |
| S5 | Plug-in | Abstract: half moon, plug and a product-specific geometric form, large product number |

Rules: 2400 x 1600 px, no logo, no brand name, neutral mock data only, no invented numbers.

## 9. Plugin identity

Rendered tiles: `applications/plugins/`. The plugin glyph is the plug bar with eight pin positions. Plugin n lights pin n in accent; the other pins are line colour. The bundle lights all eight. The Starter is the half moon in accent.

| No. | Plugin | Subtitle |
|---|---|---|
| 01 | Lead | Who Is Ready to Buy |
| 02 | Follow-Up | Follow Up Without Chasing |
| 03 | Proposal | The Proposal You Don't Have to Write |
| 04 | Session | The Hour After the Session |
| 05 | Onboarding | The Intake You Don't Have to Run |
| 06 | Content | Story Library |
| 07 | CRM | The CRM That Updates Itself |
| 08 | Ads | Ads Without an Agency |

No third-party icons or pictograms.

## 10. Components and formats

Components: `applications/components/` (components.css with --edna-* variables, renders light and dark). Square corners everywhere.

- Primary button: accent fill, ink text, Hanken Grotesk Medium 16 px, padding 16 x 24 px.
- Secondary button: 1.5 px ink outline, ink text.
- Text link: ink with a 2 px accent underline.
- Product card, badges (Plugin, Course, Book), order bump box, input, callout (accent tint, 3 px accent left bar), testimonial layout (placeholder only).

| Format | Size | File |
|---|---|---|
| Product visual | 2400 x 1600 | product-visuals/{product}/ |
| Social square / portrait | 1080 x 1080 / 1080 x 1350 | applications/social-*.png |
| Ad pair | 1080 x 1350 | applications/ad-*.png |
| Link preview | 1200 x 630 | applications/link-preview-1200x630.png |
| Email header and footer | 600 px wide | applications/email-*.png |
| Landing hero | responsive HTML | applications/landing/landing-hero.html |
| Slides | 16:9, 18 layouts | powerpoint/expert-dna-template.pptx |

Social and ads: logo bottom left, text at most 25 percent of the area, one message per post.

---

## 11. Voice (proposal)

Traits: plain, calm, direct, practical, warm. Speaks to an expert as an equal who values their own judgement.

Do say: "confused intern", "stay human", "what lives in your head", "write it down once", "plug in", "your files", "more of you for your clients".

Do not say: "AI magic", "10x", "revolutionary", "game-changer", "unlock", "supercharge", "hack", "secret".

Headline patterns: problem in their words ("Your AI works like a confused intern."); instruction ("Give it your Expert DNA."); contrast ("Stay human. Automate the rest."); result without hype ("The proposal you don't have to write.").

---

## 12. Prohibitions

- No DNA imagery: helix, strands, base pairs, molecules, nodes and bonds, hexagons, test tubes.
- No brain clichés: circuit brain, glowing brain, gears, lightbulb, robot head, puzzle head, sparkles.
- No purple-blue AI gradient look. No gradients, shadows or glow at all.
- No stock photos, icon packs or emoji.
- No long dashes (em dash or en dash). Use a colon, comma or period. Plain hyphen only for ranges (5-7).
- No invented numbers, testimonials, client names or claims.
- No rounded corners.
- No reuse of the StrategicPin node-cluster mark.

---

## 13. Open points

1. Accent #FF5533 versus StrategicPin #FF7520: kept #FF5533, confirm.
2. Tagline "Stay human. Automate the rest." is a proposal.
3. Voice (section 11) is a proposal.
4. Name and mark check: no formal trademark search has been done. A half circle with lines is a simple form; a similarity check is recommended before public launch.
5. Contents of Expert DNA Starter, Connect and Run Kit and Growth course are not defined in the brief; product visuals use working assumptions listed in `product-visuals/README.md`.
6. Book visuals are not made until the title is final.
7. Prices in all mockups are placeholders. Email footer postal address is a placeholder.
8. PowerPoint lists the Medium weight as a separate family, "Hanken Grotesk Medium".

---

## 14. File inventory

```
expert-dna-brand/
  expert-dna-design-system.md    this file
  brand-sheet.png                one-page overview
  logo/svg, logo/png, logo/favicon, logo/logo-rules.png
  fonts/                         Hanken Grotesk, IBM Plex Mono, licences, FONTS.md
  tokens/                        tokens.css, tokens.json, contrast.json
  product-visuals/               5 styles x 15 products, overview, README
  powerpoint/                    expert-dna-template.pptx, preview, HOW-TO-USE.md
  applications/                  social, ads, email, link preview, landing, components, plugins
  archive/v1-two-halves/         previous version, not for use
  phase1-directions.png, modern-study.png, plug-study*.png   exploration history
  _work/                         generator scripts (not for use)
```
