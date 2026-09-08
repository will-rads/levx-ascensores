# Email signature

- `index.html`: current black/white signature with orange accents and elevator GIF.
- `index-v1.html`: preserved original blue version.
- `assets/original-logo.png`: exact original embedded logo; intentionally unchanged.
- `assets/elevator-arrival.gif`: 6-second loop, 520×100 display size, about 22 KB. First frame is a complete still.
- `assets/levier-name.png`: Gambarino artwork, preserving the name font in email clients.

Copy from the live `/esignature/` page. Image URLs are absolute HTTPS URLs; contact links remain editable text. Gambarino is used where available, with Georgia fallback for live text. Email client settings may stop GIF animation; test a received email in the intended clients. No account signature settings were changed automatically.

Name, title and contact details are retained from v1 and still need Levier's confirmation. The website address remains the existing Vercel URL.

Rebuild artwork with Pillow and a local Gambarino font from Fontshare:
`python build-assets.py /path/to/Gambarino.ttf`
