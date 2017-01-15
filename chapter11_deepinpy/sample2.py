#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com
# 本代码片段主要描述python的上下文管理器


###################关闭文件
# f = open('new.txt',"w")
# print(f.closed)
# f.write("hello,world")
# f.close()
# print(f.closed)

# with open("new.txt","w") as f:
#     print(f.closed)
#     f.write("hello,liuzhaoyang")
# print(f.closed)


####################自定义上下文管理器
# 任何定义了__enter__()和__exit__()方法的对象都可以用于上下文管理器
# 即使用with来使用

class Say:
    def __init__(self,text):
        self.text = text
    def __enter__(self):
        self.text = "I say:"+self.text
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.text = self.text+"love mayuyu"

with Say("liuzhaoyang") as say:
    print(say.text)
print(say.text)