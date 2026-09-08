# Where this stands

Built 30 August 2026. Live, deployed, and waiting on Levier's real details.

## Decisions already made, do not reopen

- **Black and white interface, photos in color.** Every button and the emergency band are black.
  Dark orange `#d1500f` appears only in small hits: logo arrow, the rule above an open service
  panel, the top edge of the black band, the process line, contact icons, stars, card outlines.
  An earlier attempt made the buttons orange and the photos grayscale. That was wrong, both times.
- **No eyebrow labels, ever.** No small caps kicker text above a heading. Will calls it the most AI
  looking thing a page can do.
- **No numbered boxes, no full stops at the end of headings, and keep the copy short.**
- **No PRODUCT.md.** `DESIGN.md` stays lightweight.
- **Headings are Gambarino** (Fontshare, one weight only). Satoshi carries the body and UI, Cairo
  carries Arabic. Fontshare serves one family per URL, so each needs its own `<link>`.
- **The hero photography is Levier's own, and it is black and white.** He supplied it, so the site no
  longer desaturates anything itself; the service panels reveal on brightness instead of color.

## What is on the page

A scroll-scrubbed video hero, brand logo belt, six expanding service panels that auto advance,
testimonials, a "why us" statement, a black emergency band, a wide image, contact with a mailto form,
footer.

The hero intro was generated on Higgsfield (Kling 3.0 pro, silent, black and white): the camera pushes
across a marble lobby, through the doors, up the shaft, then the doors open. It is driven by scroll,
not autoplay. While it runs the only copy is "Going up" and a scroll arrow; the real headline and
buttons appear when the scroll ends. `DESIGN.md` has the mechanics.

`esignature/index.html` is a standalone copy-and-paste email signature for Levier, in the blues of his
original logo (`levx-logo-og.png`), no social links.

Testimonials are three drifting columns on desktop and a staggered card deck on phones, both built
from the same `VOICES` array. All nine reviews, the names, the faces and the star ratings are
invented, and they will need replacing or removing before Levier trades on them.

## Next

1. Levier reviews it in Arabic, then replace the placeholders listed in `REVIEW-NOTES.md`
   (phone, email, cities, photos, the claims about 24/7 and free audits).
2. He picks a logo from `logos/`, then it gets refined and dropped in.
3. Flip the default language to Spanish once he approves (`|| "en"` to `|| "es"` in `script.js`).
4. Decide what to do about the invented testimonials.
5. Confirm Levier's full name and job title, both are guessed in the email signature.
6. Swap the signature and site links to the real `.es` domain once it exists; they point at the
   Vercel URL for now, while the email on it is already `info@levxascensores.es`.
7. Levier reported the page not scrolling on his MacBook Air in both Safari and Chrome. Unconfirmed
   whether that is the scrubbed hero or his trackpad. The planned fix is a fallback to a plain hero
   when the video is not ready, plus seeking the video less often than every frame.
