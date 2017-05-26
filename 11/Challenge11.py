from PIL import Image,ImageDraw

im = Image.open("cave.jpg")

weight,height = im.size

odd = Image.new(im.mode,(int(weight/2),int(height/2)))
even = Image.new(im.mode,(weight//2,height//2))

for y in range(0,height-1):
    for x in range(0,weight-1):
        pixel = im.getpixel((x,y))
        if x%2 == 0 and y%2 == 0:
            even.putpixel((x//2, y//2), pixel)
        elif x%2 == 1 and y%2 ==1:
            odd.putpixel(((x-1) // 2, (y-1) // 2), pixel)
        else:
            pass

odd.save("odd.jpg")
even.save("even.jpg")