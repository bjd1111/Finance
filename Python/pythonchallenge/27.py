# -*- coding: UTF-8 -*-
import bz2
import Image
import string

zigzag = Image.open('zigzag.gif')
#获取图像的图像数据
zigstr = zigzag.tostring()
#获得图片的调色板数据
palette = zigzag.palette.getdata()[1][::3]
#用调色板数据替换掉图像数据，从而得到一组灰度值数据
#首先要生成一张转化对照表

transtable = string.maketrans(''.join([chr(i) for i in xrange(256)]), palette)
#然后开始转换
zigtrans = zigstr.translate(transtable)
#提取前面得到的两组数据的不同字节
ziglen = len(zigstr)
diffs = [(zigstr[i], zigtrans[i - 1])
         for i in xrange(1, ziglen) if zigstr[i] != zigtrans[i - 1]]
diffs_first = ''.join([p[0] for p in diffs])
diffs_second = ''.join([p[1] for p in diffs])
#其中diffs_first看起来十分像是 bz2 格式的数据，于是使用bz2解压
content = bz2.decompress(diffs_first)
#得到content里面包含了一大堆python保留字
#把“图像数据”与“灰度数据”两组数据中有差别的字节的坐标在一张新图上标记出来
im=Image.new('1', zigzag.size, 0)
im.putdata([zigstr[i] == zigtrans[i - 1] for i in xrange(1, ziglen)])
im.save('27.jpg')
#按照新画图片的提示，在content中找出不属于python保留字的字串
words = list(set(content.split()))
py_key_words = ['and', 'elif', 'global', 'or', 'yield', 'assert', 'else', 'if',
                'pass', 'break', 'except', 'import', 'print', 'class', 'exec',
                'in', 'raise', 'continue', 'finally', 'is', 'return', 'def',
                'for', 'lambda', 'try', 'del', 'from', 'not', 'while']
result = [w for w in words if w not in py_key_words]
print result

