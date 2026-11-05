// Expert DNA PowerPoint template v2. Run: NODE_PATH=<scratch>/node_modules node build.js
const path = require('path');
const fs = require('fs');
const PptxGenJS = require('pptxgenjs');
const JSZip = require('jszip');

const ROOT = path.resolve(__dirname, '..', '..');
const OUT = path.join(ROOT, 'powerpoint', 'expert-dna-template.pptx');
const LOGO = (v) => path.join(ROOT, 'logo', 'png', `expertdna-horizontal-${v}-1024.png`);

// ---------- tokens ----------
const K = {
  ink: '101114', white: 'FFFFFF', paper: 'F4F3F0', accent: 'FF5533', tint: 'FFE1D8',
  deep: 'B32F15', grey: '66655F', greyDark: 'A3A29C', line: 'E2E0DB', lineDark: '2E3036', surface: '1A1B1F',
};
const F = { reg: 'Hanken Grotesk', med: 'Hanken Grotesk Medium', mono: 'IBM Plex Mono Medium' };
const W = 13.333, H = 7.5, M = 0.75;
const CW = (W - 2 * M - 11 * 0.2) / 12;
const cx = (i) => M + i * (CW + 0.2);           // column start, 0-based
const sp = (n) => n * CW + (n - 1) * 0.2;       // span width
const Y = { label: 0.62, head: 0.98, rule: 2.1, top: 2.42, bottom: 6.6, foot: 6.88 };
const LOGO_H = 0.24, LOGO_W = LOGO_H * 1024 / 213;

// ---------- master helpers ----------
const rect = (x, y, w, h, color) => ({ rect: { x, y, w, h, fill: { color }, line: { type: 'none' } } });
const hline = (x, y, w, color, pt = 0.75) => ({ line: { x, y, w, h: 0, line: { color, width: pt } } });
const halfMoon = (x, y, d, color) => ({
  text: { text: '', options: { shape: 'pie', x, y, w: d, h: d, angleRange: [90, 270], fill: { color }, line: { type: 'none' } } },
});
const ph = (name, type, x, y, w, h, o = {}) => ({
  placeholder: {
    options: Object.assign({ name, type, x, y, w, h, margin: 0, align: 'left', valign: 'top', fontFace: F.reg, fontSize: 16, color: K.ink }, o),
    text: o.prompt || '',
  },
});
function footer(theme) {
  const dark = theme === 'dark', acc = theme === 'accent';
  const lineC = dark ? K.lineDark : acc ? K.ink : K.line;
  const logo = dark ? 'colour-on-dark' : acc ? 'black' : 'colour-on-light';
  return [
    hline(0, Y.foot, W, lineC),
    { image: { x: M, y: 7.03, w: LOGO_W, h: LOGO_H, path: LOGO(logo) } },
  ];
}
const slideNum = (theme) => ({ x: W - M - 0.8, y: 7.0, w: 0.8, h: 0.3, fontFace: F.mono, fontSize: 9, align: 'right', color: theme === 'dark' ? K.greyDark : theme === 'accent' ? K.ink : K.grey });
function labelBar(theme, y = Y.label) {
  return rect(M, y + 0.11, 0.16, 0.05, theme === 'accent' ? K.ink : K.accent);
}
const labelPh = (theme, prompt = 'LABEL', y = Y.label, x = M + 0.26, w = sp(8)) =>
  ph('label', 'body', x, y, w, 0.28, { fontFace: F.mono, fontSize: 10, charSpacing: 1.2, color: theme === 'dark' ? K.greyDark : theme === 'accent' ? K.ink : K.deep, prompt });
const headPh = (theme, prompt = 'Headline in one or two lines', w = sp(10), y = Y.head, size = 32) =>
  ph('headline', 'title', M, y, w, 1.0, { fontFace: F.med, fontSize: size, color: theme === 'dark' ? K.white : K.ink, lineSpacingMultiple: 0.98, prompt });
const ruleFull = (theme, y = Y.rule) => hline(0, y, W, theme === 'dark' ? K.lineDark : K.line);
const bodyOpts = (o = {}) => Object.assign({ fontFace: F.reg, fontSize: 16, color: K.ink, lineSpacingMultiple: 1.25, paraSpaceAfter: 6 }, o);

const pptx = new PptxGenJS();
pptx.layout = 'LAYOUT_WIDE';
pptx.author = 'Donatas Jonikas, PhD';
pptx.company = 'StrategicPin';
pptx.title = 'Expert DNA template';
pptx.theme = { headFontFace: F.med, bodyFontFace: F.reg };

function master(title, theme, objects) {
  const bg = theme === 'dark' ? K.ink : theme === 'accent' ? K.accent : K.white;
  pptx.defineSlideMaster({ title, background: { color: bg }, objects: [...objects, ...footer(theme)], slideNumber: slideNum(theme) });
}

// 01 Title
master('01 Title', 'dark', [
  halfMoon(W - 3.0, 0.55, 6.0, K.white),
  labelBar('dark', 0.9), labelPh('dark', 'LABEL', 0.9),
  ph('title', 'title', M, 1.45, sp(8), 2.4, { fontFace: F.med, fontSize: 54, color: K.white, lineSpacingMultiple: 0.95, prompt: 'Presentation title' }),
  ph('subtitle', 'body', M, 4.25, sp(7), 0.9, bodyOpts({ color: K.greyDark, fontSize: 18, prompt: 'Subtitle or client name' })),
  ph('meta', 'body', M, 5.6, sp(7), 0.6, { fontFace: F.mono, fontSize: 10, charSpacing: 1.2, color: K.white, prompt: 'PRESENTER / DATE' }),
]);
// 02 Agenda
master('02 Agenda', 'light', [
  labelBar('light'), labelPh('light', 'AGENDA'), headPh('light', 'What we cover today', sp(7)), ruleFull('light'),
  ph('body', 'body', cx(4), Y.top, sp(8), 4.1, bodyOpts({ fontSize: 20, paraSpaceAfter: 14, prompt: 'Agenda item' })),
]);
// 03 Section divider
master('03 Section divider', 'accent', [
  halfMoon(W - 2.5, 1.75, 5.0, K.ink),
  labelBar('accent'), labelPh('accent', 'SECTION'),
  ph('number', 'body', M, 1.5, sp(4), 1.1, { fontFace: F.med, fontSize: 60, color: K.ink, prompt: '01' }),
  hline(0, 3.05, W - 2.5, K.ink),
  ph('headline', 'title', M, 3.35, sp(8), 2.0, { fontFace: F.med, fontSize: 54, color: K.ink, lineSpacingMultiple: 0.95, prompt: 'Section title' }),
]);
// 04 Statement
master('04 Statement', 'light', [
  labelBar('light'), labelPh('light', 'LABEL'),
  ph('headline', 'title', M, 1.2, sp(10), 2.6, { fontFace: F.med, fontSize: 54, color: K.ink, lineSpacingMultiple: 0.95, prompt: 'One clear statement' }),
  ruleFull('light', 4.25),
  ph('body', 'body', cx(6), 4.6, sp(6), 1.8, bodyOpts({ prompt: 'One or two sentences that support the statement.' })),
  rect(cx(0), 4.66, 1.8, 0.13, K.accent), rect(cx(0), 5.06, 1.24, 0.13, K.accent),
]);
// 05 Content with label
master('05 Content with label', 'light', [
  labelBar('light'), labelPh('light'), headPh('light'), ruleFull('light'),
  ph('body', 'body', M, Y.top, sp(8), 3.7, bodyOpts({ prompt: 'Body text, 16 pt. Keep it short.' })),
  ph('caption', 'body', M, 6.3, sp(8), 0.35, { fontFace: F.reg, fontSize: 12, color: K.grey, prompt: 'Caption or source' }),
]);
// 06 Two columns
master('06 Two columns', 'light', [
  labelBar('light'), labelPh('light'), headPh('light'), ruleFull('light'),
  ph('leftHead', 'body', M, Y.top, sp(5), 0.5, { fontFace: F.med, fontSize: 20, prompt: 'Left heading' }),
  ph('leftBody', 'body', M, Y.top + 0.6, sp(5), 3.4, bodyOpts({ prompt: 'Left text' })),
  ph('rightHead', 'body', cx(6), Y.top, sp(6), 0.5, { fontFace: F.med, fontSize: 20, prompt: 'Right heading' }),
  ph('rightBody', 'body', cx(6), Y.top + 0.6, sp(6), 3.4, bodyOpts({ prompt: 'Right text' })),
]);
// 07 Three cards
const cards = [];
[0, 4, 8].forEach((c, i) => {
  cards.push(rect(cx(c), Y.top, sp(4), 4.1, K.paper));
  cards.push(ph(`num${i + 1}`, 'body', cx(c) + 0.25, Y.top + 0.25, sp(4) - 0.5, 0.3, { fontFace: F.mono, fontSize: 10, charSpacing: 1.2, color: K.deep, prompt: `0${i + 1}` }));
  cards.push(ph(`cardHead${i + 1}`, 'body', cx(c) + 0.25, Y.top + 0.7, sp(4) - 0.5, 0.9, { fontFace: F.med, fontSize: 22, lineSpacingMultiple: 1.0, prompt: 'Card title' }));
  cards.push(ph(`cardBody${i + 1}`, 'body', cx(c) + 0.25, Y.top + 1.75, sp(4) - 0.5, 2.1, bodyOpts({ prompt: 'Card text' })));
});
master('07 Three cards', 'light', [labelBar('light'), labelPh('light'), headPh('light'), ruleFull('light'), ...cards]);
// 08 Process in 4 steps
const steps = [];
[0, 3, 6, 9].forEach((c, i) => {
  steps.push(rect(cx(c), Y.top, i === 0 ? sp(3) : 0.6, 0.07, i === 0 ? K.accent : K.ink));
  steps.push(ph(`stepNum${i + 1}`, 'body', cx(c), Y.top + 0.3, sp(3), 0.3, { fontFace: F.mono, fontSize: 10, charSpacing: 1.2, color: K.deep, prompt: `STEP 0${i + 1}` }));
  steps.push(ph(`stepHead${i + 1}`, 'body', cx(c), Y.top + 0.75, sp(3), 0.9, { fontFace: F.med, fontSize: 22, lineSpacingMultiple: 1.0, prompt: 'Step title' }));
  steps.push(ph(`stepBody${i + 1}`, 'body', cx(c), Y.top + 1.8, sp(3), 2.2, bodyOpts({ prompt: 'What happens in this step' })));
});
master('08 Process in 4 steps', 'light', [labelBar('light'), labelPh('light', 'PROCESS'), headPh('light'), ruleFull('light'), ...steps]);
// 09 Timeline
const tl = [hline(M, 3.3, W - 2 * M, K.ink, 1)];
[0, 3, 6, 9].forEach((c, i) => {
  tl.push(rect(cx(c), 3.15, 0.3, 0.3, i === 0 ? K.accent : K.ink));
  tl.push(ph(`when${i + 1}`, 'body', cx(c), Y.top, sp(3), 0.3, { fontFace: F.mono, fontSize: 10, charSpacing: 1.2, color: K.deep, prompt: `WEEK 0${i + 1}` }));
  tl.push(ph(`what${i + 1}`, 'body', cx(c), 3.75, sp(3), 0.8, { fontFace: F.med, fontSize: 20, lineSpacingMultiple: 1.0, prompt: 'Milestone' }));
  tl.push(ph(`detail${i + 1}`, 'body', cx(c), 4.6, sp(3), 1.9, bodyOpts({ prompt: 'What is delivered' })));
});
master('09 Timeline', 'light', [labelBar('light'), labelPh('light', 'TIMELINE'), headPh('light'), ruleFull('light'), ...tl]);
// 10 Comparison
master('10 Comparison', 'light', [
  rect(W / 2, 0, W / 2, Y.foot, K.paper),
  rect(W / 2 - 0.06, 0, 0.12, Y.foot, K.accent),
  rect(M, Y.label + 0.11, 0.16, 0.05, K.ink),
  ph('leftLabel', 'body', M + 0.26, Y.label, sp(5), 0.28, { fontFace: F.mono, fontSize: 10, charSpacing: 1.2, color: K.grey, prompt: 'BEFORE' }),
  ph('headline', 'title', M, Y.head, sp(5) + 0.2, 1.0, { fontFace: F.med, fontSize: 32, prompt: 'Without' }),
  ph('leftBody', 'body', M, Y.top, sp(5) + 0.2, 4.0, bodyOpts({ paraSpaceAfter: 12, prompt: 'Point' })),
  rect(W / 2 + 0.5, Y.label + 0.11, 0.16, 0.05, K.accent),
  ph('rightLabel', 'body', W / 2 + 0.76, Y.label, sp(5), 0.28, { fontFace: F.mono, fontSize: 10, charSpacing: 1.2, color: K.deep, prompt: 'AFTER' }),
  ph('rightHead', 'body', W / 2 + 0.5, Y.head, sp(5) + 0.2, 1.0, { fontFace: F.med, fontSize: 32, prompt: 'With' }),
  ph('rightBody', 'body', W / 2 + 0.5, Y.top, sp(5) + 0.2, 4.0, bodyOpts({ paraSpaceAfter: 12, prompt: 'Point' })),
  hline(0, Y.rule, W, K.line),
]);
// 11 Scope and deliverables table (table added per slide)
master('11 Scope and deliverables', 'light', [labelBar('light'), labelPh('light', 'SCOPE'), headPh('light'), ruleFull('light'),
  ph('caption', 'body', M, 6.3, sp(10), 0.35, { fontFace: F.reg, fontSize: 12, color: K.grey, prompt: 'Caption' })]);
// 12 Offer and price
const offers = [];
[0, 4, 8].forEach((c, i) => {
  const hi = i === 1;
  offers.push(rect(cx(c), Y.top, sp(4), 3.75, hi ? K.tint : K.white));
  if (!hi) offers.push({ rect: { x: cx(c), y: Y.top, w: sp(4), h: 3.75, fill: { type: 'none' }, line: { color: K.ink, width: 0.75 } } });
  offers.push(rect(cx(c), Y.top, sp(4), 0.07, hi ? K.accent : K.ink));
  offers.push(ph(`optLabel${i + 1}`, 'body', cx(c) + 0.25, Y.top + 0.3, sp(4) - 0.5, 0.3, { fontFace: F.mono, fontSize: 10, charSpacing: 1.2, color: K.deep, prompt: `OPTION 0${i + 1}` }));
  offers.push(ph(`optName${i + 1}`, 'body', cx(c) + 0.25, Y.top + 0.7, sp(4) - 0.5, 0.9, { fontFace: F.med, fontSize: 20, lineSpacingMultiple: 1.0, prompt: 'Option name' }));
  offers.push(ph(`optBody${i + 1}`, 'body', cx(c) + 0.25, Y.top + 1.6, sp(4) - 0.5, 0.9, bodyOpts({ prompt: 'What is included' })));
  offers.push(ph(`price${i + 1}`, 'body', cx(c) + 0.25, Y.top + 2.65, sp(4) - 0.5, 0.95, { fontFace: F.med, fontSize: 60, valign: 'bottom', prompt: '0 EUR' }));
});
master('12 Offer and price', 'light', [labelBar('light'), labelPh('light', 'OFFER'), headPh('light'), ruleFull('light'), ...offers,
  ph('caption', 'body', M, 6.3, sp(10), 0.35, { fontFace: F.reg, fontSize: 12, color: K.grey, prompt: 'Prices are working numbers.' })]);
// 13 Quote
master('13 Quote', 'light', [
  labelBar('light'), labelPh('light', 'IN THEIR WORDS'),
  ph('quote', 'body', M, 1.3, sp(8), 3.4, { fontFace: F.med, fontSize: 32, lineSpacingMultiple: 1.08, prompt: 'Quote' }),
  hline(M, 5.05, sp(8), K.line),
  ph('name', 'body', M, 5.3, sp(8), 0.35, { fontFace: F.med, fontSize: 16, prompt: 'Name' }),
  ph('role', 'body', M, 5.7, sp(8), 0.3, { fontFace: F.mono, fontSize: 10, charSpacing: 1.2, color: K.grey, prompt: 'ROLE, COMPANY' }),
  rect(cx(9), 1.3, sp(3), sp(3) * 1.25, K.paper),
  ph('photo', 'pic', cx(9), 1.3, sp(3), sp(3) * 1.25, { prompt: 'Photo' }),
]);
// 14 Image and text
master('14 Image and text', 'light', [
  rect(0, 0, cx(6) - 0.2, Y.foot, K.paper),
  ph('image', 'pic', 0, 0, cx(6) - 0.2, Y.foot, { prompt: 'Image' }),
  rect(cx(7), Y.label + 0.11, 0.16, 0.05, K.accent),
  ph('label', 'body', cx(7) + 0.26, Y.label, sp(5), 0.28, { fontFace: F.mono, fontSize: 10, charSpacing: 1.2, color: K.deep, prompt: 'LABEL' }),
  ph('headline', 'title', cx(7), Y.head, sp(5), 1.6, { fontFace: F.med, fontSize: 32, lineSpacingMultiple: 0.98, prompt: 'Headline' }),
  ph('body', 'body', cx(7), 2.8, sp(5), 3.0, bodyOpts({ prompt: 'Text' })),
  ph('caption', 'body', cx(7), 6.3, sp(5), 0.35, { fontFace: F.reg, fontSize: 12, color: K.grey, prompt: 'Caption: what the viewer sees' }),
]);
// 15 Lesson opener
master('15 Lesson opener', 'dark', [
  labelBar('dark', 0.9), labelPh('dark', 'MODULE 01 / LESSON 01', 0.9),
  ph('title', 'title', M, 1.45, sp(9), 2.4, { fontFace: F.med, fontSize: 54, color: K.white, lineSpacingMultiple: 0.95, prompt: 'Lesson title' }),
  hline(M, 4.3, sp(7), K.lineDark),
  ph('goalLabel', 'body', M, 4.55, sp(7), 0.3, { fontFace: F.mono, fontSize: 10, charSpacing: 1.2, color: K.greyDark, prompt: 'AFTER THIS LESSON YOU CAN' }),
  ph('goal', 'body', M, 4.95, sp(7), 1.4, bodyOpts({ color: K.white, fontSize: 20, prompt: 'Learning goal' })),
  rect(W - 3.2, 4.55, 3.2, 0.2, K.accent), rect(W - 2.2, 5.15, 2.2, 0.2, K.accent),
]);
// 16 Exercise
const fields = [];
[0, 1, 2].forEach((i) => {
  const y = Y.top + i * 1.35;
  fields.push(rect(cx(6), y, sp(6), 1.15, K.paper));
  fields.push(ph(`field${i + 1}`, 'body', cx(6) + 0.2, y + 0.15, sp(6) - 0.4, 0.3, { fontFace: F.mono, fontSize: 10, charSpacing: 1.2, color: K.grey, prompt: `FIELD 0${i + 1}` }));
  fields.push(hline(cx(6) + 0.2, y + 0.9, sp(6) - 0.4, K.line));
});
master('16 Exercise', 'light', [
  labelBar('light'), labelPh('light', 'EXERCISE'), headPh('light', 'Exercise title', sp(8)), ruleFull('light'),
  ph('time', 'body', cx(9), Y.label, sp(3), 0.28, { fontFace: F.mono, fontSize: 10, charSpacing: 1.2, color: K.grey, align: 'right', prompt: '00 MIN' }),
  ph('body', 'body', M, Y.top, sp(5), 3.9, bodyOpts({ paraSpaceAfter: 10, prompt: 'Step' })),
  ...fields,
]);
// 17 Key takeaways
const tk = [];
[0, 1, 2].forEach((i) => {
  const y = Y.top + i * 1.35;
  tk.push(hline(M, y, W - 2 * M, i === 0 ? K.ink : K.line));
  tk.push(ph(`n${i + 1}`, 'body', M, y + 0.25, sp(1), 0.3, { fontFace: F.mono, fontSize: 10, charSpacing: 1.2, color: K.deep, prompt: `0${i + 1}` }));
  tk.push(ph(`take${i + 1}`, 'body', cx(2), y + 0.2, sp(9), 0.9, { fontFace: F.med, fontSize: 22, lineSpacingMultiple: 1.05, prompt: 'Takeaway' }));
});
master('17 Key takeaways', 'light', [labelBar('light'), labelPh('light', 'KEY TAKEAWAYS'), headPh('light'), ...tk]);
// 18 Closing and contact
master('18 Closing and contact', 'dark', [
  halfMoon(W - 3.0, 0.55, 6.0, K.white),
  labelBar('dark', 0.9), labelPh('dark', 'NEXT STEP', 0.9),
  ph('title', 'title', M, 1.45, sp(8), 2.4, { fontFace: F.med, fontSize: 54, color: K.white, lineSpacingMultiple: 0.95, prompt: 'Closing line' }),
  hline(M, 4.3, sp(7), K.lineDark),
  ph('contact', 'body', M, 4.6, sp(7), 1.8, { fontFace: F.mono, fontSize: 12, charSpacing: 1.0, color: K.white, lineSpacingMultiple: 1.5, prompt: 'CONTACT' }),
]);

// ---------- example slides ----------
const t = (s, name, text, o = {}) => s.addText(text, Object.assign({ placeholder: name }, o));
const bullets = (arr, o = {}) => arr.map((x) => ({ text: x, options: Object.assign({ bullet: { indent: 18 }, breakLine: true }, o) }));
const numbered = (arr) => arr.map((x) => ({ text: x, options: { bullet: { type: 'number', indent: 28 }, breakLine: true } }));

let s = pptx.addSlide({ masterName: '01 Title' });
t(s, 'label', 'EXPERT DNA / PROPOSAL');
t(s, 'title', 'Stay human. Automate the rest.');
t(s, 'subtitle', 'Proposal for {Client name}');
t(s, 'meta', 'DONATAS JONIKAS, PHD / {DATE}');

s = pptx.addSlide({ masterName: '02 Agenda' });
t(s, 'label', 'AGENDA'); t(s, 'headline', 'What we cover today');
t(s, 'body', numbered(['Why AI without context fails', 'What goes into your Expert DNA', 'The 8 plugins', 'How we start']));

s = pptx.addSlide({ masterName: '03 Section divider' });
t(s, 'label', 'SECTION'); t(s, 'number', '02'); t(s, 'headline', 'Write down what lives in your head');

s = pptx.addSlide({ masterName: '04 Statement' });
t(s, 'label', 'THE PROBLEM'); t(s, 'headline', 'AI without context works like a confused intern.');
t(s, 'body', 'It answers from the internet\'s average. Your Expert DNA gives it your offers, your method, your voice and your rules instead.');

s = pptx.addSlide({ masterName: '05 Content with label' });
t(s, 'label', 'WHAT IS EXPERT DNA'); t(s, 'headline', 'Your knowledge, written down once');
t(s, 'body', bullets(['Offers and prices', 'Ideal client', 'Method', 'Voice and stories', 'Rules you never break']));
t(s, 'caption', 'Plain Markdown files that both people and AI can read.');

s = pptx.addSlide({ masterName: '06 Two columns' });
t(s, 'label', 'HOW IT WORKS'); t(s, 'headline', 'You keep the human part. AI takes the rest.');
t(s, 'leftHead', 'What stays with you'); t(s, 'leftBody', 'Expertise, personality, empathy and care. The things clients pay you for.');
t(s, 'rightHead', 'What AI takes'); t(s, 'rightBody', 'The busywork around the work: follow-ups, proposals, notes, records and first drafts.');

s = pptx.addSlide({ masterName: '07 Three cards' });
t(s, 'label', 'WHAT GOES INTO YOUR EXPERT DNA'); t(s, 'headline', 'Three kinds of files the AI works from');
[['Your offer', 'Offers and prices, and the ideal client each one is for.'], ['Your method', 'How you work, step by step, and the rules you never break.'], ['Your voice', 'How you write and speak, and the stories only you can tell.']]
  .forEach(([h, b], i) => { t(s, `num${i + 1}`, `0${i + 1}`); t(s, `cardHead${i + 1}`, h); t(s, `cardBody${i + 1}`, b); });

s = pptx.addSlide({ masterName: '08 Process in 4 steps' });
t(s, 'label', 'PROCESS'); t(s, 'headline', 'From your head to working plugins');
[['Write it down', 'Your offers, client, method, voice, stories and rules as Markdown files.'], ['Connect', 'Plug your files into the plugins you need.'], ['Run', 'The plugins work from your files, not from the internet\'s average.'], ['Improve', 'Update a file once and every plugin follows.']]
  .forEach(([h, b], i) => { t(s, `stepNum${i + 1}`, `STEP 0${i + 1}`); t(s, `stepHead${i + 1}`, h); t(s, `stepBody${i + 1}`, b); });

s = pptx.addSlide({ masterName: '09 Timeline' });
t(s, 'label', 'TIMELINE'); t(s, 'headline', 'How the work runs');
[['{WEEK 01}', 'Kick-off', '{What is delivered}'], ['{WEEK 02}', 'Expert DNA files', '{What is delivered}'], ['{WEEK 03}', 'Plugins connected', '{What is delivered}'], ['{WEEK 04}', 'Running and handover', '{What is delivered}']]
  .forEach(([a, b, c], i) => { t(s, `when${i + 1}`, a); t(s, `what${i + 1}`, b); t(s, `detail${i + 1}`, c); });

s = pptx.addSlide({ masterName: '10 Comparison' });
t(s, 'leftLabel', 'WITHOUT EXPERT DNA'); t(s, 'headline', 'The confused intern');
t(s, 'leftBody', bullets(['Answers from the internet\'s average', 'Guesses your prices and your offer', 'Writes in nobody\'s voice']));
t(s, 'rightLabel', 'WITH EXPERT DNA'); t(s, 'rightHead', 'Works from your files');
t(s, 'rightBody', bullets(['Knows your offers, prices and ideal client', 'Follows your method and rules', 'Writes the way you write']));

s = pptx.addSlide({ masterName: '11 Scope and deliverables' });
t(s, 'label', 'SCOPE'); t(s, 'headline', 'What is included'); t(s, 'caption', 'Replace every item in braces before sending.');
const hdr = (x) => ({ text: x, options: { fontFace: F.mono, fontSize: 10, color: K.grey, charSpacing: 1.2, bold: false, border: [{ type: 'none' }, { type: 'none' }, { pt: 1, color: K.ink }, { type: 'none' }] } });
const cell = (x, o = {}) => ({ text: x, options: Object.assign({ fontFace: F.reg, fontSize: 16, color: K.ink, border: [{ type: 'none' }, { type: 'none' }, { pt: 0.75, color: K.line }, { type: 'none' }] }, o) });
s.addTable([
  [hdr('DELIVERABLE'), hdr('WHAT YOU GET'), hdr('WHEN')],
  [cell('Expert DNA files', { fontFace: F.med }), cell('{Description}'), cell('{Week}')],
  [cell('Plugins connected', { fontFace: F.med }), cell('{Which plugins}'), cell('{Week}')],
  [cell('Setup Call', { fontFace: F.med }), cell('{Description}'), cell('{Week}')],
  [cell('Handover', { fontFace: F.med }), cell('{Description}'), cell('{Week}')],
], { x: M, y: Y.top, w: W - 2 * M, colW: [sp(4), sp(6) + 0.2, sp(2)], rowH: 0.62, valign: 'middle', margin: [0.04, 0.1, 0.04, 0] });

s = pptx.addSlide({ masterName: '12 Offer and price' });
t(s, 'label', 'OFFER'); t(s, 'headline', 'Choose how to start');
[['BOOK', 'Expert DNA: the book', 'The method, in one read.', '7 EUR'], ['PLUGINS', 'All 8 plugins', 'Each with a mini course.', '97 EUR'], ['SETUP', 'Setup Call', 'With a specialist.', '297 EUR']]
  .forEach(([a, b, c, d], i) => { t(s, `optLabel${i + 1}`, a); t(s, `optName${i + 1}`, b); t(s, `optBody${i + 1}`, c); t(s, `price${i + 1}`, d); });
t(s, 'caption', 'Prices are working numbers and placeholders.');

s = pptx.addSlide({ masterName: '13 Quote' });
t(s, 'label', 'IN THEIR WORDS'); t(s, 'quote', '{Client quote. Use real words only, with written permission.}');
t(s, 'name', '{Name Surname}'); t(s, 'role', '{ROLE, COMPANY}');

s = pptx.addSlide({ masterName: '14 Image and text' });
t(s, 'label', 'INSIDE A PLUGIN'); t(s, 'headline', 'The proposal you don\'t have to write');
t(s, 'body', 'Insert a real screenshot of the plugin output on the left. Never use stock photos.');
t(s, 'caption', 'Caption: {what the viewer sees in the screenshot}');

s = pptx.addSlide({ masterName: '15 Lesson opener' });
t(s, 'label', 'MODULE 01 / LESSON 02'); t(s, 'title', 'Write your offer file');
t(s, 'goalLabel', 'AFTER THIS LESSON YOU CAN'); t(s, 'goal', 'Write down your offers and prices so AI can quote them correctly.');

s = pptx.addSlide({ masterName: '16 Exercise' });
t(s, 'label', 'EXERCISE'); t(s, 'headline', 'Write your first Expert DNA file'); t(s, 'time', '{15} MIN');
t(s, 'body', numbered(['List every offer you sell today.', 'Add the price and who each offer is for.', 'Write one sentence on what the client gets.']));
['OFFER NAME', 'PRICE', 'WHO IT IS FOR'].forEach((x, i) => t(s, `field${i + 1}`, x));

s = pptx.addSlide({ masterName: '17 Key takeaways' });
t(s, 'label', 'KEY TAKEAWAYS'); t(s, 'headline', 'Three things to remember');
['AI without context works like a confused intern.', 'Write down what lives in your head once, as plain files.', 'Stay human. Automate the rest.'].forEach((x, i) => { t(s, `n${i + 1}`, `0${i + 1}`); t(s, `take${i + 1}`, x); });

s = pptx.addSlide({ masterName: '18 Closing and contact' });
t(s, 'label', 'NEXT STEP'); t(s, 'title', 'Let\'s write your Expert DNA.');
t(s, 'contact', 'DONATAS JONIKAS, PHD\nEXPERTDNA.NET\n{EMAIL}');

// ---------- write + clean dashes ----------
(async () => {
  const buf = await pptx.write({ outputType: 'nodebuffer' });
  const zip = await JSZip.loadAsync(buf);
  let fixed = 0;
  for (const n of Object.keys(zip.files)) {
    if (!n.endsWith('.xml') && !n.endsWith('.rels')) continue;
    let x = await zip.file(n).async('string');
    const y = x.replace(/[\u2013\u2014]/g, '-');
    if (y !== x) { fixed++; zip.file(n, y); }
  }
  fs.writeFileSync(OUT, await zip.generateAsync({ type: 'nodebuffer', compression: 'DEFLATE' }));
  console.log('written', OUT, 'xml files with dashes replaced:', fixed);
})();
