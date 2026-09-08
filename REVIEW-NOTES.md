# For Levier's review — things to replace before going live

**Three of these are false claims, not just placeholders.** The stats row under the brand belt
says 35 years of experience, 2,400+ elevators under service and 98% client retention. Levier is
starting this company, so all three are untrue today. They are on the page as placeholders at
Will's request. **They must be replaced or the whole row removed before Levier trades on it.**

The rest are placeholders that need his real data:

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
7. **Stats row**: 35 / 2,400+ / 98% / 24/7. See the warning above. Edit the `data-to` values in `index.html`, or delete the whole `<section class="stats">` block.
8. **Language default**: English loads first for review. To make Spanish the default later: in `script.js`, change `localStorage.getItem("levx-lang") || "en"` to `|| "es"`.

Logo concepts are in `logos/` (01 wordmark, 02 monogram, 03 pictorial, 04 badge). Pick one and I refine it.
