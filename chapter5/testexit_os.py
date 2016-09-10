#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang
def later():
    import os
    print('bye sys world')
    os._exit(99)
    print('never reached')

if __name__=='__main__':
    later()
