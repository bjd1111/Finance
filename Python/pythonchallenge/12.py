import Image
import os

f = open('evil2.gfx')
content = f.read()

def writen(n,content):
    name = '12/' + str(n)
    if os.path.exists(name):
        f0 = open(name)
        c = f0.read()
        content = c+content
        
 
    f1 = file(name,'w')
    f1.write(content)
    f1.close()
    
i=0
for s in content:
    
    n =i%5
    writen(n,s)
    i+=1

f.close

