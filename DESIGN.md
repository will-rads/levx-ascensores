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
Scroll-scrubbed video intro · brand logo marquee · expanding service panels ·
drifting testimonial columns · big-statement "why" with 2 columns + process line ·
full-bleed blue emergency band · full-bleed image break · split contact (channels + form) · footer.
No eyebrows, no numbered labels, no dashes anywhere.

## Hero intro
The hero is a 260vh track (220vh under 900px) with a `position: sticky` 100vh stage pinned inside it.
Scroll position maps to `heroVideo.currentTime`, so the intro plays as you scroll rather than on its
own. A rAF loop does the seeking and it only runs while an IntersectionObserver says the hero is on
screen, so there is still no scroll listener anywhere.

While the video runs the only copy on screen is the cue: "Going up" / "Subiendo" / "نصعد" in
Gambarino, with a small uppercase scroll label and an orange arrow. It fades out between 56% and 82%
of the track. The real `h1`, lede and buttons fade up between 84% and 100%, and carry `inert` until
they are more than half visible so they stay out of the tab order.

A scrim over the video keeps the copy readable on every frame, bright marble or dark shaft: a
left-to-right black gradient (flipped for RTL) plus a short one from the top. Because the hero is
dark, the copy is white and the primary button inverts to white with black text. The header goes
transparent with white contents while it sits over the hero (`.site-header.over-hero`).

Under `prefers-reduced-motion` the whole thing is skipped: `.hero.no-scrub` drops the track to normal
height, hides the cue, shows the copy, and the closing frame stands in as a still background.

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
The hero is video: `img/hero.mp4` (10s, 1600x900, silent, every frame a keyframe so scrubbing is
smooth), with `img/hero-poster.jpg` as its first frame and `img/hero-still.jpg` (the closing shot) as
the reduced-motion background. Generated on Higgsfield with Kling 3.0 in `pro` mode from a generated
wide-lobby start frame.

Real black and white photography supplied by Levier: `img/doors-wide.jpg`
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
Scroll-scrubbed hero video (rAF loop gated by an IntersectionObserver), scroll reveals
(IntersectionObserver), accordion via `grid-template-rows 0fr/1fr`, CSS marquee. All gated behind
prefers-reduced-motion. No scroll listeners.
