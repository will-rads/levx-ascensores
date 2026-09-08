"""Rebuild signature artwork: python build-assets.py /path/to/Gambarino.ttf"""
from pathlib import Path
import base64, re, sys
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "assets"
FONT = sys.argv[1]
S = 2
INK = "#0b0b0b"
ORANGE = "#d1500f"

def font(size):
    return ImageFont.truetype(FONT, round(size*S))

def text(draw, xy, value, size, fill=INK, anchor="lt"):
    draw.text(tuple(round(x*S) for x in xy), value, font=font(size), fill=fill, anchor=anchor)

def rect(draw, box, fill, outline=None, width=1):
    draw.rectangle(tuple(round(v*S) for v in box), fill=fill, outline=outline, width=round(width*S))

def line(draw, points, fill, width=1):
    draw.line([(round(x*S),round(y*S)) for x,y in points], fill=fill, width=round(width*S))

def ease(t):
    t=max(0,min(1,t))
    return t*t*(3-2*t)

# Preserve the exact logo image bytes from the original signature.
old=(ROOT / "index-v1.html").read_text(encoding="utf-8")
logo=re.search(r'data:image/png;base64,([^"\s]+)',old).group(1)
(OUT / "original-logo.png").write_bytes(base64.b64decode(logo))

name=Image.new("RGB",(300*S,66*S),"white")
d=ImageDraw.Draw(name)
text(d,(0,1),"Levier",31)
text(d,(0,43),"Founder · LEVX Ascensores",14)
name.save(OUT / "levier-name.png",optimize=True)

frames=[]
for i in range(120):
    t=i/20
    if t<0.6: opening,floor=1,2
    elif t<1.3: opening,floor=1-ease((t-.6)/.7),2
    elif t<2.1: opening,floor=0,0
    elif t<2.9: opening,floor=0,1
    elif t<3.6: opening,floor=0,2
    elif t<4.5: opening,floor=ease((t-3.6)/.9),2
    else: opening,floor=1,2
    im=Image.new("RGB",(520*S,100*S),"white")
    d=ImageDraw.Draw(im)
    line(d,[(0,95),(520,95)],"#d8d8d5")
    # Floor indicator advances, then arrival causes the doors to open.
    line(d,[(449,16),(449,5)],ORANGE,1.5)
    line(d,[(445,9),(449,5),(453,9)],ORANGE,1.5)
    text(d,(460,1),str(floor),17,ORANGE)
    rect(d,(430,25,492,94),"white",INK,1)
    rect(d,(434,29,488,93),"#f4f4f3")
    text(d,(461,55),"LEVX",13,INK,"mt")
    # Panels retreat sideways inside the doorway; there are no scene cuts.
    panel=27*(1-opening)
    if panel>0:
        rect(d,(434,29,434+panel,93),"#e3e3e1")
        rect(d,(488-panel,29,488,93),"#e3e3e1")
        line(d,[(434+panel,29),(434+panel,93)],"#a5a5a0")
        line(d,[(488-panel,29),(488-panel,93)],"#a5a5a0")
    line(d,[(430,25),(492,25)],ORANGE,2)
    rect(d,(500,54,504,58),ORANGE)
    frames.append(im)

palette=frames[0].quantize(colors=64)
colors=palette.getpalette()
white=palette.getpixel((0,0))
colors[white*3:white*3+3]=[255,255,255]
palette.putpalette(colors)
frames=[f.quantize(palette=palette,dither=Image.Dither.NONE) for f in frames]
for f in frames:
    colors=f.getpalette()
    white=f.getpixel((0,0))
    colors[white*3:white*3+3]=[255,255,255]
    f.putpalette(colors)
frames[0].save(OUT / "elevator-arrival.gif",save_all=True,append_images=frames[1:],duration=50,loop=0,optimize=True,disposal=1)
frames[0].convert("RGB").save(OUT / "elevator-arrival-still.png",optimize=True)
with Image.open(OUT / "elevator-arrival.gif") as gif:
    assert gif.n_frames>20
    assert gif.size==(1040,200)
    assert (OUT / "elevator-arrival.gif").stat().st_size<500000
print("GIF:", (OUT / "elevator-arrival.gif").stat().st_size, "bytes")
