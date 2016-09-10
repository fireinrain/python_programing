#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang

import sys,os,pprint
trace=False
if sys.platform.startswith('win'):
    dirname=r'C:\python3.4\Lib'
else:
    dirname=r'/usr/lib/python3.4'

allsize=[]
for (this_dir,sub_here,file_here) in os.walk(dirname):
    if trace:print(this_dir)
    for filename in file_here:
        if filename.endswith('.py'):
            fullname=os.path.join(this_dir,filename)
            fullsize=os.path.getsize(fullname)
            allsize.append((fullsize,fullname))

allsize.sort()
pprint.pprint(allsize[:2])
pprint.pprint(allsize[-2:])
