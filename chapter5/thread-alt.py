#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang

import threading,time


def action(i):
    print(i ** 8)


class Power:
    def __init__(self, i):
        self.i = i

    def action(self):
        print(self.i ** 8)

def parent():
    # 开启一个线程
    threading._start_new_thread(action, (3,))
    #j开启另一个线程
    threading._start_new_thread((lambda: action(2)), ())

    obj = Power(1)
    threading._start_new_thread(obj.action, ())

if __name__=='__main__':
    parent()
    time.sleep(20)
    print('byebye')