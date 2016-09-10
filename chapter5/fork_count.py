#!/usr/bin/env python3
#coding:utf-8
#written by:liuzhaoyang

import os,time

def counter(count):
    for i in range(count):
        time.sleep(4)
        print('[%s] =>>> %s' % (os.getpid(),i))
for i in range(5):
    pid=os.fork()
    if pid !=0:
        print('process %d spawned' % pid)
    else:
        counter(5)
        os._exit(0)
print('main process exiting')