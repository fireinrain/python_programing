#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang

import threading

class Mythread(threading.Thread):
    def __init__(self,my_id,count,mutex):
        threading.Thread.__init__(self)
        self.my_id=my_id
        self.count=count
        self.mutex=mutex

    def run(self):
        for i in range(self.count):
            with self.mutex:
                print('[%s]=>>>>%s' % (self.my_id, i))

stdoutmutex=threading.Lock()
threads=[]

for i in range(10):
    thread=Mythread(i,100,stdoutmutex)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print('main thread exiting')