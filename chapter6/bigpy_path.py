#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang

import os,sys,pprint
trace=0 #1代表目录，2代表文件

visited={}
allsize=[]

for src_dir in sys.path:
    for(this_dir,sub_here,file_here) in os.walk(src_dir):
        if trace>0:print(this_dir)
        this_dir=os.path.normpath(this_dir)
        fixcase=os.path.normcase(this_dir)
        print('******'+str(trace))
        if fixcase in visited:
            continue
        else:
            visited[fixcase]=True
        for filename in file_here:
            if filename.endswith('.py'):
                if trace>1:print('...',filename)
                print('******' + str(trace))
                pypath=os.path.join(this_dir,filename)
                try:
                    pysize=os.path.getsize(pypath)
                except os.error:
                    print('skipping',pypath,sys.exc_info()[0])
                else:
                    pylines=len(open(pypath,'rb').readlines())
                    allsize.append((pysize, pylines, pypath))

print('by size....')
allsize.sort()
pprint.pprint(allsize[:3])
pprint.pprint((allsize[-3:]))

print('by lines...')
allsize.sort(key=lambda x:x[1])
pprint.pprint(allsize[:3])
pprint.pprint(allsize[-3:])