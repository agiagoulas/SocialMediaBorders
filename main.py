import typer
from PIL import Image, ImageOps
from typing import Optional

def main():
    path = "/Users/agiagoulas/Desktop/L1003917.jpg"
    outpath = "/Users/agiagoulas/Desktop/L1003917-out.jpg"
    # path = "/Users/agiagoulas/Desktop/L1003904.jpg"
    # outpath = "/Users/agiagoulas/Desktop/L1003904-out.jpg"
    boder_colour = "#fff" # takes string and # colour codes
    min_border_percent = 5 # in decimal percent
    min_border_percent = min_border_percent / 100

    img = Image.open(path)
    width, height = img.size
    print(img.size)
    

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

  
    print(imgWithBorder.size)






if __name__ == "__main__":
    
    typer.run(main)


