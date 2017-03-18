# -*- coding: utf-8 -*-
import urllib
import urllib2
postdata=urllib.urlencode({
 'username':'bjd1111',
 'password':'9878522',
 'continueURI':'http://www.verycd.com/',
 'fk':'',
 'login_submit':'登录'
})
req = urllib2.Request(
 url = 'http://secure.verycd.com/signin',
 data = postdata
)
result = urllib2.urlopen(req)
print result.read() 





# -*- coding: utf-8 -*-
import urllib
url = 'http://www.verycd.com/'

a = urllib.urlopen(url)
print a.read()

