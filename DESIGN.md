# LEVX Ascensores design system (v2, lightweight)

One-page trilingual site (EN default / ES / AR-RTL). Plain HTML/CSS/JS, no build step.
Design skill: gpt-taste-2. Read: local-service landing, black and white interface, orange sparks.

## Color
`--bg #f4f4f3` ground · `--surface #fff` · `--ink #0b0b0b` · `--ink-2 #5d5d5d` · `--line #e3e3e1`.
`--accent #0b0b0b`: the interface is black on white, so every button, the active language chip and
the emergency band are black. `--spark #d1500f` is a dark orange used only in small hits against
black or white: the arrow inside the logo mark, the rule above an open panel name, the top edge of
the emergency band, the process line, the contact icons, selection and focus rings. Photographs
keep their own colors; only the collapsed service panels are desaturated, and they return to color
when they open.

## Type
Gambarino (Fontshare, single 400 weight) for every `h1` and `h2`. Satoshi 700 UI / 400 body, and
Satoshi 900 for the LEVX wordmark and the small labels on the service panels. Arabic ignores
Gambarino and sets headings in Cairo 900 via `[lang=ar]`, tracking reset to 0.
Fontshare drops the second family when two are requested in one URL, so Satoshi and Gambarino each
need their own `<link>`.

## Shape rule
Interactive = pill (999px). Media and cards = 18px (`--r-media`). Inputs = 12px, inside a contact
card at 24px so the nested corners stay concentric.

## Touch and edges
Anything clickable shrinks to `scale(0.96)` while pressed (service panels use `0.98`, they are far
bigger). Photographs carry a `1px` hairline outline at 10% black, or 10% white on the black deck
card, so they do not bleed into the page. The focus ring never changes an element's own radius.

## Sections
Split hero with generated photo · brand logo marquee · expanding service panels ·
drifting testimonial columns · big-statement "why" with 2 columns + process line ·
full-bleed blue emergency band · full-bleed image break · split contact (channels + form) · footer.
No eyebrows, no numbered labels, no dashes anywhere.

## Service panels
Six flex panels, `flex: 1` collapsed and `flex: 4` open, 600ms width transition (pattern taken from
the Namou partner portal area accordion). Collapsed media sits darker; the open one brightens.
Hover or click opens a panel; leaving the row restarts a 4.5s auto-advance. Stacks to
height-animated rows under 900px. No auto-advance under prefers-reduced-motion.

## Testimonials
Desktop: three columns of cards scrolling vertically at 46s / 58s / 52s, middle one reversed, edges
masked. Under 900px the columns are replaced by a staggered deck (adapted from the 21st.dev
stagger-testimonials component): the front card is black with an orange keyline, neighbours sit
behind it tilted and faded, and arrows or a tap on a side card steps through. Both are rendered in
JS from `VOICES` in script.js so they follow the language switch. Each card carries a four or five
star rating in orange, and portraits keep their color.

## Copy rule
No full stop at the end of any heading, in any language.

## Images
Real black and white photography supplied by Levier: `img/hero.jpg` (steel cabin), `img/doors-wide.jpg`
(closed doors in a marble lobby), and three service panels (maintenance, modernization, installation).
The three remaining service photos are still generated placeholders, desaturated so the panel row reads
as one set. Reviewer portraits in `img/people/` stay in color. `img/brands/*.png`: real manufacturer
logos from Wikimedia Commons, grayscale with the white knocked out, shown at 55% opacity.
Because the photography is already monochrome, service panels reveal on brightness and contrast
rather than on color.

## i18n
Same mechanism as v1: `I18N` dict in script.js, `data-i18n` / `data-i18n-ph`, localStorage `levx-lang`,
`dir=rtl` for AR, phone numbers wrapped `dir="ltr"`. Default flips to Spanish by changing `|| "en"` to `|| "es"`.

## Motion
Hero load rise (CSS keyframes), scroll reveals (IntersectionObserver), accordion via
`grid-template-rows 0fr/1fr`, CSS marquee. All gated behind prefers-reduced-motion. No scroll listeners.
