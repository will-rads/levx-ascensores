# LEVX design

Plain one-page service site. Design direction: gpt-taste-2. Preserve this look unless asked otherwise.

## Visual rules

- Ground `#f4f4f3`, surface white, ink `#0b0b0b`, secondary ink `#5d5d5d`, lines `#e3e3e1`.
- Buttons and emergency band are black; orange `#d1500f` is for small accents, stars, rules and focus rings. Hero primary button is white.
- Square corners throughout, including navigation, its sliding highlight and portraits. Thin image outlines. Preserve photos' native colors; service panels change brightness/contrast.
- Gambarino 400: headings, navigation, buttons, stats and header wordmark. Satoshi: body, form/language labels, small panel labels and footer wordmark. Cairo handles Arabic text; the Latin header name stays Gambarino.
- Full header name on phones, stacked on two lines. Keep language controls and call button beside it; compact spacing below 360px.
- No eyebrow headings, numbered boxes or final full stops on headings. Keep copy short.

## Page order

Video hero, manufacturer belt, stats, six services, buildings split, reviews, why/process, emergency band, dark photo CTA, contact/mailto form, footer.

## Hero

Reuse `img/hero.mp4` on every device: silent 10-second, 1600x900, 24fps all-keyframe H.264 (~3.5 MB). Generated with Kling 3.0 pro from a generated lobby frame. `hero-poster.jpg` is the initial frame; `hero-still.jpg` is the closing fallback.

Desktop: 340vh track / sticky 100vh stage. At <=900px: 280svh / 100svh with vh fallbacks. Scroll maps to video time; rAF runs only while visible. Wait for each seek, cap requests at 24/second, and skip unchanged targets. Muted inline playback briefly primes loading, then pauses; first gestures retry if needed.

Cue fades at 56-82%; headline/buttons appear at 84-100%, remaining inert until half visible. Dark gradient scrims and a transparent white-text header preserve contrast. Reduced motion, media errors or 15 seconds without initial decoded data select the static hero and visible, usable copy.

## Reviews

Shared `VOICES` content follows EN/ES/AR switching.

- Desktop: three vertical columns, 46/58/52-second loops, middle reversed, masked edges. Preserve this animation.
- <=900px: two horizontal opposing loops, 38/44 seconds, following the Green Room FX mobile reference. Square black cards, 258px wide, minimum 230px tall, 10px card gaps and 14px row gap. Portrait/name first, quote below, orange stars at bottom.
- Mobile rows pause on hover, touch or focus. Reduced motion removes loops/duplicates and allows horizontal scrolling. Arabic card text remains RTL.

## Other motion

Services expand from flex 1 to 4 over 600ms and advance every 7 seconds; below 900px they become height-animated rows. Stats count once over 1.6 seconds; 24/7 stays static. Respect reduced motion. Use IntersectionObserver, CSS and rAF, not scroll listeners or animation dependencies.

## Image sources

Levier supplied `doors-wide.jpg` and the maintenance, modernization and installation photos. Repairs, accessibility and retrofit use stock images; building and CTA images are in `img/`. Reviewer portraits are generated and not real customers. Manufacturer PNGs originated from Wikimedia Commons and are grayscale/transparent at low opacity. The email signature keeps the original blue logo branding.

Desktop navigation follows Cedars: centered dark translucent square menu, 250ms sliding orange highlight on hover/focus, active section tracking, reduced-motion support. Mobile navigation remains hidden.

## Motion preference

`motion.js` runs before CSS and sets `data-motion` from the system preference or a saved site override. A square bottom-corner EN/ES/AR button appears for reduced-motion visitors and anyone with a saved choice. It enables or reduces all site animations, remembers `levx-motion` locally and reloads to apply. History state preserves the current visit if storage is blocked. Computer settings are unchanged; Safari media permission is separate.
