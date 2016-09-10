#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang

def later():
    import sys
    print('bye sys world')
    sys.exit(55)
    print('never reached')

if __name__=='__main__':
    try:
        later()
    except SystemExit:
        print('hehehh')