import re
import urllib2
import urllib



def get_herf():
    address = []
    for page in xrange(50,100):
        try:

            url = "http://www.meizitu.com/a/list_1_%d.html" %page
            request = urllib2.Request(url)
            respond = urllib2.urlopen(request)
            content = respond.read()
            pattern = re.compile('<p><a href="(.*?)"  target=.*?><img.*?src.*?style.*?/></a></p>',re.S)
            #print content
            result = re.findall(pattern,content)
            #print result
            for item in result:
               address.append(item)
        except urllib2.URLError, e:
                print e
                pass
        except StandardError, e:
                print e
                pass
    return address



def get_imgurl():
    url_add = get_herf()


    
    print "total:", len(url_add),"category"

    for url in url_add:
            try:
                num_cat = int(url_add.index(url)+1)

                print "saving category:", num_cat

                request = urllib2.Request(url)
                respond = urllib2.urlopen(request,timeout=5)
                content = respond.read().decode("gbk")


                pattern = re.compile('<img.*?alt=".*?" src="(.*?)" /><br />',re.S)
                result = re.findall(pattern,content)


                for item in result:

                    number = int(result.index(item))+1

                    save(str(item),num_cat,number)
                print "finished all saving, total", len(result), "pictures"
            except urllib2.URLError, e:
                print e
                pass
            except StandardError, e:
                print e
                pass


 
def save(imageURL,num_cat,number):




    filename = str(num_cat)+"_"+str(number)+".jpg"


    urllib.urlretrieve(imageURL,filename)


    print "finished saving picture:", num_cat, number
   
get_imgurl()