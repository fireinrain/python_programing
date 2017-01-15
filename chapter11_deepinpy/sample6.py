#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com
# 本代码片段主要描述python的内存管理
# 参数的引用
# def f(x):
#     x = 100
#     print(x)
#
# a = 1
# f(a)
# print(a)

# def f(x):
#     x[0] = 100
#     print(x)
#
# a = [1,2,3]
# f(a)
# print(a)

a = 1
print(id(a))
print(hex(id(a)))  #将整数变成16进制
# 在Python中，整数和短小的字符，Python都会缓存这些对象，以便重复使用
