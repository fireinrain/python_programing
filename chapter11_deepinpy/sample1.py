#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com
# 本代码片段主要描述关于python的特殊方法和多范式


############################ 关于运算符
# 只要对象实现了特殊方法__add__,就可以使用+，
# 对两个对象实现既定的（在方法—__add__实现的操作）
# print('abc'+'xyz')
# print('abc'.__add__('xyz'))


######################## 同理可以实现乘法
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


######################## 关于内置函数
# print(len([1,2,5,8,7]))
# print([1,2,5,8,7].__len__())

# print((-1).__abs__())
# print(abs(-1))

# print((2.3).__int__())
# print(int(2.3))


########################列表元素的引用
# li = [1,2,8,9,7,6]
# print(li[3])
# print(li.__getitem__(3))
# # print(li.__setitem__(3,0))
# li[3]=0
# print(li)

# dics = {'a':1,'b':2}
# {'a':1,'b':2}.__delitem__('a')
# dics.pop('a')
# print(dics)


########################函数
# 类只要实现了call方法，就可以像内置函数一样，可以调用
# 传入的参数，将会传给call作为参数
# class SampleMore:
#     def __call__(self,a):
#         return a + 5
# add = SampleMore()
# print(add(2))
# print([i for i in map(add,[2,5,6])])

