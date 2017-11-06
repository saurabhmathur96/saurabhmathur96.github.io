import os, sys
from PIL import Image
import glob

size = (240, 240)

for infile in glob.glob('images/*.png'):
    try:
        im = Image.open(infile)
        im.thumbnail(size, Image.ANTIALIAS)
        im.save(infile, 'PNG')
    except IOError:
        print ("cannot resize '%s'" % infile)