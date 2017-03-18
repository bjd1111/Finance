"""

import urllib
template = "http://butter:fly@www.pythonchallenge.com/pc/hex/lake%i.wav"
for i in range(1, 26):
    urllib.urlretrieve(template % i)
    
import wave
lake1 = wave.open('lake1.wav','r')
print lake1.getnframes()
#10800
print lake1.getsampwidth()
# 1

import Image
for i in range(1, 26):
   Image.fromstring("RGB", (60, 60),
                    wave.open("lake%i.wav"%i).readframes(10800)).show()
"""




import urllib, wave, Image
from cStringIO import StringIO
canvas = Image.new('RGB', (300, 300))
url = "http://butter:fly@www.pythonchallenge.com/pc/hex/lake%i.wav"
for i in range(25):
     wav = wave.open(StringIO(urllib.urlopen(url % (i + 1)).read()))
     piece = Image.fromstring('RGB', (60, 60), wav.readframes(10800))
     canvas.paste(piece, ((i % 5) * 60, (i / 5) * 60))
canvas.show()




"""

im = Image.new("RGB", (300, 300))
for y in range(5):
    for x in range(5):
        im.paste(Image.fromstring("RGB", (60, 60), pieces.pop(0)),
                 (60*x, 60*y))
im.show()
"""

