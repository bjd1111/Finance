"""
import difflib

f = open('delta.txt','r')
data  = f.readlines()
l1 = []
l2 = []

    

for line in data:
     
     l1.append(line[:53])
     l2.append(line[56:-1])

print l1



def splitdiff(a, b):
     seq = difflib.SequenceMatcher(None, a, b)
     result1 = result2 = result3 = ""
     for tag, i1, i2, j1, j2 in seq.get_opcodes():
         if tag == 'equal':
             result1 += "".join(a[i1:i2])
         if tag == 'delete':
             result2 += "".join(a[i1:i2])
         if tag == 'insert':
             result3 += "".join(b[j1:j2])
         if tag == 'replace':
             result2 += "".join(a[i1:i2])
             result3 += "".join(b[j1:j2])
     return result1, result2, result3





"""


import urllib, gzip, Image, difflib, time
from cStringIO import StringIO
url = 'http://huge:file@www.pythonchallenge.com/pc/return/deltas.gz'
data = urllib.urlopen(url).read()
l1 = []
l2 = []
for line in gzip.GzipFile(fileobj=StringIO(data)):
     
     l1.append(line[:53])
     l2.append(line[56:-1])



result = list(difflib.ndiff(l1, l2))


def solve(condition):
     s = [chr(int(group, 16))
          for line in result if line.startswith(condition)
          for group in line[len(condition):].split()]
     Image.open(StringIO("".join(s))).show()


for condition in " +-":
     solve(condition)
     time.sleep(1)  # give time to view

