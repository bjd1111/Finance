
import urllib

import pickle


url = 'http://www.pythonchallenge.com/pc/def/banner.p'

a = urllib.urlopen(url)
content = a.read()
c = pickle.loads(content)

for i in c:
    a = ''
    for j in i:
        a += j[0]*j[1]
    print a
    
        
    
    
