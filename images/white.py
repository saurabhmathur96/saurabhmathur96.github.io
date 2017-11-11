from PIL import Image

i = Image.open('gravitas.png')
X, Y = i.size
delta = 10
for x in range(X):
     for y in range(Y):
             p = i.getpixel((x,y))
             if 141 - delta <= p[0] <= 141 +delta and 176-delta <= p[1] <= 176+delta and 176-delta <= p[2] <= 176+delta:
                     i.putpixel((x,y), (255,255,255))
 
i.save('gravitas-white.png')
