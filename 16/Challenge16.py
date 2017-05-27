#test
from PIL import Image
im = Image.open(r'mozart.gif')
newim = Image.new('RGB',(640,480))
for i in range(480):
    for j in range(640):
        if im.getpixel((j,i)) == 195:
            [newim.putpixel((k,i),im.getpixel(( (k+j)%640,i))) for k in range(640)]
            break
newim.save(r'out16.gif')