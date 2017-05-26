from urllib import request
from urllib import response
import re
import string

urls = ["http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=21232"]

for url in urls:
    # url_request = request.Request(url)
    urlResponse = request.urlopen(url).read()
    #urlResponse = "aaa111ccc"
    matchPattern = "(\d+)"
    numbersObj = re.search(matchPattern,str(urlResponse))
    if(numbersObj):
        numbers = numbersObj.group(1)
        #numbers = numbersObj[0]
        nextUrl = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+ numbers
        urls.append(nextUrl)
        print(numbers)
    else:
        print(url)
        print(urlResponse)

