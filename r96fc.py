
# USAGE:
# python TCODfont.py /path/to/font/font.ttf 12

import sys
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from u8util import getCharID
from u8util import main_font_lut
from pathlib import Path
import os 

if len(sys.argv) < 3:
    print("Usage: r96fc.py {Font-Name} {Font-Size} [Font-Size-Multiplier]") 
else:
    fontpath = sys.argv[1]
    fontpoint = int(sys.argv[2])
    fontmul = float(sys.argv[3]) if len(sys.argv) > 3 else 1

    for i in range(0, 10000):
        image = Image.new('RGBA', [fontpoint * 2, fontpoint * 2])
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(fontpath, round(fontpoint * fontmul))    
        ch = getCharID(chr(i))
        if ch != None and main_font_lut[ch] != 0x0:
            path = "Render96font/gfx/"+main_font_lut[ch]+".png"
            size = font.getsize(chr(i))
            offset = font.getoffset(chr(i))
            print(f"{chr(i)}: {offset}")
            draw.text(((fontpoint / 2 - size[0] / 2), offset[1] / 6), chr(i), font=font, stroke_width=0, spacing=0)
            image = image.rotate(90).transpose(PIL.Image.FLIP_LEFT_RIGHT)
            image = image.crop((0, fontpoint, fontpoint * 2, fontpoint * 2))
            os.makedirs(os.path.dirname(path), exist_ok=True)
            image.save(path)