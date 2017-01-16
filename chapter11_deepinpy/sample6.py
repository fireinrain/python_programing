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

# a = 1
# print(id(a))
# print(hex(id(a)))  #将整数变成16进制
# 在Python中，整数和短小的字符，Python都会缓存这些对象，以便重复使用


# a = 1
# b = 1
# print(a is b)
#
# a = "good"
# b = "good"
# print(a is b)

# a = "very good morningvery good morning"
# b = "very good morningvery good morning"
# print(a is b)

# a = str("very good morningvery good morning")
# b = str("very good morningvery good morning")
# print(a is b)
# print(id(a),id(b))
#
#
# a = []
# b = []
# print(a is b)

# from sys import getrefcount
# a = [1,2,3]
# print(getrefcount(a))
# b = a
# print(getrefcount(b))
# 在Python中，每个对象都有存有指向该对象的引用总数，即引用计数(reference count)。
# 我们可以使用sys包中的getrefcount()，来查看某个对象的引用计数。
# 需要注意的是，当使用某个引用作为参数，传递给getrefcount()时，参数实际上创建了一个临时的引用。
# 因此，getrefcount()所得到的结果，会比期望的多1。


########################################对象引用对象
# Python的一个容器对象(container)，比如表、词典等，可以包含多个对象。
# 实际上，容器对象中包含的并不是元素对象本身，是指向各个元素对象的引用。
# class from_obj:
#     def __init__(self,to_obj):
#         self.to_obj = to_obj
#
# b = [1,2,3]
# a = from_obj(b)
# print(id(a.to_obj))
# print(id(b))

# 对象引用对象，是Python最基本的构成方式。
# 即使是a = 1这一赋值方式，实际上是让词典的一个键值"a"的元素引用整数对象1。
# 该词典对象用于记录所有的全局引用。该词典引用了整数对象1。
# 我们可以通过内置函数globals()来查看该词典。

# a = 1
# b = 2
# print(globals())

# from sys import getrefcount
#
# a = [1, 2, 3]
# print(getrefcount(a))
#
# b = [a, a]
# print(getrefcount(a))


#容器对象的引用可能构成很复杂的拓扑结构。
# 我们可以用objgraph包来绘制其引用关系
# import objgraph
# x = [1,2,3]
# y = [x,dict(key1=x)]
# z = [y,(x,y)]
# objgraph.show_refs([z],filename="ref_topo.png")


# 两个对象可能相互引用，从而构成所谓的引用环(reference cycle)。
# from sys import getrefcount
# a = []
# b = [a]
# a.append(b)
# print(getrefcount(a))
# 即使是一个对象，只需要自己引用自己，也能构成引用环。
# a = []
# a.append(a)
# print(getrefcount(a))

##################################引用减少
# 某个对象的引用计数可能减少。比如，可以使用del关键字删除某个引用
# from sys import getrefcount
# a = [1,2,3]
# b = a
# print(getrefcount(a))
# del a
# print(getrefcount(b))
#
# a = [1,2,3]
# del a[0]
# print(a)

# 如果某个引用指向对象A，当这个引用被重新定向到某个其他对象B时，对象A的引用计数减少
# from sys import getrefcount
# a = [1,2,3]
# b = a
# print(getrefcount(a))
# a = 1
# print(getrefcount(b))



#################################垃圾回收
# a = [1,2,3]
# del a
#
# import gc
# print(gc.get_threshold())

###############################分代回收
# Python同时采用了分代(generation)回收的策略。
# 这一策略的基本假设是，存活时间越久的对象，越不可能在后面的程序中变成垃圾。
# 我们的程序往往会产生大量的对象，许多对象很快产生和消失，但也有一些对象长期被使用。
# 出于信任和效率，对于这样一些“长寿”对象，我们相信它们的用处，所以减少在垃圾回收中扫描它们的频率。
# import gc
# gc.set_threshold(700, 10, 5)
# Python将所有的对象分为0，1，2三代。所有的新建对象都是0代对象。
# 当某一代对象经历过垃圾回收，依然存活，那么它就被归入下一代对象。垃圾回收启动时，一定会扫描所有的0代对象。
# 如果0代经过一定次数垃圾回收，那么就启动对0代和1代的扫描清理。
# 当1代也经历了一定次数的垃圾回收后，那么会启动对0，1，2，即对所有对象进行扫描。
# 这两个次数即上面get_threshold()返回的(700, 10, 10)返回的两个10。
# 也就是说，每10次0代垃圾回收，会配合1次1代的垃圾回收；而每10次1代的垃圾回收，才会有1次的2代垃圾回收。
# 同样可以用set_threshold()来调整，比如对2代对象进行更频繁的扫描。


###############################孤立的引用环
# 引用环的存在会给上面的垃圾回收机制带来很大的困难。
# 这些引用环可能构成无法使用，但引用计数不为0的一些对象
# from sys import getrefcount
# a = []
# b = [a]
# a.append(b)
# print(getrefcount(a))
#
# del a
# print(getrefcount(b))
# print(b[0])
# print(getrefcount(b[0]))
