import re
from urllib import request
url = 'http://www.pythonchallenge.com/pc/hex/unreal.jpg'
#start = 30203
#start = 2123456743

username = 'butter'
password = 'fly'
p = request.HTTPPasswordMgrWithDefaultRealm()

p.add_password(None, url, username, password)

handler = request.HTTPBasicAuthHandler(p)
opener = request.build_opener(handler)
start = 1152983631
end = 2123456789
find = re.compile(r'bytes \d*-(\d*)')
while start<end:
    rq = request.Request(url)
    rq.add_header('Range','bytes=%d-%d' % (start,end))
    f = opener.open(rq)
    start = re.findall(find,str(f.info()))
    if len(start)>0:
        start = int(start[0])+1
    #print f.info()
    open(r'D:\Projects\PythonChallenge\20\out20.zip','wb').write(f.read())