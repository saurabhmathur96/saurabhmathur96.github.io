from PIL import Image,ImageEnhance
import glob

for f in glob.glob('images/*.png'):
    i = Image.open(f)

    i = ImageEnhance.Sharpness(i).enhance(1.2)

    i.save(f)