__author__ = 'apple'
import threading
from threading import Thread
from Queue import Queue
from time import sleep, ctime


q = Queue()
NUM = 2
JOBS = 10
a = [0,1,2,3,4,5,6,7,8,9]

def remove(i):
    global a
    a.remove(i)
    print a
    print
    print
def working():
    while True:
        arguement = q.get()
        remove(arguement)
        sleep(4)
        q.task_done()
for i in range(NUM):
    t = Thread(target=working)

    t.setDaemon(True)
    t.start()

print "aaaaaaaaaaa"
for i in a:
    q.put(i)
print q
q.join()
print "bbbbbbbbbbbbbbb"