#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang

"""
找到任意目录树下所有给定类型的文件中的最大的一个
避免重复路径，捕获错误，添加最终和行数大小
同样使用集合，文件迭代起和生成器避免装载整个文件
并试图绕过不可解的目录或文件
"""

import os,pprint
from  sys  import argv,exc_info

trace=1#0代表关闭，1代表目录，2代表文件
dirname,extname=r'/usr/lib/python3.4','.py'
print(os.curdir)
if len(argv)>1:dirname=argv[1]
if len(argv)>2:extname=argv[2]
if len(argv)>3:trace=int(argv[3])

def tryprint(arg):
    try:
        print(arg)
    except UnicodeDecodeError:
        print(argv.encode())

visited=set()
allsize=[]

for(this_dir,sub_here,file_here) in os.walk(dirname):
    # if trace:print(this_dir)
    this_dir=os.path.normpath(this_dir)
    fixname=os.path.normcase(this_dir)
    # print('这是'+fixname)

    if fixname in visited:
        if trace:tryprint('skipping'+this_dir)

        else:
            visited.add(fixname)
            for filename in file_here:
                if filename.endswith(extname):
                    if trace>1:print('...'+filename)
                    fullname=os.path.join(this_dir,filename)
                    print('zheshi'+fullname)
                    try:
                        bytesize=os.path.getsize(fullname)
                        linesize=sum(+1 for line in open(fullname,'rb'))

                    except os.error as e:
                        print(e,exc_info()[0])
                    else:

                        allsize.append((bytesize, linesize, fullname))
print(visited)
for (title,key) in [('byte',0),('line',1)]:
    print('\nby %s...' % title)
    allsize.sort(key=lambda x:x[key])
    pprint.pprint(allsize[:3])
    pprint.pprint(allsize[-3:])



