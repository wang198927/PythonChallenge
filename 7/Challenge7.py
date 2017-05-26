from PIL import Image

im = Image.open('oxygen.png')
# for j in range(0, im.size[1]):
#     flag = 1
#     for i in range(0,im.size[0]):
#         rbga = im.getpixel((i,j))
#         if(rbga[0]==rbga[1]==rbga[2]):
#             continue
#         else:
#             flag = 0
#     if(flag):
#         print(j)



print(''.join([chr(i[0]) for i in [im.getpixel((j, im.size[1] / 2)) for j in range(0, im.size[0],7)]]))

key = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print(''.join(chr(i) for i in key))

# import PIL.Image
# print(PIL.Image.open('oxygen.png').tobytes()[108188:110620:28])