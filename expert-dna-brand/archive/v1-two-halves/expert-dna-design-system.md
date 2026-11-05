# Expert DNA design system

This file is the single source of truth for everything Expert DNA looks like: the logo, colour, type, layouts, plugin tiles, slides, social posts, ads and web pages. People and AI agents both read it. If a decision is not written here, it is not made again from scratch each time: it is added here.

Version: 1.0. Date: 2026-11-05. Owner: Donatas Jonikas, PhD (StrategicPin, UAB Marketologai).

---

## 1. How an AI uses this file

Before creating any visual, the AI follows this order:

1. Identify the format (slide, social post, ad, web page, book cover, email, plugin tile) and find its section below.
2. Take colours from section 4, type from section 5, grid and spacing from section 6. Introduce no other colours or fonts.
3. Use logo files from `logo/` exactly as supplied. Never redraw, retype or recolour the logo.
4. Check every text and background pair against the contrast table in section 4.3. Use only pairs marked "allowed".
5. Check the text against section 11 (voice) and section 12 (prohibitions).
6. Use only facts from section 2. Never invent numbers, testimonials, client names or claims. Missing data is written as a placeholder in braces, for example `{Client name}`.

---

## 2. Brand essence

Expert DNA is a digital product line for English-speaking coaches, consultants, course creators and trainers who work alone or with a small team. It teaches and equips them to get far more out of AI. AI without context works like a confused intern. The expert writes down what lives in their own head (offers and prices, ideal client, method, voice, stories, rules) as plain Markdown files, and the AI works from those files instead of from the internet's average. That written body of knowledge is the buyer's Expert DNA.

Promise: Stay human. Automate the rest. Clients pay the expert for expertise, personality, empathy and care. AI takes the busywork, so clients get more of the expert.

Personality in five words: clear, calm, practical, confident, human.

It must never feel like: hype, a guru, a tech start-up, "AI magic", a biotech or lab brand.

Product line (prices are working numbers, always treated as placeholders):

- Book: Expert DNA: Stay Human, Automate the Rest, 7 EUR (front offer)
- Expert DNA Starter, 29 EUR (order bump)
- 8 plugins, each with a mini course, 29 EUR each, all 8 for 97 EUR
- Setup Call with a specialist, 297 EUR; Connect and Run Kit; Growth course; strategy session with Donatas Jonikas, PhD; Done For You
- Domain: expertdna.net

Relation to StrategicPin: a relative, not a twin. Shared: neutrals, flat colour, square corners, thin full-width rules, small mono labels, asymmetric layouts. Own: the mark, the accent, the typefaces.

---

## 3. Logo

### 3.1 The mark: "Two halves"

A brain seen from the front. The left hemisphere is solid with two folds: the human part, the expert's judgement. The right hemisphere is five written lines: the expert's knowledge written down and handed to AI. The mark draws the promise: stay human, automate the rest.

Construction (see `logo/logo-rules.png`):

- Unit u. The mark is 9u wide and 8u high.
- Two half circles with radius 4u, separated by a vertical gap of 1u.
- Left half: two folds cut 0.5u wide, with round ends.
- Right half: five lines, each 1u high, 0.75u apart, clipped by the half circle.
- In full colour the left half is ink (or paper on dark) and the lines are accent.

### 3.2 Logo family

All files are in `logo/svg/` (master) and `logo/png/` (512, 1024 and 2048 px wide, transparent background). All text is converted to outlines, so no file depends on installed fonts.

| Version | File name pattern | Use |
|---|---|---|
| Horizontal | expertdna-horizontal-{colourway} | Default. Slides, ads, email, web header |
| Horizontal with tagline | expertdna-horizontal-tagline-{colourway} | Website, social profile, book back |
| Stacked | expertdna-stacked-{colourway} | Square formats, book spine area, merch |
| Stacked with tagline | expertdna-stacked-tagline-{colourway} | Website footer, social avatar banner |
| Mark | expertdna-mark-{colourway} | Favicon, avatar, small spaces |
| Wordmark | expertdna-wordmark-{colourway} | Where the mark already appears nearby |
| Endorsed | expertdna-endorsed-{colourway} | Book, presentations by Donatas: logo, a thin rule, "by Donatas Jonikas, PhD" |

Colourways:

| Colourway | Left half | Lines | Wordmark | Background it sits on |
|---|---|---|---|---|
| colour-on-light | ink | accent | ink | paper or white |
| colour-on-dark | paper | accent | paper | ink |
| black | ink | ink | ink | paper, white, accent field, accent tint |
| white | white | white | white | ink, dark flat photo |
| accent | accent | accent | accent | ink only (one-colour print, merch) |

Rules:

- On an accent field the logo is always the black version.
- The endorsement line is never part of the main logo. It appears only in the endorsed lockup.
- Slides and ads use the logo without tagline. Website and social use the tagline version.
- Favicons: `logo/favicon/` (16, 32, 48, 180, 512 px, favicon.ico, favicon.svg). Social avatar: `logo/favicon/social-avatar-512.png` (paper mark on ink).

### 3.3 Clear space and minimum size

- Clear space: 2u on every side, where 2u is one quarter of the mark height. Nothing enters it.
- Minimum sizes, screen and print: mark 16 px or 5 mm; horizontal 120 px or 30 mm wide; stacked 72 px or 20 mm wide; horizontal with tagline 220 px or 55 mm wide.

### 3.4 Misuse (rendered in `logo/logo-rules.png`)

1. Do not stretch or squash.
2. Do not rotate.
3. Do not swap the halves.
4. Do not use other colours.
5. No gradients.
6. No shadows or glow.
7. Do not add or remove lines.
8. No low-contrast placement (for example paper logo on accent tint).

---

## 4. Colour

### 4.1 Palette

| Name | Token | Hex | Use |
|---|---|---|---|
| Ink | --edna-ink | #101114 | Dark field, all main text on light |
| Paper | --edna-paper | #F4F1EC | Main light background |
| White | --edna-white | #FFFFFF | Secondary light background, cards |
| Accent: Signal red-orange | --edna-accent | #FF5533 | Mark lines, stripe motif, buttons, one full field per set |
| Accent tint | --edna-accent-tint | #FFE1D8 | Callout boxes, highlighted rows |
| Accent deep | --edna-accent-deep | #B32F15 | Small accent text and labels on light backgrounds only |
| Grey | --edna-grey | #66655F | Secondary text on light |
| Grey on dark | --edna-grey-dark | #A3A29C | Secondary text on ink |
| Line | --edna-line | #DCD7CE | Rules and borders on light |
| Line on dark | --edna-line-dark | #34383F | Rules and borders on ink |

Two hues only: the accent family and the neutrals. Ink, paper and white are shared with StrategicPin on purpose. The accent is shifted from StrategicPin orange (#FF7520) toward red, so the two brands read as relatives. Comparison: `tokens/accent-comparison.png`.

Tokens: `tokens/tokens.css` and `tokens/tokens.json`. Contrast data: `tokens/contrast.json`.

### 4.2 Accent rules (checkable)

- The accent covers at most one third of any layout, unless the layout is a full accent field.
- A full accent field is allowed at most once per set: one slide in a deck section, one post in a carousel, one ad in a pair.
- Text on an accent field is always ink. Never white or paper on accent.
- Small text in accent colour on light backgrounds uses accent deep #B32F15, never #FF5533.
- Accent and accent tint are not used as two separate fills in the same small component.
- No gradients, shadows or glow, anywhere.

### 4.3 Contrast (WCAG 2.1, calculated)

AA normal text needs 4.5 to 1. AA large text (24 px and up, or 19 px bold and up) needs 3 to 1.

| Text | Background | Ratio | Normal text | Large text | Status |
|---|---|---|---|---|---|
| Ink | Paper | 16.76 | pass | pass | allowed |
| Ink | White | 18.88 | pass | pass | allowed |
| Ink | Accent | 5.93 | pass | pass | allowed |
| Ink | Accent tint | 15.30 | pass | pass | allowed |
| Paper | Ink | 16.76 | pass | pass | allowed |
| White | Ink | 18.88 | pass | pass | allowed |
| Accent | Ink | 5.93 | pass | pass | allowed |
| Grey on dark | Ink | 7.38 | pass | pass | allowed |
| Accent deep | Paper | 5.59 | pass | pass | allowed |
| Accent deep | White | 6.30 | pass | pass | allowed |
| Accent deep | Accent tint | 5.10 | pass | pass | allowed |
| Grey | Paper | 5.19 | pass | pass | allowed |
| Grey | White | 5.85 | pass | pass | allowed |
| Grey | Accent tint | 4.74 | pass | pass | allowed |
| Accent | White | 3.18 | fail | pass | large text only, 24 px and up |
| White | Accent | 3.18 | fail | pass | forbidden by brand rule (text on accent is ink) |
| Accent | Paper | 2.82 | fail | fail | forbidden |
| Paper | Accent | 2.82 | fail | fail | forbidden |
| Grey | Ink | 3.23 | fail | pass | forbidden, use grey on dark |
| Accent deep | Ink | 3.00 | fail | pass | forbidden |
| Grey on dark | Paper | 2.27 | fail | fail | forbidden |
| Accent | Accent tint | 2.58 | fail | fail | forbidden |

---

## 5. Typography

### 5.1 Typefaces

- Schibsted Grotesk (Regular, Medium, Bold): wordmark, headlines, body, buttons.
- IBM Plex Mono (Regular, Medium): small uppercase labels, plugin numbers, prices in tables, captions of screenshots.

Why Schibsted Grotesk won: it has the most character in the wordmark "Expert DNA" of the five tested (Schibsted Grotesk, Hanken Grotesk, Familjen Grotesk, Onest, Geist), it comes from news publishing, which suits a brand about clear thinking, and it stays readable in long paragraphs. Geist was rejected because it reads as tech start-up; Familjen as too quirky for body text. IBM Plex Mono replaces StrategicPin's JetBrains Mono to keep the brands apart while keeping the label system.

Rules:

- Numbers in prices use proportional figures (do not switch on tabular figures in Schibsted Grotesk: "1,490" spaces badly).
- Headlines: Bold, letter-spacing minus 0.02 em.
- Labels: IBM Plex Mono Medium, uppercase, letter-spacing 0.12 em, preceded by one small accent bar (3 to 1 rectangle).
- Mono is only for short items: labels, numbers, sources, captions. Never for paragraphs.
- Fallback if fonts are missing: Arial and Courier New. Always send PDF, not .pptx.

Font files and install steps: `fonts/` and `fonts/FONTS.md`.

### 5.2 Scale

| Element | Font | Size | Weight | Line height |
|---|---|---|---|---|
| Slide title (title slide) | Schibsted Grotesk | 54 pt | Bold | 1.0 |
| Slide headline | Schibsted Grotesk | 32 pt | Bold | 1.1 |
| Slide body | Schibsted Grotesk | 16 pt | Regular | 1.4 |
| Slide caption | Schibsted Grotesk | 12 pt | Regular | 1.35 |
| Slide label | IBM Plex Mono | 10 pt | Medium, caps | 1.2 |
| Large price or number | Schibsted Grotesk | 60 pt | Bold | 1.0 |
| Web H1 | Schibsted Grotesk | 64 px (40 px under 600 px) | Bold | 1.02 |
| Web H2 | Schibsted Grotesk | 40 px (30 px mobile) | Bold | 1.1 |
| Web H3 | Schibsted Grotesk | 24 px | Bold | 1.25 |
| Web body | Schibsted Grotesk | 18 px | Regular | 1.55 |
| Web button | Schibsted Grotesk | 16 px | Medium | 1.0 |
| Web label | IBM Plex Mono | 12 px | Medium, caps | 1.2 |
| Social headline (1080 px canvas) | Schibsted Grotesk | 60 to 88 pt | Bold | 1.05 |
| Book cover title (1800 px wide) | Schibsted Grotesk | 150 to 180 px | Bold | 0.98 |

Body text on slides is never smaller than 16 pt. Smaller sizes are only for labels, captions, sources and footers.

---

## 6. Grid, spacing and motif

### 6.1 Grid

- Slides: 16:9, 13.333 x 7.5 in. Side margins 0.75 in. 12 columns, gutter 0.2 in.
- Content sits on columns: full width 12; two columns 6 and 6; asymmetric 5 and 7 or 4 and 8; three cards of 4; four cards of 3.
- Web: 12 columns, max content width 1200 px, gutter 24 px, side padding 16 px on mobile, 48 px on desktop.
- Spacing scale (4 px base): 4, 8, 12, 16, 24, 32, 48, 64, 96, 128.

### 6.2 Signature motif: the stripe stack

The stripe stack is the five lines of the mark's right half, used as a graphic element: five horizontal accent bars, bar height to gap 6 to 4.5.

- It means "the part that is handed to AI". Use it where automation, files or plugins are the subject.
- At most once per layout.
- Always bleeds off one edge of the layout (left or right), never floats in the middle.
- Never rotated, never in another colour than accent (or ink on an accent field).

Inherited from the family: thin full-width rules (1 px, line colour) from edge to edge. They separate the label and headline zone from the content.

### 6.3 Layout rules

- Asymmetric: content starts from different grid columns, not always the same margin.
- Square corners on every component. Border radius is 0.
- Generous empty space: at least one third of a slide or post stays empty.
- No frames around whole slides, no underlines under headlines, no coloured strips along edges as decoration.

---

## 7. Imagery

- No stock photography, ever.
- Allowed: real photos of Donatas Jonikas, real screenshots of plugin outputs and files, illustrations built from the brand's own shapes.
- Illustration style: flat, built from the mark's geometry (half circles, folds, lines), one or two colours, no gradients.
- Every screenshot has a one-line caption in IBM Plex Mono saying what the viewer sees.
- Where a photo of a person is needed and none exists, leave a clearly labelled empty slot.

---

## 8. Plugin identity system

Rendered tiles: `applications/plugins/`.

- The plugin glyph is the mark's right hemisphere cut into 8 equal lines. Plugin n has line n in accent; the other seven lines are in line colour.
- All 8 plugins (bundle): all eight lines in accent.
- Expert DNA Starter: the left hemisphere with folds, in accent (the human part you write first).
- Each tile carries: mono label ("PLUGIN 03"), glyph, plugin name, subtitle, badge, price.

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

No third-party icons or pictograms are used for plugins. The number and the glyph line are the identifier.

---

## 9. Components

CSS and renders: `applications/components/` (components.css, components.html, components.png, components-dark.png).

- Primary button: accent fill, ink text, Schibsted Grotesk Medium 16 px, padding 16 x 24 px, square corners.
- Secondary button: transparent, 1.5 px ink outline, ink text.
- Text link: ink text with a 2 px accent underline.
- Product card: white on paper, 1 px line border, mono label, title, price, one button.
- Badges ("Plugin", "Course", "Book"): mono caps 11 px, 1 px border, square.
- Checkout order bump: accent tint box, 3 px accent left bar, one checkbox with one question.
- Input: 1 px ink border, label above in mono caps.
- Callout: accent tint fill, 3 px accent left bar.
- Testimonial: layout only. Quote, name, role, photo slot. Never filled with invented text.

---

## 10. Formats

| Format | Size | File |
|---|---|---|
| Book cover front | 6 x 9 in, 1800 x 2700 px at 300 dpi | applications/book-cover-front.png |
| Social square | 1080 x 1080 | applications/social-1080x1080-*.png |
| Social portrait | 1080 x 1350 | applications/social-1080x1350-*.png |
| Ad pair | 1080 x 1350 | applications/ad-1080x1350-*.png |
| Link preview | 1200 x 630 | applications/link-preview-1200x630.png |
| Email header and footer | 600 px wide | applications/email-*.png |
| Landing hero | responsive HTML | applications/landing/landing-hero.html |
| Slides | 16:9 .pptx, 6 layouts | applications/slides/slide-template.pptx |

Social and ads: logo bottom left, text covers at most 25 percent of the area, one message per post.

---

## 11. Voice (proposal)

Derived only from the brief. To be confirmed by Donatas.

Traits: plain, calm, direct, practical, warm. Speaks to an expert as an equal who values their own judgement.

Do say: "confused intern", "stay human", "what lives in your head", "write it down once", "your files", "more of you for your clients".

Do not say: "AI magic", "10x", "revolutionary", "game-changer", "unlock", "supercharge", "hack", "secret".

Headline patterns:

- Problem in their words: "Your AI works like a confused intern."
- Instruction: "Give it your Expert DNA."
- Contrast: "Stay human. Automate the rest."
- Result without hype: "The proposal you don't have to write."

---

## 12. Prohibitions

- No DNA imagery: no double helix, strands, base-pair ladders, molecules, nodes and bonds, hexagon lab shapes, test tubes.
- No brain clichés: circuit-board brain, glowing brain, gears in a head, lightbulb, robot head, puzzle-piece head, sparkles or stars.
- No purple-blue "AI gradient" look. No gradients, shadows or glow at all.
- No stock photos, icon packs or emoji.
- No long dashes (em dash or en dash) in any text. Use a colon, comma or period. A plain hyphen only for ranges (5-7).
- No invented numbers, testimonials, client names or claims.
- No rounded corners.
- No reuse of the StrategicPin node-cluster mark.

---

## 13. Open points

1. Accent: recommended #FF5533 (Signal red-orange) over StrategicPin #FF7520. Needs Donatas's confirmation.
2. Tagline "Stay human. Automate the rest." is a proposal.
3. Voice notes (section 11) are a proposal.
4. Name check: a web search on 2026-11-05 found no company using "Expert DNA" as a brand with a similar look. DNA Diagnostics Center offers a service called "Expert DNA Review". Expert AG (Swiss electronics retail) uses black type with an orange accent. A formal trademark search was not done.
5. The StrategicPin logo file was not available in the working environment, so the side-by-side squint test was made against the image shared in the chat, not the master file.
6. Prices in all mockups are working numbers and placeholders.
7. The postal address in the email footer is a placeholder.
8. Slide fonts: PowerPoint lists the Medium weight as a separate family, "Schibsted Grotesk Medium". This is how the static font files are named.

---

## 14. File inventory

```
expert-dna-brand/
  phase1-directions.png          Phase 1 contact sheet
  brand-sheet.png                one-page overview, 2400 px wide
  expert-dna-design-system.md    this file
  logo/svg/                      master SVGs, outlined text
  logo/png/                      PNG exports 512, 1024, 2048 px
  logo/favicon/                  favicons, favicon.ico, social avatar
  logo/logo-rules.png            construction, clear space, minimum size, misuse
  fonts/                         font files, licences, FONTS.md
  tokens/                        tokens.css, tokens.json, contrast.json, accent-comparison.png
  applications/                  book cover, social, ads, email, link preview, motion storyboard
  applications/landing/          landing-hero.html and screenshots
  applications/slides/           slide-template.pptx and preview
  applications/plugins/          plugin tiles and overview
  applications/components/       components.css, components.html and renders
  phase1/                        Phase 1 direction SVGs
  _work/                         generator scripts (not for use)
```
