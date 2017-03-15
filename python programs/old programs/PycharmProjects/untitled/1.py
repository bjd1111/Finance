__author__ = 'apple'
import urllib2
content = urllib2.urlopen("http://www.baidu.com")
print content.read()
