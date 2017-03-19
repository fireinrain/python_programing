#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com

import os
import requests
import re
from bs4 import BeautifulSoup
import lxml

url1 = "http://211.97.73.55/file3.data.weipan.cn/49040620/4972137bacaadd6eb3d6e6a808aea14dce404a12?ip=1489892614,171.36.0.238&ssig=xfO22WZQs9&Expires=1489893214&KID=sae,l30zoo1wmz&fn=%E5%90%8D%E5%AE%B6%E5%8D%81.pdf&skiprd=2&se_ip_debug=171.36.0.238&corp=2&from=1221134&wsiphost=local"
url2 = "http://211.97.76.41/file3.data.weipan.cn/49040620/e12a1288a69b90c1a2486dceee87bea4c09db30d?ip=1489892739,171.36.0.238&ssig=AwReErfDBI&Expires=1489893339&KID=sae,l30zoo1wmz&fn=%E5%A4%A7%E4%B8%AD%E5%9B%BD%E5%BF%97%E3%80%90%E8%91%A1%E3%80%91%E6%9B%BE%E5%BE%B7%E6%98%AD.pdf&skiprd=2&se_ip_debug=171.36.0.238&corp=2&from=1221134&wsiphost=local"
sha_id = "4972137bacaadd6eb3d6e6a808aea14dce404a12"

url = "http://vdisk.weibo.com/s/uxrDcNlK9mB5Q?category_id=0&parents_ref=uxrDcNlK9mB5O"

# html = requests.get(url).text
with open("sina.html","r",encoding='utf-8') as file:
    html = file.read()

    repat = re.compile("\"url\":\"http:.+file3\.data\.weipan\.cn\.wscdns\.com")
    # re_pat = re.compile("\"url\":\"http://file3.data.weipan.cn.wscdns.com/978813/13eda429d40482761192841b334d9b525462c9da?ip=1489893992,171.36.0.238&ssig=Muji%2FI5DAI&Expires=1489894592&KID=sae,l30zoo1wmz&fn=%E6%B4%AA%E4%B8%9A----%E6%B8%85%E6%9C%9D%E5%BC%80%E5%9B%BD%E5%8F%B2%E3%80%90%E7%BE%8E%E3%80%91.pdf&skiprd=2&se_ip_debug=171.36.0.238&from=1221134\"")
    download_urls = re.findall(repat,html)
    download_url_str = download_urls[0]
    url_strs = download_url_str.split(",")

    # urls = re.findall(r"\"url\":\"http:.+file3\.data\.weipan\.cn\.wscdns\.com",download_url_str)
    # print(download_urls[0])
    for i in url_strs:
        print(i)

# 内容在js文件里面所以不用bs，直接用正则表达式
# bsobj = BeautifulSoup(html,"lxml")
# href_list = bsobj.findAll()
# for i in href_list:
#     print(i)