from PIL import Image

i = Image.open('crs_clear.png')
X, Y = i.size
delta = 5

for x in range(X):
     for y in range(Y):
             p = i.getpixel((x,y))
             if 248 - delta <= p[0] <= 248 +delta and 249-delta <= p[1] <= 249+delta and 248-delta <= p[2] <= 248+delta:
                     i.putpixel((x,y), (255,255,255))

i.save('crs-white.png')
 