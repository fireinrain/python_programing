#!/usr/bin/env python3
#coding:utf-8
# 用oswalk完成目录树的列举
import os,sys

def lister(root):#对于根目录
    for(this_dir,subshere,fileshere) in os.walk(root):
        print('['+this_dir+']')
        for fname in fileshere:
            path=os.path.join(this_dir,fname)
            print('---'+path)
if __name__=='__main__':
    lister(sys.argv[1])