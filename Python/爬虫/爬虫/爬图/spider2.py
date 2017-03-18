import re
import urllib2
import urllib
import threading
import time
from time import ctime,sleep


herf = []

img_url = []
img_url2 = []
threads = []
lock = threading.Lock()
def get_herf(page):
    address = []
    try:
            url = "http://www.meizitu.com/a/list_1_%d.html" %page
            request = urllib2.Request(url)
            respond = urllib2.urlopen(request,timeout=10)
            content = respond.read()
            pattern = re.compile('<p><a href="(.*?)"  target=.*?><img.*?src.*?style.*?/></a></p>',re.S)
            #print content
            result = re.findall(pattern,content)
            #print result
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

def get_imgurl(herf):
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
                print "ingurl error"
                pass
            except StandardError, e:
                print "ingurl error"
                print e
                pass
    return address

def read(jpg):
    global img_url
    content = urllib2.urlopen(jpg).read()
    return content

def grab(content,name):
    with open(str(name) + '.jpg', 'w') as f:
        f.write(content)
        print "finished",str(name), ctime()

def get_content():
    global img_url, img_url2
    lock.acquire()
    try:
        herf = get_herf(1)
        img_url = get_imgurl(herf)
        img_url2 = list(img_url)
        for item in img_url2:
            if item in img_url:
                content = read(item)
                img_url.remove(item)
                grab(content,img_url2.index(item))
            elif len(img_url) == 0:
                break
            else:
                pass
    except StandardError, e:
            print "get_content(), error"
            print e
            pass
    finally:
        lock.release()


def main():
    for t in xrange(4):
        t = threading.Thread(target=get_content)
        threads.append(t)
    for i in xrange(4):
        threads[i].start()
        threads[i].join()




main()


"""
a = threading.Thread(target=get_content)
b = threading.Thread(target=get_content)
c = threading.Thread(target=get_content)
d= threading.Thread(target=get_content)
a.start()
b.start()
c.start()
d.start()
"""