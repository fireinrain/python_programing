

# import requests
# import os
# from bs4 import BeautifulSoup
#
# user_agent='Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12'
# head = {'User-Agent': user_agent}
# url='http://docs.pythontab.com/tornado/introduction-to-tornado/index.html'
# req=requests.session().get(url).content
# with open('index.html','wb') as file:
#     file.write(req)
#
# print('下载完成')

import socket

# 创建一个socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 建立连接
s.connect(('202.108.33.107',80))
# 发送数据
s.send(b'GET /t HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# 接收数据
buffer=[]
while True:
    data=s.recv(1024)
    if data:
        buffer.append(data)
    else:
        break
data_needed=b''.join(buffer)
print(data_needed)
s.close()
# 分离http头部和网页主体
header,html=data_needed.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))

# 写入文件
with open('index.html','wb') as file:
    file.write(html)
print('下载完成')
