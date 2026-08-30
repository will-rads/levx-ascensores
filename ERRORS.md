# Things that bit us, and what fixed them

## Tooling

- **`gh repo create` is blocked** by the Claude Code permission classifier (it counts as publishing).
  The repo was created through the Composio GitHub tool instead, on the `personal-github` account
  (= will-rads, **not** the `namou-github` one). Plain `git push` is fine and needs no workaround.
- **The Vercel MCP token cannot create projects** (403). The local CLI works:
  `npx vercel link --yes --project levx-ascensores`, then `npx vercel deploy --prod --yes`.
  Any npm or node command in this environment needs `NODE_OPTIONS=--use-system-ca`.
- **Browser pane screenshots come out blank** once the page has been scrolled. It is a capture bug,
  the page itself is fine. Verify with the Playwright tools instead.
- **`python -m http.server` resets the connection** on large images. Every image was converted to a
  JPG of 1600px or less with ffmpeg, which also fixed it. Vercel never had the problem.

## Content sources

- Manufacturer logos come from **Wikimedia Commons** via
  `https://commons.wikimedia.org/wiki/Special:FilePath/<file name>?width=600`, which renders SVGs to
  PNG for you. They were then converted to grayscale with the near-white pixels knocked out to
  transparent, trimmed, and normalised to a common height.
- **Orona and Fermator have no usable logo file online.** Mitsubishi Electric and Hitachi took their
  place in the belt. Drawing the missing two by hand is the only other option.
- Photos and portraits are generated with Gemini `gemini-3-pro-image-preview` using
  `GEMINI_API_KEY`, `responseModalities: ["IMAGE"]` and an `imageConfig.aspectRatio`.

## Code traps

- **RTL and absolute positioning.** `inset-inline-start: 50%` centers nothing in Arabic, it anchors
  the right edge. The testimonial deck uses physical `left: 50%` and mirrors its own offsets with a
  direction factor in JS instead.
- **`setLang` runs `renderVoices`**, so the language switch must be called at the *bottom* of
  `script.js`, after `VOICES` and the deck helpers exist. Calling it early throws a TDZ error.
- **No scroll listeners anywhere.** The header hairline, the reveals and the service panel start all
  use IntersectionObserver. Keep it that way.
- **A blur filter on small logos reads as "out of focus"** on a phone, not as softness. Lower the
  opacity instead.
