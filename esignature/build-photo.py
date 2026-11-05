"""Builds the photo signature artwork: round portrait + three contact icons.
Email apps strip SVG, so everything is PNG at 2x.
Usage: python build-photo.py <portrait.png>"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageOps

OUT = Path(__file__).parent / "assets"
BG = (242, 242, 241)
INK = (11, 11, 11)
S = 4  # supersample, then shrink for smooth edges


def portrait(src, px=272, ring=8, color=False, name="levier-photo.png"):
    im = Image.open(src).convert("RGB")
    if not color:
        im = ImageOps.grayscale(im).convert("RGB")
    w, h = im.size
    side = min(w, h)
    im = im.crop(((w - side) // 2, 0, (w + side) // 2, side))  # keep the top, it holds the face
    big = px * S
    im = im.resize((big - 2 * ring * S,) * 2, Image.LANCZOS)
    canvas = Image.new("RGB", (big, big), BG)
    d = ImageDraw.Draw(canvas)
    d.ellipse((0, 0, big - 1, big - 1), fill=(255, 255, 255))  # white ring
    mask = Image.new("L", im.size, 0)
    ImageDraw.Draw(mask).ellipse((0, 0, im.size[0] - 1, im.size[1] - 1), fill=255)
    canvas.paste(im, (ring * S, ring * S), mask)
    canvas.resize((px, px), Image.LANCZOS).save(OUT / name, optimize=True)


def icon(name, draw_fn, px=36):
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
