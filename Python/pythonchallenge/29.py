# -*- coding: UTF-8 -*-
import bz2
import urllib

url = 'http://repeat:switch@www.pythonchallenge.com/pc/ring/guido.html'
html = urllib.urlopen(url).read()
#提取出仅由空白字符组成的行
html_lines = html.split('\n')
whitespace_lines = [l for l in html_lines if len(l.strip()) == 0]
#把每一行空白字符的长度转换成字符输出
msg = ''.join([chr(len(l)) for l in whitespace_lines])
#使用bz2解压
result = bz2.decompress(msg)
print result
