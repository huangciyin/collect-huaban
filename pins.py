#coding=utf-8
import urllib2, urllib, cookielib, re, sys

def getPin():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    print 'logining'
    args = sys.argv
    keyWord = args[1]
    print keyWord
    page = args[2]
    print page
    keyWord = keyWord.encode('utf8')
    for j in range(0, int(page)):
        url = 'http://huaban.com/search/?q=' + keyWord +'&page=' + str(j) + '&per_page=20&wfl=1'
        print url
        res = urllib.urlopen(url).read()
        r = 'key":"(.*?)",'
        imgs = re.findall(r, res);
        for i in imgs:
            imgUrl = 'http://img.hb.aicdn.com/' + i + '_fw554'
            print imgUrl
            file('./%s.jpeg' % i, 'wb').write(
                    urllib.urlopen(imgUrl).read())

getPin()
