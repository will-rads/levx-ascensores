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
- Fonts are Satoshi (Fontshare) and Cairo for Arabic. Design skill in use is gpt-taste-2.

## What is on the page

Hero, brand logo belt, six expanding service panels that auto advance, testimonials, a "why us"
statement, a black emergency band, a wide image, contact with a mailto form, footer.

Testimonials are three drifting columns on desktop and a staggered card deck on phones, both built
from the same `VOICES` array. All nine reviews, the names, the faces and the star ratings are
invented, and they will need replacing or removing before Levier trades on them.

## Next

1. Levier reviews it in Arabic, then replace the placeholders listed in `REVIEW-NOTES.md`
   (phone, email, cities, photos, the claims about 24/7 and free audits).
2. He picks a logo from `logos/`, then it gets refined and dropped in.
3. Flip the default language to Spanish once he approves (`|| "en"` to `|| "es"` in `script.js`).
4. Decide what to do about the invented testimonials.
