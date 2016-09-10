#!/usr/bin/env python3
#coding:utf-8
#written by:liuzhaoyang

import sys,os
def mylister(currdir):
    print('当前目录：'+currdir)
    for file in os.listdir(currdir):
        path=os.path.join(currdir,file)
        if not os.path.isdir(path):
            print(path)
        else:
            mylister(path)
if __name__=='__main__':
    mylister(sys.argv[1])
