"""
import Image
image  = Image.open('mozart.gif')


#for i in xrange(429,434):
#    print i,0,'color', image.getpixel((i,0))




def pink():
    pink_cord = []
    pink = []
    i,j  = image.size
    n = 0
    for y in xrange(j):
        for x in xrange(i):
            if image.getpixel((x,y)) == 195:
                pink_cord.append((x,y))
    
    for i in xrange(0,len(pink_cord),5):
        b = pink_cord[i:i+5]
        pink.append(b)
    
    return pink
        

def crop_cord():
    cord = []
    a = 0
    b = 0
    for item in pink():
        i,j =  item[-1]

        #print i,j
        c = []
        if j-b ==0:
            for x in xrange(a,i):
                c.append((x,0))
        elif j-b ==1:
            for x in xrange(a,image.size[0]):
                    
                c.append((x,b))
            
            for x in xrange(0,i):
                c.append((x,j))           
        cord.append(c)
        a = item[-1][0]
        b = item[-1][1]
        
    return cord

def reverse(cord):
    a = []
    c = cord
    for i in xrange(len(cord)):
        a.append(c.pop())
    return a



img = Image.new('P',(2000,1000))
def paste(img):
    col = 0
    for i in crop_cord():
        #i = reverse(n)
        
        val = []
        row = 0
        
        for item in i:
            val.append(image.getpixel(item))
            #print val
        #print val
        for i in xrange(len(val)):
            #print i,col
            img.putpixel((i,col),val[i])
            row +=1

        col+=1
        #print 'EEEEEEEEEEEEEEEEEEENNNNNNNNNNNNNNNNNNNNDDDDDDDDDDD'
    img.show()

paste(img)



"""

import Image
def straighten(source):
     target = source.copy()
     for y in range(source.size[1]):
         line = [source.getpixel((x, y)) for x in range(source.size[0])]
         
         pink = line.index(195)
         line = line[pink:] + line[:pink]
         
         for x, pixel in enumerate(line):
             target.putpixel((x, y), pixel)
     return target

out = straighten(Image.open("mozart.gif"))
out.show()
            
