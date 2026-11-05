# Email signature

**In use: `photo.html`** (live at `https://www.levxascensores.es/esignature/photo.html`). Two versions on one page, black and white and colour portrait, each with its own Copy button. Levier copies on a computer and pastes into Gmail web; the Gmail phone app only takes plain text.

- `photo.html`: white, content-width, round portrait, LEVIER ORAHA, Founder, phone, email, site, LinkedIn. Icons sit inline with the text (Gmail splits separate icon cells when pasted). No SVG, no web fonts, no negative margins.
- `build-photo.py`: rebuilds `assets/levier-photo.png`, `assets/levier-photo-color.png` and the `icon-*.png` files. Run `python build-photo.py source/levier-portrait.png`.
- `source/levier-portrait.png`: the original portrait Levier supplied.
- Image URLs end in `?v=N`. Bump N after rebuilding artwork, or Gmail keeps showing its cached copy.

Older, not in use:

- `index.html`: black and white signature with the elevator GIF and Gambarino name artwork (`build-assets.py`).
- `index-v1.html`: original blue version.
- `assets/original-logo.png`, `assets/elevator-arrival.gif`, `assets/levier-name.png`: artwork for those two.
