import bz2
import zlib
f = open('20/package.pack','r')
data = f.read()
#print data
def unwrap(data):
     result = ""
     while True:
         if data.startswith('x\x9c'):
             data = zlib.decompress(data)
             result += ' '
         elif data.startswith('BZh'):
             data = bz2.decompress(data)
             result += '#'
         elif data.endswith('\x9cx'):
             data = data[::-1]
             result += '\n'
         else:
             return result


print unwrap(data)
f.close()
