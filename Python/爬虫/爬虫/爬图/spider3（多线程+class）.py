import re
import urllib2
import threading
from time import ctime
import threading
from threading import Thread
from Queue import Queue
import time
from time import sleep
import os

q = Queue()
NUM = 20
imgurl = []
pages = 1


class web_info:
    def __init__(self):
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent }
    def get_herf(self, page):
        address = []
        try:
                url = "http://www.meizitu.com/a/list_1_%d.html" %page
                request = urllib2.Request(url)
                respond = urllib2.urlopen(request,timeout=10)
                content = respond.read()
                pattern = re.compile('<p><a href="(.*?)"  target=.*?><img.*?src.*?style.*?/></a></p>',re.S)
                result = re.findall(pattern,content)
                for item in result:
                   address.append(item)
        except urllib2.URLError, e:
                    print e
                    print "herf error"
                    pass
        except StandardError, e:
                    print e
                    print "herf error"
                    pass
        return address
    def get_imgurl(self,herf):
        address = []
        for url in herf:
                try:
                    request = urllib2.Request(url)
                    respond = urllib2.urlopen(request,timeout=10)
                    content = respond.read().decode("gbk")
                    pattern = re.compile('<img.*?alt=".*?" src="(.*?)" /><br />',re.S)
                    result = re.findall(pattern,content)
                    for item in result:
                        address.append(item)
                except urllib2.URLError, e:
                    print e
                    print "imgurl error"
                    pass
                except StandardError, e:
                    print "imgurl error"
                    print e
                    pass
        return address
class spider:
    def __init__(self):
        self.name = "spider 1"
    def read(self,jpg):
        content = urllib2.urlopen(jpg).read()
        return content
    def grab(self,content,category_name, name):

        with open(str(category_name)+"_"+str(name) + '.jpg', 'w') as f:
            f.write(content)
            print "finished saving picture:",str(category_name)+"_"+str(name), ctime()

def download(url):
    a = spider()
    content = a.read(url)
    a.grab(content,pages,imgurl.index(url))
def working():
    while True:

        arguement = q.get()
        download(arguement)
        q.task_done()

for i in xrange(1,2):
    a = web_info()
    herf = a.get_herf(i)
    imgurl =  a.get_imgurl(herf)

    for i in range(NUM):
            t = Thread(target=working)
            t.setDaemon(True)
            t.start()
    for i in imgurl:
        q.put(i)
    q.join()


"""
def main():
    a = web_info()
    herf = a.get_herf(1)
    imgurl =  a.get_imgurl(herf)
    b = list(imgurl)

    c =spider()
    num = 0
    while len(imgurl) != 0:
        try:
            print threading.currentThread().getName()
            content = c.read(imgurl[0])
            c.grab(content,1,num)
            num += 1
            #lock.acquire()
            imgurl.remove(imgurl[0])
            #lock.release()
        except StandardError, e:
            print e

"""

"""
def main():
    a = web_info()

    for page in xrange(1,200):
        herf = a.get_herf(page)
        imgurl =  a.get_imgurl(herf)
        b = spider()
        for i in imgurl:
            content = b.read(i)
            b.grab(content,page,imgurl.index(i))
            print threading.currentThread().getName()

"""


"""
  def update(self,jpg):
        global imgurl
        imgurl.remove(jpg)

    def downloadall(self):
        num = 0
        b = list(imgurl)
        try:
            for i in b:
                content = self.read(i)
                self.grab(content,1,num)
                num += 1
                #lock.acquire()
                self.update(i)
                #lock.release()
        except StandardError,e:
            print e
            pass
class multithreads:
    def __init__(self):
        self.name = "this is a multi-threads class"
    def Mthreads(self):
        threads =[]
        for t in xrange(4):
            t = threading.Thread(target=working)
            threads.append(t)
        for i in xrange(4):
            threads[i].start()
            t.setDaemon(True)

"""