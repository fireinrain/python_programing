#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
from tkinter import *
import sys

name=input('sssssss')
def hello(name):
    print('你好，刘朝阳'+name)
    sys.exit()
root=Tk()
widget=Label(root)

widget.config(text='hello ,gui python')
widget.pack(side=TOP,expand=YES,fill=BOTH)

btt=Button(root,command=(lambda :print('再见') or sys.exit()))
btt.config(text='点击')
btt.pack(side=RIGHT,expand=YES,fill=X)

btt2=Button(root,command=hello)
btt2.pack(side=LEFT,expand=YES,fill=X)
root.title('我是一个标题')
root.mainloop()