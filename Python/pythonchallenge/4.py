
import urllib
import re

num0 = 12345
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

def next(num):
    url1 = url + str(num)
    a = urllib.urlopen(url1)
    content = a.read()

    pattern  = re.compile('is (.*)',re.S)
    result = re.findall(pattern,content)
    print content
    return result[0]


def go():
    num = num0
    while True:
        if num == 16044:
            num = num/2
        if num == 82682:
            num = 63579
        next(num)
        num = next(num)
        


go()
