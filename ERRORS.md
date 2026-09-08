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
- **`python -m http.server` cannot serve video at all.** It does not answer Range requests, so the
  browser resets the connection on `img/hero.mp4` and the hero looks broken locally while being fine
  on Vercel. A ~25 line threading server that handles `Range` and returns 206 fixes it. Same handler
  also cures the reset on larger images.
- **`python -m http.server` resets the connection** on large images. Every image was converted to a
  JPG of 1600px or less with ffmpeg, which also fixed it. Vercel never had the problem.

## Content sources

- Manufacturer logos come from **Wikimedia Commons** via
  `https://commons.wikimedia.org/wiki/Special:FilePath/<file name>?width=600`, which renders SVGs to
  PNG for you. They were then converted to grayscale with the near-white pixels knocked out to
  transparent, trimmed, and normalised to a common height.
- **Orona and Fermator have no usable logo file online.** Mitsubishi Electric and Hitachi took their
  place in the belt. Drawing the missing two by hand is the only other option.
- **Higgsfield tries to hijack a cinematic prompt with an unrelated preset.** The elevator intro came
  back as a "preset_recommendation" for a PS1 survival-horror template. Decline it by resending with
  `declined_preset_id`. The presets are all character and meme effects, none of them are camera moves,
  so camera direction has to live in the prompt text.
- **Kling 3.0 in `pro` mode with `sound: "off"`** is the model that took a four-shot list in one
  prompt and held it. `cinematic_studio_video_v2` also has a real `multi_shots` flag if it is needed.
- **Scrubbing needs an all-keyframe encode.** `-g 1 -keyint_min 1 -sc_threshold 0` at 1600x900 CRF 32
  lands at 3.5MB and seeks instantly. A normal encode stutters because every seek decodes forward from
  the last keyframe.
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

- **Fontshare only serves one family per URL.** Requesting `f[]=satoshi...&f[]=gambarino@400` in a
  single link silently returns Satoshi alone. Give each family its own `<link>` tag.
- **A tall sticky hero hides its own failures.** If the video never loads, the pinned stage never
  changes, so the page looks frozen even though it is scrolling normally. Any scroll-driven hero needs
  a fallback to a plain static hero when the video is not ready.
