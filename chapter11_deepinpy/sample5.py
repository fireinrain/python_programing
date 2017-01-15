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

# def print_para(func):
#     def pp_f(a,b):
#         a = a**2
#         b = b**2
#         print("input:", a, b)
#         return func(a,b)
#     return pp_f
#
# @print_para
# def square_sum(a,b):
#     return a**2+b**2
#
# @print_para
# def square_diff(a,b):
#     return a**2-b**2
#
# print(square_diff(3,4))
# print(square_sum(3,4))
# 相当于这样
# square_sum = decorator(square_sum)
# square_sum(3, 4)

##############################含参数的装饰器
# def pre_str(pre=""):
#     #this is  a derector
#     def decorator(Func):
#         def new_func(a,b):
#             print(pre+"input:",a,b)
#             return Func(a,b)
#         return new_func
#     return decorator
#
# @pre_str('^_^')
# def square_sum(a,b):
#     return a**2+b**2
# @pre_str('^_^')
# def square_diff(a,b):
#     return a**2-b**2
# print(square_diff(3,4))
# print(square_sum(3,4))
# # 相当于这样调用
# square_sum = pre_str('^_^') (square_sum)


#################################装饰类
# 一个装饰器可以接收一个类，并返回一个类，从而起到加工类的效果
def decorator(aClass):
    class newClass:
        def __init__(self,age):
            self.total_display = 0
            self.wrapped = aClass(age)
        def display(self):
            self.total_display += 1
            print("total display:",self.total_display)
            self.wrapped.display()
    return newClass

@decorator
class Bird:
    def __init__(self,age):
        self.age = age
    def display(self):
        print("My age is",self.age)

my_bird = Bird(5)
for i in range(3):
    my_bird.display()

# 装饰器的核心作用是name binding