#��ȡ������Ů
#coding=utf-8
import re
import urllib.request
import string
import os

def getpage():
    page = 1
    os.chdir("D:\\downloads")
    os.getcwd()
    while page<14:
        url = "http://www.51ztzj.com/tag/339_ + str(page).html"
        headers = {'User-Agent','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36'}
        opener = urllib.request.build_opener()
        opener.addheaders = [headers]
        data = opener.open(url).read()
        content = data.decode("utf-8")
        datas = re.findall('<img.*?class="height_min".*?title="(.*?)".*?src="(.*?)".*?>',content,re.S)
        for x in datas:
            try:
                url = x[1]
                name = x[0] + '.jpg'
                data = urllib.request.urlopen(url).read()
                f = open(name,'wb')
                f.write(data)
                f.close
                print (x[0] + "     �Ѿ�����")
            except OSError:
                print ("�������쳣�����Ǽ���ִ����ȥ")    
        print ("��%dҳд�����" % page)
        page = page + 1
    print ("д����ɣ�")
        
        
getpage()