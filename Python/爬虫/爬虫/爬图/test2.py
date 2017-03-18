__author__ = 'apple'
#coding:gb2312
import urllib
import re
import threading

url = ['http://henan.weather.com.cn/index.shtml\',\'http://gd.weather.com.cn/index.shtml\',\'http://xj.weather.com.cn/index.shtml']
def getlist(url):
    page=urllib.urlopen(url)
    html=page.read()
    page.close()
    reg='<a title=.*?>(.*?)</a>.*?<span>(.*?)</span>.*?<b>(.*?)</b>'
    weatherList = re.compile(reg).findall(html)
    for weather in weatherList:
        print str(weather[0]+weather[1]+"/"+weather[2]).decode('utf-8').encode('gb2312')
def main():
    threads = []
    nloops = range(len(url))
    for i in nloops:
        t = threading.Thread(target=getlist,args=[url[i],])
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
if __name__ == '__main__':
    main()