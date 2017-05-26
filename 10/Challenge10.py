# a ="1"
# lastNumber=0
# for i in range(0,30):
#     pos = 0
#     temp=""
#     while pos < len(a):
#         count = 1
#         while pos+1<len(a) and a[pos] == a[pos+1]:
#             pos += 1
#             count +=1
#         temp = temp  + str(count)+ a[pos]
#         pos += 1
#     a = temp
# print(len(a))


import re
def describe(s):
    sets = re.findall("(1+|2+|3+)", s)  # like "111", "2", ...
    return "".join([str(len(x))+x[0] for x in sets])

s = "1"
for dummy in range(30):
    s = describe(s)

print(len(s))