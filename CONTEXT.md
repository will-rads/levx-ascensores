# Context

Marketing site for **LEVX Ascensores**, the elevator maintenance and repair company Will's friend
Levier is starting in Spain. Levier reads Arabic, Will reads English, the customers read Spanish.

## Stack

Plain HTML, CSS and JS. **No build step, no framework, no dependencies.** Four files do everything:

| File | Holds |
| --- | --- |
| `index.html` | All markup, one page |
| `styles.css` | All styles, design tokens at the top |
| `script.js` | Translations, service panels, testimonials, contact form |
| `DESIGN.md` | The design system, read this before changing anything visual |

Images live in `img/` (`services/`, `people/`, `brands/`). Logo concepts are in `logos/`, which is
gitignored along with `screenshots/`.

## Languages

English loads first, Spanish and Arabic are in the switcher. Text lives in the `I18N` object in
`script.js`, keyed by the `data-i18n` attributes in the markup. Arabic flips the page to RTL and
swaps to the Cairo font. Phone numbers are wrapped in `dir="ltr"` so they do not reverse.

To make Spanish the default later, change `|| "en"` to `|| "es"` at the bottom of `script.js`.

## Running it

```bash
python -m http.server 8642 --directory family-friends/levier-elevator
```

There is also a `levx` entry in `Me/.claude/launch.json` for the Browser pane.

## Deploying

Repo [will-rads/levx-ascensores](https://github.com/will-rads/levx-ascensores), live at
<https://levx-ascensores.vercel.app>. Vercel is connected to GitHub, so **a push to `main` deploys
itself**. A deploy takes well under a minute.

## Still placeholder

Phone, email, cities and all photography are invented. The full list of what Levier has to replace
is in `REVIEW-NOTES.md` (parts of that file describe an older version of the layout, trust this file
and `DESIGN.md` where they disagree).
