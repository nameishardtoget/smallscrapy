#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
from lxml import html
import  requests,os
from bs4 import BeautifulSoup
def getPage(pageNum):
    r = requests.get(pageNum, headers)
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.content, "lxml")
    t1=soup.find_all('a')
    t=1
    for t2 in t1:

        t3=t2.get('href')

        if any(char.isdigit() for char in t3) and 'Index'not in t3:

            ss='http://365.sese365.cc'+t3
            print(ss)
            r = requests.get(ss, headers)
            print(r.status_code)
            r.encoding = r.apparent_encoding
            soup = BeautifulSoup(r.content, "lxml")
            if not os.path.exists("./" + 'beauty' + str(t)):
                os.mkdir("./" + 'beauty' + str(t))
            localpath = "./" + 'beauty' + str(t)
            t = t + 1
            n=0
            for link in soup.find_all('img'):


                d = link.get('src')
                if 'jpg' in d:
                    print(d)
                    html = requests.get(d)
                    with open(localpath + '/' + str(n) + '.jpg', 'wb') as file:
                        file.write(html.content)
                        file.close()
                        n += 1


headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
for q in range(4,5):
    if q==1:
        s='http://365.sese365.cc/a/ar/Index.html'
    else:
        s= 'http://365.sese365.cc/a/ar/Index_{}.html'.format(q)

    tt = getPage(s)

