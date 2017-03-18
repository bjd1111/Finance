# -*- coding: UTF-8 -*-
import Image
import urllib

ufo_1 = Image.open('mandelbrot.gif')
def mandelbrot(left=0.34, bottom=0.57, width=0.036, height=0.027,
               max=128, size=(640, 480)):
    xstep = width / size[0]
    ystep = height / size[1]
    for y in xrange(size[1] - 1, -1, -1):
        for x in xrange(size[0]):
            c = complex(left + x * xstep, bottom + y * ystep)
            z = 0+0j
            for i in xrange(max):
                z = z * z + c
                if abs(z) > 2:
                    break
            yield i

#绘制一个新的分形图
ufo_2 = ufo_1.copy()
ufo_2.putdata(list(mandelbrot()))
ufo_2.show()
#查找两副图片的差异
differences = [(a - b) for a, b in zip(ufo_1.getdata(), ufo_2.getdata()) if a != b]
#根据差值绘制出一张新的图片
plot = Image.new('1', (23, 73))
plot.putdata([i < 16 for i in differences])
#把图片放大10倍显示
plot.resize((230, 730)).show()










"""
def mandelbrot():
    size = (640,480)
    palette = [(50,5,50),(100,186,5),(150,45,12),(200,74,35)]
    img = Image.new('RGB',size)
    for Py in xrange(size[1]):
        for Px in xrange(size[0]):
            x0 = (Px - size[0]/2.0)*4.0/size[0]
            y0 = (Py - size[1]/2.0)*4.0/size[1]
            x = 0
            y = 0
            iteration = 0
            max_iteration = 100
           
            while x*x + y*y < 2*2  and  iteration < max_iteration: 

                xtemp = x*x - y*y + x0
                y = 2*x*y + y0
                x = xtemp
                iteration = iteration + 1
                color = palette[iteration%4]
            
            img.putpixel((Px,Py), color)
    img.show()
  
mandelbrot()


"""





'''
import numpy as np
import pylab as pl
import time
from matplotlib import cm

def iter_point(c):
    z = c
    for i in xrange(1, 100): # 最多迭代100次
        if abs(z)>2: break # 半径大于2则认为逃逸
        z = z*z+c
    return i # 返回迭代次数
    
def draw_mandelbrot(cx, cy, d):
    """
    绘制点(cx, cy)附近正负d的范围的Mandelbrot
    """
    x0, x1, y0, y1 = cx-d, cx+d, cy-d, cy+d 
    y, x = np.ogrid[y0:y1:200j, x0:x1:200j]
    c = x + y*1j
    start = time.clock()
    mandelbrot = np.frompyfunc(iter_point,1,1)(c).astype(np.float)
    print "time=",time.clock() - start
    pl.imshow(mandelbrot, cmap=cm.Blues_r, extent=[x0,x1,y0,y1])
    pl.gca().set_axis_off()
    
x,y = 0.27322626, 0.595153338

pl.subplot(231)
draw_mandelbrot(-0.5,0,1.5)
for i in range(2,7):    
    pl.subplot(230+i)
    draw_mandelbrot(x, y, 0.2**(i-1))
pl.subplots_adjust(0.02, 0, 0.98, 1, 0.02, 0)
pl.show()
'''
