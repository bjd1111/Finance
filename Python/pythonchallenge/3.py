import urllib
import re
a = urllib.urlopen('http://www.pythonchallenge.com/pc/def/equality.html')
content = a.read()
pattern  = re.compile('<!--(.*?)-->',re.S)
result = re.findall(pattern,content)
code = "".join(result).replace("\n","")

pattern1 = re.compile('[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]')
result1 = re.findall(pattern1,code)

print "".join(result1)
