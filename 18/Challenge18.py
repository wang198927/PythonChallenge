#后缀改为brightness,下载deltas.gz
import gzip,difflib

fd = gzip.open("deltas.gz","r")
txt = fd.read().splitlines()
fd.close()
left=[]
right=[]

for rows in txt:
    left.append(rows[:53])
    right.append(rows[56:])

compareResult = list(difflib.ndiff(left,right))

png = ['', '', '']
for row in compareResult:
    str1 = str(row[4:-1])
    print(row)
    # print(row)
    # print(bytes)
    if row[0] == '-':
        png[0] += str1
    elif row[0] == '+':
        png[1] += str1
    elif row[0] == ' ':
        png[2] += str1

for i in range(3):
    open('out18_%d.png' % i, 'wb').write(png[i])