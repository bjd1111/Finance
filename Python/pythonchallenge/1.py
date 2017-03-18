# -*- coding: utf-8 -*-
__author__ = 'apple'
code = "g fmnc wms bgblr rpylqjyrc gr zw " \
       "fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr g" \
       "l zw fylb gq glcddgagclr ylb rfyr'q ufw rf" \
       "gq rcvr gq qm jmle. sqgle " \
       "qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

letters = 'abcdefghijklmnopqrstuvwxyz'


dic = dict(zip([a for a in letters], [b for b in xrange(1,27)]))
    
dic1 = dict(zip([b for b in xrange(1,27)],[a for a in letters]))

dic.update({'.':'.','(':'(',')':')',' ':' '})

def translate(content):
    b = ''
    for i in content:
        if i in letters:
            a = dic[i]+2
            b += dic1[a%26]
        else:
            b+= i
    return b

print translate(code)
print translate('map')


"""
import string
table = string.maketrans(
    string.ascii_lowercase,
    string.ascii_lowercase[2:]+string.ascii_lowercase[:2])
string.translate(code,table) 
"""


"""
o =''
for x in code:
	if ord(x)>=ord('a') and ord(x)<=ord('z'):
		o+=chr((ord(x)+2-ord('a'))%26+ord('a'))
	else:
		o+=x
print o

"""
