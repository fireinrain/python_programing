#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang

"""
找出单个目录下最大的python源文件
"""
import os,glob,sys

def find_big(dirname):
    if dirname==None:
        dirname=r'/usr/lib/python3.4'
    allsizes=[]
    allpy=glob.glob(dirname+os.sep+'*.py')
    for filename in allpy:
        filesize=os.path.getsize(filename)
        allsizes.append((filesize,filename))


    all_file_sort=sorted(allsizes)
    return all_file_sort

if __name__=='__main__':
    file=find_big(sys.argv[1])
    print(file[:2])
    print(file[-2:])
