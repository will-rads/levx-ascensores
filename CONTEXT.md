# LEVX Ascensores

Marketing site for Levier's elevator maintenance/repair company in Spain. Will reviews in English, Levier in Arabic, customers in Spanish.

## Files

- `index.html`, `styles.css`, `script.js`: one-page site, plain HTML/CSS/JS, no build or runtime dependencies.
- `motion.js`: early site motion preference, shared by CSS and interactions.
- `img/`: video, service images, portraits and manufacturer logos.
- `esignature/photo.html`: **current** email signature, round portrait (black and white and colour versions), real contacts. `esignature/index.html` is the older GIF version.
- `serve.py`: local server with Range support, so the hero video plays locally. Run `python serve.py` (port 8643); also the `levx` entry in `Me/.claude/launch.json`.
- `logos/`: ignored logo concepts; `levx-logo-og.png`: original logo.
- `AGENTS.md`: working and automatic-push instructions.
- `DESIGN.md`: visual rules. `MEMORY.md`: current status. `REVIEW-NOTES.md`: content awaiting confirmation. `ERRORS.md`: operational pitfalls.

## Languages

`I18N` in `script.js` maps `data-i18n` / `data-i18n-ph` attributes. English defaults until approval to switch to Spanish. Saved choice: `levx-lang`. Arabic uses RTL/Cairo; phone numbers remain LTR. Change the final language fallback to `es` when approved.

## Checks and deployment

Run from this folder:

```powershell
node --check script.js
node --test hero.test.cjs reviews.test.cjs nav.test.cjs motion.test.cjs
git diff --check
```

Use `python serve.py` for local testing. Python's basic HTTP server cannot serve the video.

[Repository](https://github.com/will-rads/levx-ascensores) | [Live site](https://www.levxascensores.es/) | [Vercel fallback](https://levx-ascensores.vercel.app/)

Vercel project: `will-namou/levx-ascensores`. `levxascensores.es` redirects to `www.levxascensores.es` (308). Hostinger manages DNS using `ns1.dns-parking.com` / `ns2.dns-parking.com`; email records remain unchanged.

| Type | Name | Value | TTL |
|---|---|---|---|
| A | `@` | `216.198.79.1` | 300 |
| CNAME | `www` | `b669c54bc299f8be.vercel-dns-017.com` | 300 |

Push to `main` to deploy automatically. Use the `will-rads` account; see `ERRORS.md` if Git selects NamouProperties.
