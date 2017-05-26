
f = open("evil2.gfx","rb")
txt = f.read()
f.close()

for i in range(5):
    f = open('%d.jpg' % i, 'wb')
    f.write(txt[i::5])
    f.close()