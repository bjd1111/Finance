# 'encoding: UTF-8'
__author__ = 'apple'

import re
import urllib2
import threading
from threading import Thread
from Queue import Queue
import time
from time import sleep, ctime


q = Queue()         # 初始化队列
NUM = 200            # 线程数
imgurl = []         # 保存图片地址的list
pages = 6


class webinfo:
    def __init__(self):
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent }
    def get_herf(self, page):                                        #取得子网页链接
        address = []
        try:
                url = "http://www.meizitu.com/a/list_1_%d.html" %page
                request = urllib2.Request(url)
                respond = urllib2.urlopen(request,timeout=10)
                content = respond.read()
                pattern = re.compile('<p><a href="(.*?)"  target=.*?><img.*?src.*?style.*?/></a></p>', re.S)
                result = re.findall(pattern, content)
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

    def get_imgurl(self, herf):              #取得img的url
        address = []
        for url in herf:
                try:
                    request = urllib2.Request(url)
                    respond = urllib2.urlopen(request,timeout=10)
                    content = respond.read().decode("gbk")
                    pattern = re.compile('<img.*?alt=".*?" src="(.*?)" /><br />' , re.S)
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
class spider:                                       #初始化spider类
    def __init__(self):
        self.name =  "spider 1"

    def read(self,jpg):                             #读取网页内容
        content = urllib2.urlopen(jpg).read()
        return content

    def grab(self,content,category_name, name):     #下载到本地当前目录
        with open(str(category_name)+"_"+str(name) + '.jpg', 'w') as f:
            f.write(content)
            print "finished saving picture:",str(category_name)+"_"+str(name), ctime()

def download(url):                                  #设置具体的处理函数，负责处理单个任务
    a = spider()
    content = a.read(url)
    a.grab(content,pages,imgurl.index(url))

def working():      #这个是工作进程，负责不断从队列取数据并处理
    while True:
        arguement = q.get()
        download(arguement)
        q.task_done()           #在完成这项工作之后，使用 queue.task_done() 函数向任务已经完成的队列发送一个信号。

for l in xrange(1, 5):   #取得1-5页的img url
    a = webinfo()
    herf = a.get_herf(l)
    jpg = a.get_imgurl(herf)
    print jpg
"""
    for i in jpg:
        imgurl.append(i)


print "total:", len(imgurl), "pictures"
print "processing... "


print "++++start saving++++"
for n in range(NUM):                 #初始化线程
        t = Thread(target=working)
        t.setDaemon(True)            #设置守护线程
        t.start()                   #开始
for i in imgurl:                     #导入到queue
    q.put(i)
q.join()        #对队列执行 join 操作，实际上意味着等到队列为空，再退出主程序。！！！！！！！！！有待完善，有bug
"""