
#encoding: UTF-8
import threading
from threading import Thread
from Queue import Queue
from time import sleep
#q是任务队列
#NUM是并发线程总数
#JOBS是有多少任务
q = Queue()
NUM = 5
JOBS = 10
#具体的处理函数，负责处理单个任务
def do_somthing_using(arguments):
    print arguments
#这个是工作进程，负责不断从队列取数据并处理
def working():
    while True:
        arguments = q.get()
        do_somthing_using(arguments)
        sleep(1)
        q.task_done()
#fork NUM个线程等待队列
for i in range(NUM):
    t = Thread(target=working)

    t.setDaemon(True)
    t.start()
#把JOBS排入队列
for i in range(JOBS):
    q.put(i)
#等待所有JOBS完成
q.join()







"""
import threading
from time import ctime,sleep
a = []
for i in xrange(1000):
    a.append(i)

def main():
    global a
    b= list(a)
    if lock.acquire():
        for i in b:
            print a, "PP", threading.currentThread().getName()
            if i in a:

                a.remove(i)

                print a, ctime(), threading.currentThread().getName()
        else:
            pass

        lock.release()

    sleep(4)
def Mthreads():
        threads =[]
        for t in xrange(4):
            t = threading.Thread(target=main)
            threads.append(t)
        for i in xrange(4):
            threads[i].start()
            threads[i].join()
lock = threading.Lock()
Mthreads()
print ctime()

"""