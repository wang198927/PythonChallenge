from PIL import Image,ImageDraw

img = Image.open("wire.png")

new_img = Image.new("RGB",(100,100))

count = 0
x = 0
y = 0
total = 99
up_flag = 0
left_flag = 0
down_flag = 0
right_flag = 1
for i in range(10000):
    old_pixel = img.getpixel((count,0))
    try:
        new_img.putpixel((x,y),old_pixel)
    except:
        print(x,y)
        print(total)
        print(right_flag,up_flag,left_flag,down_flag)
    else:
        if(up_flag):
            y += 1
        elif(left_flag):
            x -= 1
        elif(down_flag):
            y -= 1
        else:
            x += 1

        if(x==total and right_flag ==1):
            right_flag = 0
            up_flag = 1
        elif(y==total and up_flag==1):
            up_flag = 0
            left_flag = 1
        elif(x==(99-total) and left_flag == 1):
            left_flag = 0
            down_flag = 1
        elif(y==(99-total) and down_flag == 1):
            down_flag = 0
            right_flag = 1
            total -= 1
            y += 1
            x += 1
    count += 1
new_img.save('out14.png')
