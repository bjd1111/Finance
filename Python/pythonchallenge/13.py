
import urllib
import re
import xmlrpclib


url = 'http://www.pythonchallenge.com/pc/phonebook.php'

content = xmlrpclib.Server(url)
#print content.system.listMethods()
print content.phone('Bert')
