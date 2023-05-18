#!/usr/local/bin/python3
import argparse
import os
import filetype
from PIL import Image, ImageOps


def process_picture(path: str, outpath: str, border_color: str, min_border_percent: int, keepOriginal: bool):
    if filetype.is_image(path):
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

        imgWithBorder = ImageOps.expand(img, border=border, fill=border_color)
        if not keepOriginal:
            imgWithBorder.save(outpath)
        else:
            dir = os.path.dirname(outpath)
            base = os.path.basename(outpath)
            new_base = os.path.splitext(
                base)[0] + "_border" + os.path.splitext(base)[1]
            new_path = os.path.join(dir, new_base)
            imgWithBorder.save(new_path)
    else:
        return


def process_picture_dir(path: str, outpath: str, border_color: str, min_border_percent: int, keepOriginal: bool):
    files = [f for f in os.listdir(
        path) if os.path.isfile(os.path.join(path, f))]
    for file in files:
        file_path = os.path.join(path, file)
        file_outpath = os.path.join(outpath, file)
        process_picture(file_path, file_outpath, border_color,
                        min_border_percent, keepOriginal)


def main():
    parser = argparse.ArgumentParser(
        description='Adding colored borders to pictures for social media to bring them to a 1:1 format.')
    parser.add_argument("Path", metavar="path", type=str,
                        help='the path to the image')
    parser.add_argument('-c', "--color", type=str, default="white",
                        help='the color of the border')
    parser.add_argument('-bp', "--borderpercentage", type=int, default=5,
                        help='the percentage of the border size')
    parser.add_argument('-k', "--keepOriginal", action=argparse.BooleanOptionalAction, default=False,
                        help='keep the original image')
    args = parser.parse_args()

    path = args.Path
    outpath = args.Path
    border_color = args.color
    min_border_percent = args.borderpercentage / 100
    keepOriginal = args.keepOriginal

    if os.path.isfile(path):
        process_picture(path, outpath, border_color,
                        min_border_percent, keepOriginal)
    elif os.path.isdir(path):
        process_picture_dir(path, outpath, border_color,
                            min_border_percent, keepOriginal)
    else:
        return


if __name__ == "__main__":
    main()
