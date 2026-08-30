# LEVX Ascensores design system (v2, lightweight)

One-page trilingual site (EN default / ES / AR-RTL). Plain HTML/CSS/JS, no build step.
Design skill: gpt-taste-2. Read: local-service landing, clean premium light, one cobalt accent.

## Color
`--bg #f7f8fa` ground · `--surface #fff` · `--ink #14171c` · `--ink-2 #59626f` ·
`--accent #2337d6` (the only accent, used for every CTA and the emergency band) · `--line #e4e7ed`.

## Type
Satoshi (Fontshare) 900 display / 700 UI / 400 body. Cairo for Arabic via `[lang=ar]`.
Display tracking -0.02em (reset to 0 for Arabic).

## Shape rule
Interactive = pill (999px). Media and cards = 18px (`--r-media`). Inputs = 12px.

## Sections
Split hero with generated photo · brand logo marquee · expanding service panels ·
drifting testimonial columns · big-statement "why" with 2 columns + process line ·
full-bleed blue emergency band · full-bleed image break · split contact (channels + form) · footer.
No eyebrows, no numbered labels, no dashes anywhere.

## Service panels
Six flex panels, `flex: 1` collapsed and `flex: 4` open, 600ms width transition (pattern taken from
the Namou partner portal area accordion). Collapsed media is grayscale; the open one goes to color.
Hover or click opens a panel; leaving the row restarts a 4.5s auto-advance. Stacks to
height-animated rows under 900px. No auto-advance under prefers-reduced-motion.

## Testimonials
Three columns of cards scrolling vertically at 46s / 58s / 52s, middle one reversed, edges masked.
Cards are rendered in JS from `VOICES` in script.js so they follow the language switch.
Columns drop to two, then one, on narrow screens.

## Images
`img/hero.jpg`, `img/technician.jpg`, `img/doors-wide.jpg`, `img/services/*.jpg`, `img/people/*.jpg`:
Gemini-generated (nano banana pro), cool-toned editorial placeholders. Swap for real photos at the
same paths. `img/brands/*.png`: real manufacturer logos from Wikimedia Commons, converted to
grayscale with the white knocked out, shown at 32% opacity.

## i18n
Same mechanism as v1: `I18N` dict in script.js, `data-i18n` / `data-i18n-ph`, localStorage `levx-lang`,
`dir=rtl` for AR, phone numbers wrapped `dir="ltr"`. Default flips to Spanish by changing `|| "en"` to `|| "es"`.

## Motion
Hero load rise (CSS keyframes), scroll reveals (IntersectionObserver), accordion via
`grid-template-rows 0fr/1fr`, CSS marquee. All gated behind prefers-reduced-motion. No scroll listeners.
