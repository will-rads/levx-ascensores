# Current state

Updated 6 November 2026. Folder moved from `family-friends/` to `projects/levier-elevator/`.

- Custom domain live: both domains showed Valid Configuration in Vercel; user confirmed the site loads. Root redirects to `www.levxascensores.es`. DNS details are in `CONTEXT.md`.

- Mobile reviews: two opposing horizontal rows. Desktop retains three vertical animated columns.
- Header: Gambarino, full LEVX Ascensores name on phones. Desktop has a centered square translucent menu with a sliding orange highlight.
- Hero: existing MP4 on desktop and phones; serialized seeks, muted loading priming, stable mobile height and static fallback. Local browser checks passed.
- M1 MacBook Air: user reports animations worked after disabling macOS Reduce Motion. Browser/version coverage and the site override on that Mac remain unverified.
- Reduced-motion visitors see Enable animations at bottom right (bottom left in Arabic). It saves a LEVX-only override; the button is hidden when motion is already enabled and no choice is saved.
- Automatic commit/push after necessary changes is authorized in `AGENTS.md`.
- Real contact details are live on the site: +34 617 50 96 16, WhatsApp `wa.me/34617509616`, levier@levxascensores.es, office C. Alcalá, 201, 6C, Salamanca, 28028 Madrid (contact list and footer).
- Current signature: `esignature/photo.html`, live at `www.levxascensores.es/esignature/photo.html`. White background, content-width, round portrait (B&W and colour versions), LEVIER ORAHA in caps, Founder, phone, email, site and LinkedIn in a 2x2 grid under the photo. Will tested it in Gmail. Icons sit inline with text because Gmail splits separate cells on paste. Image URLs carry `?v=N`; bump it when artwork changes so Gmail drops its cached copy. Rebuild artwork with `python esignature/build-photo.py esignature/source/levier-portrait.png`.
- Older GIF signature (`esignature/index.html`) and v1 stay in the folder but are no longer the one in use.

## Next

Levier reviews the site in Arabic, confirms the content in `REVIEW-NOTES.md`, chooses a logo and confirms his title ("Founder" is a guess). Switch the default to Spanish after approval. Update remaining hardcoded site/signature URLs to the live domain; DNS setup did not change source files.

## Keep

Preserve square shapes, black/white UI, small orange accents and short copy without heading punctuation or eyebrow labels. Keep `DESIGN.md` lightweight; no separate PRODUCT.md.
