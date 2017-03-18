
import urllib
import Image
import StringIO

url = 'http://huge:file@www.pythonchallenge.com/pc/return/cave.jpg'


a = urllib.urlopen(url)
image = a.read()
j = StringIO.StringIO(image)

img = Image.open(j)


size = img.size
cord = []
for i in xrange(0,size[0],2):
    for j in xrange(0,size[1],2):       
        cord.append((i,j))
for i in xrange(1,size[0],2):
    for j in xrange(1,size[1],2):       
        cord.append((i,j))
        
size1 =(size[0]/2,size[1]/2)
print size1
n = Image.new('RGB',size1)

for i in cord:
    val =img.getpixel(i)
    c = (i[0]/2,i[1]/2)
    n.putpixel(c,val)
n.show()
