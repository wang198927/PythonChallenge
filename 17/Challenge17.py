from urllib import request
from urllib import response
from http import cookies,cookiejar
import bz2
import xmlrpclib
import re
import string



#获取所有网址的cookies,然后用BZ解码

urls = ["http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=12345"]
cookieStr = b""
for url in urls:
    cookies = cookiejar.CookieJar()
    handler = request.HTTPCookieProcessor(cookies)
    opener = request.build_opener(handler)
    urlResponse = request.urlopen(url).read()
    cookieResponse = opener.open(url)
    for term in cookies :
        if term.name == "info":
            cookieStr += bytes(term.value,"utf8")
    #urlResponse = "aaa111ccc"
    print(cookieStr)
    matchPattern = "busynothing is (\d+)"
    numbersObj = re.findall(matchPattern,str(urlResponse))
    if(numbersObj):
        #numbers = numbersObj.group(1)
        numbers = numbersObj[0]
        nextUrl = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing="+ numbers
        urls.append(nextUrl)
        print(numbers)
    else:
        print(url)
        print(urlResponse)
        print(bz2.decompress(cookieStr))


#回顾13题，给莫扎特老爹打电话
server = xmlrpclib.Server(r'http://www.pythonchallenge.com/pc/phonebook.php')
print(server.phone('Leopold'))

#修改request header cookies
info='the flowers are on their way'
url='http://www.pythonchallenge.com/pc/stuff/violin.php'
req = request.Request(url, headers={'Cookie': 'info=' + info})
print(request.urlopen(req).read())