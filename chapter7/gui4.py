#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang

from tkinter import *
import sys
x=42
def handle(x,y):
    print(x)

def func():
    handle()
root=Tk()
btt=Button(root)
btt.config(text='点击')
btt.pack(side=RIGHT,expand=YES,fill=X)
