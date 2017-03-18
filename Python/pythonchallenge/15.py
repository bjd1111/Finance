import calendar

tuesday = 1 #0-6 for mondayto sunday
for i in xrange(1006,2000):
    if calendar.isleap(i) and calendar.weekday(i,1,27)==tuesday:
        
        if str(i)[-1]=='6':
            print i
        
