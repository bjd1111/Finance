import Image
image = Image.open('wire.png')
size = image.size
cord = []
for i in xrange(size[0]):
    cord.append((i,0))

    



steps = []
i = 100
while i >0:
    steps.append((i,i-1,i-1,i-2))
    i = i-2

    
x = 0
y = 0
cor1= []
num = 0
for step in steps:
    for x in xrange(num,num+step[0]):
        cor = (x,y)
        cor1.append(cor)
    x = step[0]-1 + num
 
    for y in xrange(num+1,num+step[1]+1):
        cor = (x,y)
        cor1.append(cor)
    y = step[1]+num



    for x in xrange(step[2]+num-1,num-1,-1):
        cor = (x,y)
        cor1.append(cor)
    x = num
        
    for y in xrange(step[3]+num,num,-1):
        cor = (x,y)
        cor1.append(cor)
    y = num + 1
    
    num += 1


img = Image.new('RGB',(100,100))

for i in xrange(len(cord)):
    #print cord[i]
    val = image.getpixel(cord[i])
    img.putpixel(cor1[i],val)
img.show()
    
