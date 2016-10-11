# from time import ctime
# from socket import *
#
# HOST='127.0.0.1'
# PORT=21567
# BUFSIZE=1024
# ADDR=(HOST,PORT)
#
# tcp_cli_sock=socket(AF_INET,SOCK_STREAM)
# tcp_cli_sock.connect(ADDR)
#
# while True:
#     data=input('>>>:')
#     if not data:
#         break
#     tcp_cli_sock.send(str.encode(data))
#     data=tcp_cli_sock.recv(BUFSIZE)
#     if not data:
#         break
#     print(data)
# tcp_cli_sock.close()

#!/usr/bin/python3
# 文件名：client.py
#
# # 导入 socket、sys 模块
# import socket
# import sys
#
# # 创建 socket 对象
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # 获取本地主机名
# host = socket.gethostname()
#
# # 设置端口好
# port = 9999
#
# # 连接服务，指定主机和端口
# s.connect((host, port))
#
# # 接收小于 1024 字节的数据
# msg = s.recv(1024)
#
# s.close()
#
# print (msg.decode('utf-8'))







# # 导入socket库
# from socket import *
#
# # 创建一个套嵌字
# client_socket=socket(AF_INET,SOCK_STREAM)
#
# # 建立连接
# client_socket.connect(('www.sina.com.cn',80))
#
# # 发送数据
# client_socket.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
#
# # 接收数据
# buffer=[]
# while True:
#     # 每次最多接受1k数据
#     data_raw=client_socket.recv(1024)
#     if data_raw:
#         buffer.append(data_raw)
#     else:
#         break
# data=b''.join(buffer)
# client_socket.close()
# # print(data.decode('utf-8'))
#
# # 分离返回的数据
# header=data.split(b'\r\n\r\n',1)[0]
# html=data.split(b'\r\n\r\n',1)[1]
# print(header.decode('utf-8'))
#
# # 把数据写入文件
# with open('sina_back.html','wb') as file:
#     file.write(html)

# # 服务器
# from socket import *
# import threading
# import time
#
# # 创建一个套嵌字
# server_socket=socket(AF_INET,SOCK_STREAM)
# # 绑定端口和主机名
# server_socket.bind(('127.0.0.1',8888))
# # 监听端口,指定最多可以同时连接数
# server_socket.listen(5)
# print('waiting for connection')
#
# def tcplink(sock,addr):
#     print('accept new connection from $s:$s...' % addr)
#     sock.send(b'welcom liuzhaoyang')
#     while True:
#         data=sock.recv(1024)
#         time.sleep(1)
#         if not data or data.decode('utf-8')=='exit':
#             break
#         sock.send(('hello,%s!'% data).encode('utf-8'))
#     sock.close()
#     print('connection from :%s closed'% addr)
# arr=[]
# while True:
#     #接受一个新连接
#     sock,addr=server_socket.accept()
#
#     # #创建新的线程来处理tcp链接
#     # t_process=threading.Thread(target=tcplink,args=(sock,addr))
#     data=sock.recv(1024)
#     arr.append(data)
#     print(arr)
#
# with open('word.txt','wb') as f:
#     f.write(arr)
#
#
# #!/usr/bin/python
# # -*- coding: utf-8 -*-
#
# import socket
#
# host = '127.0.0.1'
# port = 23456
# bufsiz = 1024
# ADDR = (host,port)
#
# tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# tcpCliSock.connect(ADDR)
#
# while True:
#     data = input('> ')
#     if not data:
#         break
#     tcpCliSock.send(data.encode('utf-8'))
#     data = tcpCliSock.recv(bufsiz)
#     if not data:
#         break
#     print(data)
#
# tcpCliSock.close()



