#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com
import os
import re
import urllib.request
from bs4 import BeautifulSoup

url = 'http://www.math.pku.edu.cn/teachers/qiuzy/ds_python/courseware/index.htm'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser', from_encoding = 'utf-8')
#nodes = soup.find_all('td', {'align':'left'})
nodes_tr = soup.find_all('tr')
nodes = []
for node in nodes_tr:
    try:
        nodes.append((node.find_all('td', align = "left")[0]))
    except:
        pass
urls = {}
url_head = 'http://www.math.pku.edu.cn/teachers/qiuzy/ds_python/courseware/'
code_subs = {}

for node in nodes:
    key = (node.get_text().split('，'))[0]
    value = node.find_all('a',href = re.compile("(.*)\.[(py)(pdf)]"))
    urls[key] = value
    for i in node.get_text().split('，'):
        a = i.find('代码文件')
        if  a != -1:
            code_subs[key] = i[0:a]

os.mkdir('裘宗燕python')
os.chdir('裘宗燕python')

from multiprocessing.dummy import Pool, freeze_support
func = urllib.request.urlretrieve

with Pool(4) as pool:
    for key in urls:
        try:
            os.mkdir(key)
        except:
            pass
        os.chdir(key)
        a = urls[key]
        toCrawl = []
        for i in a:
            url_temp = i.attrs['href']
            text_temp = i.getText()
            if text_temp == '代码文件':
                text_temp = code_subs[key]
            toCrawl.append((url_head + url_temp, url_temp))
            with open('%s.txt' % text_temp, 'w') as f:
                f.write(str(i))
                print('%s' % text_temp, 'is done!')
        pool.starmap(func, toCrawl)
        os.chdir('..')