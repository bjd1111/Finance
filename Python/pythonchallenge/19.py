import urllib
import re
import email
import wave



url = 'http://butter:fly@www.pythonchallenge.com/pc/hex/bin.html'
src = urllib.urlopen(url).read()
c = re.compile("<!--\n(.*)\n-->", re.DOTALL)
data = c.findall(src)[0]

message = email.message_from_string(data)
audio = message.get_payload(0).get_payload(decode=True)




f=open('19.wav','w')
f.write(audio)
f.close()

a = wave.open('19.wav','r')
reverse = wave.open('reversed.wav', 'wb')
reverse.setparams(a.getparams())
for i in range(a.getnframes()):
    reverse.writeframes(a.readframes(1)[::-1])
reverse.close()

