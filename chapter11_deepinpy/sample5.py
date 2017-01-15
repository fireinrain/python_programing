#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com
# 本代码片段主要描述python的装饰器
# 装饰器可以对一个函数、方法或者类进行加工。


#####################装饰函数和方法
# def square_sum(a,b):
#     return a**2+b**2
#
# def square_diff(a,b):
#     return a**2-b**2
#
# print(square_diff(3,4))
# print(square_sum(3,4))


# def square_sum(a,b):
#     print("input:",a,b)
#     return a**2+b**2
#
# def square_diff(a,b):
#     print("input:", a, b)
#     return a**2-b**2
#
# print(square_diff(3,4))
# print(square_sum(3,4))

def print_para(func):
    def pp_f(a,b):
        print("input:", a, b)
        return func(a,b)
    return pp_f

@print_para
def square_sum(a,b):
    return a**2+b**2

@print_para
def square_diff(a,b):
    return a**2-b**2

print(square_diff(3,4))
print(square_sum(3,4))