__author__ = 'apple'
import threading
import time, thread
from time import ctime
a = []

for i in xrange(1,10):
    a.append(i)
print "at the beginning,a is :", a


b = list(a)
b.append(-1)
b.sort()
print "b is ", b

def run():
    global a
    for i in b:
        try:

            print "check", i, ctime()
            if i in a:

                print "remove ", i, "now"
                a.remove(i)
                print
                print
                print "a is " , a
                print "b is ", b
                print
                print

            elif len(a) == 0:
                print "finished"
                exit()
            else:
                print  i , "is not in a "
                print "go to next"
                print
        except StandardError, e:
            print e

thread1 = threading.Thread(target=run)
thread2= threading.Thread(target=run)

thread1.start()

thread2.start()
