'''
30.10.2023 WebP to PNG Conversion Using Python
https://www.pycodemates.com/2023/10/webp-to-png-conversion-using-python.html
'''
from PIL import Image # Open a WebP image
import os

def one_image_conversion():
    webp_image = Image.open("input.webp")
    png_image = webp_image.convert("RGBA")
    png_image.save("output.png")

def many_image_conversion():
    webp_dir = "book1-webp"
    png_dir = "book1-png"
    os.makedirs(png_dir, exist_ok=True)
    curri = 0
    for filename in os.listdir(webp_dir):
        if filename.endswith(".webp"):
            webp_image = Image.open(os.path.join(webp_dir, filename))
            png_image = webp_image.convert("RGBA")
            png_image.save(os.path.join(png_dir, filename.replace(".webp", ".png")))
            curri += 1; print(curri)


if __name__ == "__main__":
    many_image_conversion()

