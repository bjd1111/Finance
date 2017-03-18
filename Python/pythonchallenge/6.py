
import re
from zipfile import ZipFile

num0 = 90052
z = ZipFile('channel.zip')
w = ''
is_num = True
def next(num):
    global w,is_num
    fil ='channel/'+ str(num)+'.txt'
 
    a = open(fil)
    content = a.read()

    pattern  = re.compile('is (.*)',re.S)
    result = re.findall(pattern,content)
    
 
 
    if result == []:
        is_num = False
        return
    name = str(result[0])+'.txt'
    if len(result) != 0:
        w = w + z.getinfo(name).comment
       

    print content
    a.close()
    return result[0]

def go():
    num = num0
    while is_num:
        next(num)
        num = next(num)
        


go()

print w

    
