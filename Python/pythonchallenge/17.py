# -*- coding: utf-8 -*-
import urllib,urllib2
import re
import bz2
import xmlrpclib
#import StringIO



#++++++++++++++++++++++++++++++++stage 1++++++++++++++++++++++++++++++++++++++++
num0 = 12345
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='
cookies = ''

def next(num):
    global cookies
    url1 = url + str(num)
    a = urllib.urlopen(url1)
    content = a.read()

    pattern  = re.compile('is (.*)',re.S)
    result = re.findall(pattern,content)


    
    cookie =  a.info().getheader('Set-Cookie')
    pattern1 = re.compile('info=(.*); expires',re.S)
    result1 = re.findall(pattern1,cookie)

    result1 = urllib.unquote_plus(result1[0])
    cookies+=result1

    
    print content
    return result[0]


def go():
    num = num0
    while True:
       
        if num =='83051':
           
            break
  
        num = next(num)

        
        

def print_code():

    go()
    code = cookies+'\x90'
    info = bz2.decompress(code)
    print info


    
#print_code()


#++++++++++++++++++++++++++++++++stage   2++++++++++++++++++++++++++++++++++++++++

url = 'http://www.pythonchallenge.com/pc/phonebook.php'

content = xmlrpclib.Server(url)

#print content.phone('Leopold')



#++++++++++++++++++++++++++++++++stage 3++++++++++++++++++++++++++++++++++++++++

message = "the flowers are on their way"
url = 'http://www.pythonchallenge.com/pc/stuff/violin.php'
req = urllib2.Request(url,
     headers={'Cookie': 'info=' + urllib.quote_plus(message)})
print urllib2.urlopen(req).read()


print 'answer is balloons'
