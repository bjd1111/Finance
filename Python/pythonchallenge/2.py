import urllib
import re
a = urllib.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html')
content = a.read()
pattern  = re.compile('-->.*?<!--(.*?)-->',re.S)
result = re.findall(pattern,content)
code = "".join(result).replace("\n","")

content = "!!!@@@$$"
def find(content):
    dic={}
    for i in content:
        if i in dic:
            dic[i]+=1
        else:
            dic[i] = 1

    return dic


def mini(content):
    b={}
    a = find(content)
    for i in a.keys():
        if a[i] == min(a.values()):
            b.update({i:a[i]})
    return b
        
        
    
    

print mini(code)

for i in mini(code):
    print i


"""
for i in content:
    a[i] = a.get(i,0)+1
"""
