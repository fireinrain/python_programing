#!/usr/bin/env python3
#coding:utf-8
#written by:liuzhaoyang

import os
def child():
    print('hello from child',os.getpid())
    os._exit(0)
def parent():
    while True:
        newpid=os.fork()
        print(newpid)
        if newpid==0:
            child()
        else:
            print('hello from parent',os.getpid(),str(newpid)+'***')
        if input()=='q':break

parent()



# import os
# import time

# # 创建子进程之前声明的变量
# source = 10
#
# try:
#     pid = os.fork()
#
#     if pid == 0:  # 子进程
#         print("this is child process.")
#         # 在子进程中source自减1
#         source = source - 1
#         time.sleep(3)
#     else:  # 父进程
#         print("this is parent process.")
#
#     print(source)
#
# except OSError as e:
#     pass