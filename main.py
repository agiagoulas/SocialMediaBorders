#!/usr/local/bin/python3
from PIL import Image, ImageOps
import argparse

def main():
    parser = argparse.ArgumentParser(description='Adding borders to pictures for social media..')
    parser.add_argument("Path", metavar="path", type=str,
                        help='the path to the image')
    parser.add_argument('-c', "--colour", type=str, default="white",
                        help='the colour of the border')
    parser.add_argument('-bp', "--borderpercentage", type=int, default=5,
                        help='the percentage of the border size')
    args = parser.parse_args()

    path = args.Path
    outpath = args.Path
    border_colour = args.colour
    min_border_percent = args.borderpercentage / 100

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

    imgWithBorder = ImageOps.expand(img, border = border, fill = border_colour)
    imgWithBorder.save(outpath) 

if __name__ == "__main__":
    main()
