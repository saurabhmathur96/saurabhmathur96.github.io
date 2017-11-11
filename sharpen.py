from PIL import Image,ImageEnhance


i = Image.open('images/digit.png')

i = ImageEnhance.Sharpness(i).enhance(2)

i.save('images/digit.png')