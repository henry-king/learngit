#��ȡecho����
import  urllib.request 
import urllib.parse 
import  http.cookiejar
import re
import os
import time
import random
import socket
ISOTIMEFORMAT='%Y-%m-%d %X'
def login(q):
    x = q
    values={ 
            'login_form[name]':'13220307585', 
            'login_form[password]':'newlife!' 
    } 
    logUrl="http://www.app-echo.com/index/login" 
    cook=http.cookiejar.CookieJar() 
    openner=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cook)) 
    openner.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36')] 
    r=openner.open(logUrl,urllib.parse.urlencode(values).encode()) 

    
    url = "http://www.app-echo.com/channel/1091?page=" + str(q)
    a = openner.open(url)
    data = a.read()
    a.close()
    data = data.decode("utf-8")
    redata = re.findall('<h3 class="voice-name"><a href="(.*?)">(.*?)</a></h3>',data,re.S)
    print ("��%dҳ����ɹ�\n" % q)
    n = []
    m = []
    for x in redata:
    #������ӵ�ַ�����б�
        n.append(x[0])
    #����������ֽ����б�
        m.append(x[1])
    s = zip(n,m)
    print ("�Ѿ����%d��ҳ���������ӵ�ַ" % q)
    return s
os.chdir("D:\\3D")
os.getcwd()
def download(s):
    w = 0
    for b,d in s:
    #ѭ�����ӣ���ÿ������ҳ��

        try:
            w = w + 1
            soundurl = "http://www.app-echo.com" + str(b)
            c = urllib.request.urlopen(soundurl,timeout = 10)
            datas = c.read()
            c.close()
            print ("��%d�����Ӷ������" % w)
            datas = datas.decode("utf-8")
            redatas = re.findall('play_source\("\d+".*?, "(http://.*?)"\);',datas,re.S)
            redatas = ''.join(redatas)
            funny = urllib.request.urlopen(redatas).read()
            try:
                f = open(d,'wb')
                f.write(funny)
                f.close
                print ("%sд�����\n" % d)
            except OSError:
                f = open("1.txt",'w+')
                f.write(time.strftime(ISOTIMEFORMAT))      
                f.write("   ������һ�����󣬸��ļ���ӦΪ��")
                f.write(d)
                f.write("\n\n")
                f.close
                print ("����������д�������־")
        except TimeoutError:
            print ("��ʱ���Ѿ�������")
        except socket.timeout:
            print ("��ʱ���Ѵ�����")
        except urllib.error.HTTPError:
            print ("403�����Ѵ���")
        except:
            print ("����δ֪����")
            

            
        time.sleep(1)
    print ("д�����")

page = 0
while page<433:
    page = page + 1
    download(login(page))
    t = random.randint(2,3)
    time.sleep(t)

