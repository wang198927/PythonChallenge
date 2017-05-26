

oriStr = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
oriStr = "map"
newStr = ""

# for x in oriStr:
#
#     if(('a'<=x and x<'y') or ('A'<=x and x<'Y')):
#         newStr += (chr(ord(x)+2))
#     elif(x == 'z'):
#         newStr += 'b'
#     elif(x == 'y'):
#         newStr += 'a'
#     else:
#         newStr += x

transtab = str.maketrans("abcdefghijklmnopqrstuvwxyz","cdefghijklmnopqrstuvwxyzab")
newStr = oriStr.translate(transtab)
print(newStr)

