#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com
# 本代码片段主要描述python的对象的属性

###########################属性的__dict__系统
# class Bird:
#     feather = True
#
# class Chicken(Bird):
#     fly = False
#     def __init__(self,age):
#         self.age = age
#
# summer = Chicken(2)
# print(Bird.__dict__)
# print(Chicken.__dict__)
# print(summer.__dict__)
# # 修改属性
# summer.__dict__['age'] = 3
# print(summer.__dict__['age'])
#
# summer.age = 5
# print(summer.age)

###########################property 特性，特殊的属性
# class Bird:
#     feather = True
#
# class Chicken(Bird):
#     fly = False
#     def __init__(self,age):
#         self.age = age
#     def get_adult(self):
#         if self.age>1.0:return True
#         else:return False
#     adult = property(get_adult)
#
# summer = Chicken(2)
# print(summer.adult)
# summer.age =0.5
# print(summer.adult)

# class Num:
#     def __init__(self,value):
#         self.value = value
#
#     def getNeg(self):
#         return -self.value
#     def setNeg(self,value):
#         self.value = -value
#     def delNeg(self):
#         print("value will be del after now")
#         del self.value
#     neg = property(getNeg,setNeg,delNeg,"I'm negative")
#
# x = Num(11)
# print(x.neg)
# x.neg = -18
# print(x.neg)
# print(Num.neg.__doc__)
# del x.neg
# print(x.neg)


# ###########################使用特殊方法__getattr__
# 我们可以用__getattr__(self, name)来查询即时生成的属性。
# 当我们查询一个属性时，如果通过__dict__方法无法找到该属性，
# 那么Python会调用对象的__getattr__方法，来即时生成该属性。

# class Bird:
#     feather = True
#
# class Chicken(Bird):
#     fly = False
#     def __init__(self,age):
#         self.age = age
#     def __getattr__(self, name):
#         if name == "adult":
#             if self.age >1.0:return True
#             else:return False
#         else:raise AttributeError
#
# sumer = Chicken(5)
# print(sumer.adult)
############提醒####################
# (Python中还有一个__getattribute__特殊方法，用于查询任意属性。__getattr__只能用来查询不在__dict__系统中的属性)
# __setattr__(self, name, value)和__delattr__(self, name)可用于修改和删除属性。它们的应用面更广，可用于任意属性。



###################总结###############
# __dict__分层存储属性。每一层的__dict__只存储该层新增的属性。
# 子类不需要重复存储父类中的属性。
# 即时生成属性是值得了解的概念。
# 在Python开发中，你有可能使用这种方法来更合理的管理对象的属性。
