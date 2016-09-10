#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang

import threading

stdoutlock=threading._allocate_lock()
exit_lock=[threading._allocate_lock() for i in range(10)]
i=0
def counter(my_id,count):
    for i in range(count):
        stdoutlock.acquire()

        print('[%s]=>>>>%s' % (my_id, i))
        i += 1
        stdoutlock.release()
    exit_lock[my_id].acquire()

for i in range(10):
    threading._start_new_thread(counter,(i,100))
for mutex in exit_lock:
    while not mutex.locked():pass
print('main threading exiting',i)