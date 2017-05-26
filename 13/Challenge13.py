import xmlrpclib
xmlrpc = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print(xmlrpc.system.listMethods())
print(xmlrpc.system.methodHelp('phone'))
print(xmlrpc.phone('Bert'))
