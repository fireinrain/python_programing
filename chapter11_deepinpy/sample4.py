#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com
# 本代码片段主要描述python的闭包


#############################函数对象的作用域
# def line_conf():
#     def line(x):
#         return 2*x+1
#     print(line(5))
#
# line_conf()
# print(line(5))   #无法访问，在全局作用域不可见

#############################闭包
# def line_conf():
#     def line(x):
#         return 2*x+1
#     return line
#
# my_line = line_conf()
# print(my_line(5))
# line()的定义中引用了外部的变量
# def line_conf():
#     b = 15
#     def line(x):
#         return 2*x+b
#     return line       # return a function object
#
# b = 5
# my_line = line_conf()
# print(my_line(5))

# def news():
#     b = 5
#     def line_conf():
#
#         def line(x):
#             return 2*x+b
#         return line
#     return line_conf
# my_line = news()
# print(my_line()(5))


# 一个函数和它的环境变量合在一起，就构成了一个闭包(closure)。
# 在Python中，所谓的闭包是一个包含有环境变量取值的函数对象。
# 环境变量取值被保存在函数对象的__closure__属性中
# def line_conf():
#     b = 15
#     c = 13
#     def line(x):
#         return 2*x+b+c
#     return line
# b = 30
# my_line = line_conf()
# print(my_line.__closure__)
# print(my_line.__closure__[0].cell_contents,my_line.__closure__[1].cell_contents)

# 有什么用？
# 闭包有效的减少了函数所需定义的参数数目

def line_conf(a,b):

    def line(x):
        return a*x+b
    return line

my_line = line_conf(1,1)
my_line2 = line_conf(2,5)
print(my_line(5),my_line2(3))