#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com

# import socket
#
# SERVER_ADDRESS=(HOST,PORT)='',8888
# REQUEST_QUEN_SIZE=5
#
# def handle_request(client_connection):
#     request=client_connection.recv(1024)
#     print(request.decode())
#     http_response=b"""\
#     HTTP/1.1 200 OK
#
#     Hello, World!
#     """
#     client_connection.sendall(http_response)
#
#
# def server_forever():
#     listen_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     listen_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#     listen_socket.bind(SERVER_ADDRESS)
#     listen_socket.listen(REQUEST_QUEN_SIZE)
#     print("SERVing http on port {port}".format(port=PORT))
#
#     while True:
#         client_connection,client_address=listen_socket.accept()
#         handle_request(client_connection)
#         client_connection.close()
#
# if __name__=="__main__":
#     server_forever()
##################################################v2 使用sleep阻塞额外请求#####################################################

# import socket
# import time
#
# SERVER_ADDRESS=(HOST,PORT)='',8888
# REQUEST_QUEN_SIZE=5
#
# def handle_request(client_connection):
#     request=client_connection.recv(1024)
#     print(request.decode())
#     http_response=b"""\
#     HTTP/1.1 200 OK
#
#     Hello, World!
#     """
#     client_connection.sendall(http_response)
#     time.sleep(60)  #主动阻塞处理
#
#
# def server_forever():
#     listen_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     listen_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#     listen_socket.bind(SERVER_ADDRESS)
#     listen_socket.listen(REQUEST_QUEN_SIZE)
#     print("SERVing http on port {port}".format(port=PORT))
#
#     while True:
#         client_connection,client_address=listen_socket.accept()
#         handle_request(client_connection)
#         client_connection.close()
#
# if __name__=="__main__":
#     server_forever()


#####################处理多个请求##############

# import socket
# import time
# import os
# #在win下不能实现进程。。
#
# SERVER_ADDRESS=(HOST,PORT)='',8888
# REQUEST_QUEN_SIZE=5
#
# def handle_request(client_connection):
#     request=client_connection.recv(1024)
#     print("child pid:{pid} parent pid{ppid}".format(pid=os.getpid(),ppid=os.getppid()))
#     print(request.decode())
#     http_response=b"""\
#     HTTP/1.1 200 OK
#
#     Hello, World!
#     """
#     client_connection.sendall(http_response)
#     time.sleep(60)  #主动阻塞处理
#
#
# def server_forever():
#     listen_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     listen_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#     listen_socket.bind(SERVER_ADDRESS)
#     listen_socket.listen(REQUEST_QUEN_SIZE)
#     print("SERVing http on port {port}".format(port=PORT))
#
#     while True:
#         client_connection,client_address=listen_socket.accept()
#         pid=os.fork()
#         if pid==0:
#             listen_socket.close()
#             handle_request(client_connection)
#             client_connection.close()
#             os._exit(0)
#         else:
#
#             client_connection.close()
#
# if __name__=="__main__":
#     server_forever()