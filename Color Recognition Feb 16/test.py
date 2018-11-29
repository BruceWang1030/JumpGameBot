from PIL import Image, ImageDraw
import os
import math

im = Image.open("C:\Bruce\screenshotsaver\screenshot.png")
#im.show()
im_pixel = im.load()
width, height = im.size
draw = ImageDraw.Draw(im)

print(im_pixel[693,749])
