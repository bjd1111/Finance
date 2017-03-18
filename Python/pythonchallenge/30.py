# -*- coding: UTF-8 -*-
import Image
import re
import urllib

url = 'http://repeat:switch@www.pythonchallenge.com/pc/ring/yankeedoodle.csv'
cvs_values = re.findall(r'[\d.]+', urllib.urlopen(url).read())
visual = Image.new('F', (53, 139))
#在这个cvs文件当中，共有7367个浮点数。把7367进行因式分解，得到 7367 = 53 * 139 。于是，把每一个浮点数乘以256作为像素值，生成一张 53 * 139 的灰度图。
visual.putdata(map(float, cvs_values), 256)
#把图片旋转270度角

visual = visual.transpose(Image.ROTATE_270)
#翻转图片
visual = visual.transpose(Image.FLIP_LEFT_RIGHT)
visual.show()
#把cvs数据分成三个数字一组，按照图片中的公式计算结果字符串
result = []
for i in xrange(0, len(cvs_values)-2, 3):
    result.append(chr(int(
        cvs_values[i][5] + cvs_values[i + 1][5] + cvs_values[i + 2][6])))
result = ''.join(result)
print result
