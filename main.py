#!/usr/local/bin/python3
from PIL import Image, ImageOps
import sys

def main():
    path = sys.argv[1]
    outpath = path
    boder_colour = "white" # takes string and # colour codes
    min_border_percent = 5
    min_border_percent = min_border_percent / 100

    img = Image.open(path)
    width, height = img.size

    if width >= height:
        min_border = int(height * min_border_percent) 
    else:
        min_border = int(width * min_border_percent)

    diff = int((abs(width - height) / 2) + min_border)
    if width > height:
        border = (min_border, diff, min_border, diff)
    elif height > width:
        border = (diff, min_border, diff, min_border)
    else:
        border = min_border

    imgWithBorder = ImageOps.expand(img, border = border, fill = boder_colour)
    imgWithBorder.save(outpath) 








if __name__ == "__main__":
    
    main()


