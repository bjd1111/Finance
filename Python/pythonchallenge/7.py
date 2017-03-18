
import urllib
import StringIO
import Image

url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'


 
a = urllib.urlopen(url)
image = a.read()
j = StringIO.StringIO(image)
box = (0,42,608,52)
cord = (0,45,608,45)
o =  Image.open(j)
k = o.convert('L')


t=[]
y = 45
for x in xrange(608/7+1):
    xy = (x*7,y)
    b = k.getpixel(xy)
    t.append(b)
    
def tras(codes):  
    code = ''   
    for i in codes:
        code+=chr(i)
    print code
tras(t)
code2 = [105, 110, 116, 101, 103, 114, 105, 116, 121]
tras(code2)
