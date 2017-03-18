__author__ = 'apple'
a= [2,3,4,5]

try:
    for i in xrange(3):
        if i in a:
            print "testing",i
            print 111111111
        else:
            break
except StandardError, e:
    print e


print "f"