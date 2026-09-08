# LEVX Ascensores

Marketing site for Levier's elevator maintenance/repair company in Spain. Will reviews in English, Levier in Arabic, customers in Spanish.

## Files

- `index.html`, `styles.css`, `script.js`: one-page site, plain HTML/CSS/JS, no build or runtime dependencies.
- `img/`: video, service images, portraits and manufacturer logos.
- `esignature/index.html`: separate email signature using the original blue branding.
- `logos/`: ignored logo concepts; `levx-logo-og.png`: original logo.
- `AGENTS.md`: working and automatic-push instructions.
- `DESIGN.md`: visual rules. `MEMORY.md`: current status. `REVIEW-NOTES.md`: content awaiting confirmation. `ERRORS.md`: operational pitfalls.

## Languages

`I18N` in `script.js` maps `data-i18n` / `data-i18n-ph` attributes. English defaults until approval to switch to Spanish. Saved choice: `levx-lang`. Arabic uses RTL/Cairo; phone numbers remain LTR. Change the final language fallback to `es` when approved.

## Checks and deployment

Run from this folder:

```powershell
node --check script.js
node --test hero.test.cjs reviews.test.cjs
git diff --check
```

Use a local server with HTTP Range/206 support for video testing. Python's basic HTTP server is suitable for layout checks, not reliable seek validation.

[Repository](https://github.com/will-rads/levx-ascensores) | [Live site](https://levx-ascensores.vercel.app/)

Push to `main` to deploy automatically. Use the `will-rads` account; see `ERRORS.md` if Git selects NamouProperties.
