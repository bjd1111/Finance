# -*- coding: UTF-8 -*-
import Image

bell = Image.open('bell.png')
#获取图片中所有像素的g值
bell.load()
green = bell.split()[1]
data = list(green.getdata())
message = []
#计算差值的绝对值
for i in xrange(0, len(data) - 1, 2):
    if abs(data[i] - data[i + 1]) != 42:
        message.append(chr(abs(data[i] - data[i + 1])))
        
print ''.join(message)


print "Guido Van Rossum".split()[0]
