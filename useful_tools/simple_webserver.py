#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com

import socket
# *导入套接字库

# *定义端口和自己ip地址
HOST,PORT='',8000

listen_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
listen_socket.bind((HOST,PORT))
listen_socket.listen(1)

print('servering http on port {}'.format(PORT))
while True:
    client_connectin,client_address=listen_socket.accept()
    # 如果accept()没有被激活的话，即客户端没发起请求，则被blocking
    # client_connection 其实是处理面对客户端的对象
    # 建立了tcp链接才能发送请求
    # 这里client_connection 实现了tcp链接
    request=client_connectin.recv(1024)
    # 接受客户端的请求
    print(request)

    http_response=b"""\
    HTTP/1.1 200 OK

    HEllo liu zhaoyang"""
    client_connectin.sendall(http_response)
    client_connectin.close()