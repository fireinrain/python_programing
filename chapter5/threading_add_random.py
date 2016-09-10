#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang
import threading, time
count = 0
def adder():
    global count
    count = count + 1
    time.sleep(0.5)
    count = count + 1
# update a shared name in global scope
# threads share object memory and global names
threads = []
for i in range(100):
    thread = threading.Thread(target=adder, args=())
    thread.start()
    threads.append(thread)
for thread in threads: thread.join()
print(count)