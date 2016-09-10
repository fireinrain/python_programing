#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang
import threading,time

def counter(my_id,count):
    for i in range(count):
        time.sleep(2)
        print('[%s]=>>>>%s' % (my_id,i))

for i in range(5):
    threading._start_new_thread(counter,(i,5))
time.sleep(20)
print('main thread exiting')