#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang

import threading


def child(tid):
    print('hello from thread',tid)

def parent():
    i=0
    while True:
        i+=1
        threading._start_new_thread(child,(i,))
        print('parent.....')
        if input()=='q':break
if __name__=='__main__':
    parent()