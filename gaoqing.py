#爬取高清电影网
#coding=utf-8
import string
import urllib.request
import re

class spider:
    def __init__(self):
        pass
    def getpage(self,page):
        while page<2:
            url = "http://gaoqing.la/bluray/page/" + str(page)
            data = urllib.request.urlopen(url).read()
            cotent = data.decode("utf-8")
            items = re.findall('<div.*?class="article">.*?<h2>.*?<a.*?href="(.*?)".*?>(.*?)</a>.*?</h2>.*?<div.*?class=".*?">.*?</div>.*?</div>',cotent,re.S)
            for item in items:
                print (item[0],item[1])
            page = page + 1
    
myspider = spider()
myspider.getpage(1)