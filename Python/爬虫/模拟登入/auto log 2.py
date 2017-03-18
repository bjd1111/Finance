
# -*- coding: utf-8 -*-
import urllib
import urllib2

"""

url = 'http://weibo.com'
cookie = 'SINAGLOBAL=5005052310880.273.1401617885121; _s_tentry=www.sina.com.cn; Apache=4605566626414.656.1430830844364; ULV=1430830844428:6:1:1:4605566626414.656.1430830844364:1429026108709; login_sid_t=ea2074663d1c42bc59743ebe79bab4c1; UOR=dota.uuu9.com,widget.weibo.com,login.sina.com.cn; un=472750273@qq.com; YF-Ugrow-G0=b02489d329584fca03ad6347fc915997; YF-V5-G0=82f55bdb504a04aef59e3e99f6aad4ca; YF-Page-G0=fc0a6021b784ae1aaff2d0aa4c9d1f17; myuid=2912712540; SUS=SID-2912712540-1430837075-GZ-x4htp-b64b2e67280493bcb1a0bb7365a7ca97; SUE=es%3Db611692f98742a35735117260be73b77%26ev%3Dv1%26es2%3D7e8c0173db184a23657fe93d2d62b2ac%26rs0%3Dmuj%252BJp%252Bn3b5x0MvSTdlzATgADJ%252BpAIo6PKBBoyZy%252FolW7%252BF8UIDKO3qEwWnaA3N2l00P5j%252BRjp8fCfaTXeTSiOijP%252FV2XE4HF59WUHtRr24qj%252FRXFQt1pRssCgFaiPvIbTZGpldup3Bz%252BRbj0nXeLLsI%252FPJ8lnlYzmgk3ThJ1mY%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1430837075%26et%3D1430923475%26d%3Dc909%26i%3Dca97%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D0%26st%3D0%26uid%3D2912712540%26name%3D472750273%2540qq.com%26nick%3Dbjd1111%26fmp%3D%26lcp%3D; SUB=_2A254TKcDDeTxGeRH6lAW8SzJzzyIHXVbO5_LrDV8PUNbuNBeLRXjkW9vrhjKE1k1OkvNmZP3BdnktJpflw..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhsD.6MOpkY4hoXmO1g-xFr5JpX5K2t; SUHB=0ft53KaXiTRcy9; ALF=1462373074; SSOLoginState=1430837075; un=472750273@qq.com; wvr=6'
headers = {'cookie': cookie}
req = urllib2.Request(url, headers=headers)  #每次访问页面都带上 headers参数
r = urllib2.urlopen(req)
print r.read()


"""




postdata=urllib.urlencode({
 'username':'wku0871486',
 'password':'9878522',

})
req = urllib2.Request(
 url = 'http://172.16.128.2/webAuth/index.htm?www.weibo.com/u/2912712540/home?wvr=5&lf=reg',
 data = postdata
)
result = urllib2.urlopen(req)
print result.read() 



