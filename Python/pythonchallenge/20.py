import urllib
import re

url = 'http://butter:fly@www.pythonchallenge.com/pc/hex/unreal.jpg'
opener = urllib.URLopener()

"""
opener.addheader('Range','bytes=30203-')
content = opener.open(url)
print content.info()
print content.read()


opener.addheader('Range','bytes=30237-')
content = opener.open(url)
print content.info()
print content.read()



opener.addheader('Range','bytes=30284-')
content = opener.open(url)
print content.info()
print content.read()


opener.addheader('Range','bytes=30295-')
content = opener.open(url)
print content.info()
print content.read()

opener.addheader('Range','bytes=30313-')
content = opener.open(url)
print content.info()
print content.read()


opener.addheader('Range','bytes=2123456789-')
content = opener.open(url)
print content.info()
print content.read()


opener.addheader('Range','bytes=2123456743-')
content = opener.open(url)
print content.info()
print content.read()
# the password is your new nickname in reverse。 (password： redavni)


opener.addheader('Range','bytes=1152983631-')
content = opener.open(url)
print content.info()
print content.read()
"""

opener.addheader('Range','bytes=1152983631-')
content = opener.open(url)
print content.info()
data =  content.read()
f = open('20.zip', 'w')
f.write(data)
f.close()



"""
def data(byte):
    bytes = 'bytes='+str(byte)+'-'
    opener.addheader('Range',bytes)
    content = opener.open(url)
    print content.read()
    length = re.findall(r'Content-Length: (.*)\r\nConnection',str(content.info()),re.S)
    return length[0]

byte = 30203


for i in xrange(10):
    byte = data(byte)

"""
