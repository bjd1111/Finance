import md5
broken = open('maze/mybroken.zip').read()
for i in range(len(broken)):
     for j in range(256):
         repaired = broken[:i] + chr(j) + broken[i+1:]
         if md5.md5(repaired).hexdigest() == 'bbb8b499a0eef99b52c7f13f4e78c24b':
             open('unbroken.zip','wb').write(repaired)
             print i, j
             raise StopIteration
