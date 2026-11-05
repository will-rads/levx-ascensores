"""Builds the photo signature artwork: round portrait + three contact icons.
Email apps strip SVG, so everything is PNG at 2x.
Usage: python build-photo.py <portrait.png>"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageOps

OUT = Path(__file__).parent / "assets"
BG = (255, 255, 255)
INK = (11, 11, 11)
S = 4  # supersample, then shrink for smooth edges


def portrait(src, color=False, name="levier-photo.png", d=84, tab=None, ring=3):
    """Round portrait with the black tab baked in, so no email app can pull them apart.
    Saved at 2x: display size is d wide, d + tab overlap tall."""
    k = 2 * S
    im = Image.open(src).convert("RGB")
    if not color:
        im = ImageOps.grayscale(im).convert("RGB")
    w, h = im.size
    side = min(w, h)
    im = im.crop(((w - side) // 2, 0, (w + side) // 2, side))
    top = tab[1] // 2 if tab else 0        # circle starts halfway down the tab, if there is one
    W, H = d * k, (d + top) * k
    canvas = Image.new("RGB", (W, H), BG)
    dr = ImageDraw.Draw(canvas)
    if tab:
        tx = (W - tab[0] * k) // 2
        dr.rectangle((tx, 0, tx + tab[0] * k, tab[1] * k), fill=INK)
    dr.ellipse((0, top * k, W - 1, H - 1), fill=(255, 255, 255))
    inner = W - 2 * ring * k
    im = im.resize((inner, inner), Image.LANCZOS)
    mask = Image.new("L", im.size, 0)
    ImageDraw.Draw(mask).ellipse((0, 0, inner - 1, inner - 1), fill=255)
    # thin grey ring so the white border still reads on a white email
    dr.ellipse((0, top * k, W - 1, H - 1), outline=(220, 220, 218), width=k)
    canvas.paste(im, (ring * k, top * k + ring * k), mask)
    canvas.resize((W // S, H // S), Image.LANCZOS).save(OUT / name, optimize=True)


def icon(name, draw_fn, px=28):
    big = px * S
    im = Image.new("RGB", (big, big), BG)
    d = ImageDraw.Draw(im)
    d.ellipse((0, 0, big - 1, big - 1), fill=INK)  # dark disc, like the reference
    draw_fn(d, big)
    im.resize((px, px), Image.LANCZOS).save(OUT / f"icon-{name}.png", optimize=True)


W = (255, 255, 255)


def phone(d, b):
    lw = int(b * 0.06)
    d.rounded_rectangle((b * .36, b * .24, b * .64, b * .76), radius=b * .05, outline=W, width=lw)
    d.line((b * .46, b * .67, b * .54, b * .67), fill=W, width=lw)


def mail(d, b):
    lw = int(b * 0.06)
    box = (b * .26, b * .33, b * .74, b * .67)
    d.rectangle(box, outline=W, width=lw)
    d.line((b * .27, b * .35, b * .50, b * .53, b * .73, b * .35), fill=W, width=lw, joint="curve")


def web(d, b):
    lw = int(b * 0.055)
    d.ellipse((b * .26, b * .26, b * .74, b * .74), outline=W, width=lw)
    d.ellipse((b * .40, b * .26, b * .60, b * .74), outline=W, width=lw)
    d.line((b * .27, b * .50, b * .73, b * .50), fill=W, width=lw)


def linkedin(d, b):
    from PIL import ImageFont
    f = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", int(b * 0.42))
    d.text((b * .5, b * .53), "in", font=f, fill=W, anchor="mm")


if __name__ == "__main__":
    portrait(sys.argv[1])
    portrait(sys.argv[1], color=True, name="levier-photo-color.png")
    icon("phone", phone)
    icon("mail", mail)
    icon("web", web)
    icon("linkedin", linkedin)
    print("built", sorted(p.name for p in OUT.glob("*.png")))
