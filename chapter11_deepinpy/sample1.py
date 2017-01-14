#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com


# 关于运算符
# 只要对象实现了特殊方法__add__,就可以使用+，
# 对两个对象实现既定的（在方法—__add__实现的操作）
# print('abc'+'xyz')
# print('abc'.__add__('xyz'))


# 同理可以实现乘法
# print(1.8*2.0)
# print((1.8).__mul__(2.0))

# print(True.__or__(False))
#
# class Pig:
#     def __init__(self,name):
#         self.name = name
#
#     def __or__(self, other):
#         print(self.name+other.name)
#
#
# pig1 = Pig("xiaoqian")
# pig2 = Pig("mayuyu")
# print((pig1).__or__(pig2))


# 关于内置函数

