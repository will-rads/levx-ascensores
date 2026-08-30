# For Levier's review — things to replace before going live

Nothing on the site is a false claim, but these placeholders need his real data:

1. **Phone / WhatsApp**: `+34 600 000 000` (appears in header, hero, emergency card, contact). Search-replace in `index.html`.
2. **Email**: `info@levx-ascensores.es` (contact section + form mailto in `script.js`).
3. **Photos**: 6 service panels, hero is fine without one. Blueprint-hatch boxes labeled `PHOTO · ...` show where each goes.
4. **Coverage map + cities**: city chips (Madrid, Barcelona, ...) are examples. Confirm where he actually works.
5. **Claims to confirm with him**:
   - "Certified technicians" — confirm certification.
   - "24/7 emergency line" — confirm he will actually answer 24/7.
   - "Free audit" and "binding quote" — confirm the offer.
   - Brand names in the marquee (Otis, Schindler, KONE, TK, Orona, Hyundai, Mitsubishi, Fermator) — brands he can actually service.
6. **Company name**: site says LEVX Ascensores everywhere. If he prefers another name, search-replace.
7. **Language default**: English loads first for review. To make Spanish the default later: in `script.js`, change `localStorage.getItem("levx-lang") || "en"` to `|| "es"`.

Logo concepts are in `logos/` (01 wordmark, 02 monogram, 03 pictorial, 04 badge). Pick one and I refine it.
