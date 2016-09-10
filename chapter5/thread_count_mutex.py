#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang

import time,threading

def counter(my_id,count):
    for i in range(count):
        time.sleep(2)
        mutex.acquire()
        print('[%s]=>>>>%s===>>%s' % (my_id, i,time.time()))
        mutex.release()

mutex=threading._allocate_lock()
for i in range(5):
    threading._start_new_thread(counter,(i,5))
time.sleep(6)
print('main thread exiting')