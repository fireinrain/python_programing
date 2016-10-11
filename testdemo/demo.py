# print(type(0.0+2j))
# <class 'complex'>
# 所有的标准对象均可用于布尔测试，同类型的对象之间可以比较大小，每个对象天生就具有true or false��?
# class N:
#     pass
# name=N()
# class A(N):
#     pass
#
# print(type(N))
# print(type(name))
# print(type(A))
# print(A.__name__)

# <class 'type'>
# <class '__main__.N'>

# age=1.0
# while True:
#     print(id(name))
# print(type(name))
# print(name is age)

# st=list('abcde')
# print(st)
# print(dir(print()))
#
# a=10.0
# b=10.0
# print(type(a)==type(b))
# print(type(a) is type(b))
# Python中的对象包含三要素：id、type、value
# 其中id用来唯一标识一个对象，type标识对象的类型，value是对象的��?
# is判断的是a对象是否就是b对象，是通过id来判断的
# ==判断的是a对象的值是否和b对象的值相等，是通过value来判断的
# 如下代码或许可以帮助你理解���?1?7?
# >>> a = 1
# >>> b = 1.0
# >>> a is b
# False
# >>> a == b
# True
# >>> id(a)
# 12777000
# > )
# 12777000
# >> id(b)
# 14986000
# >>> a = 1
# >>> b = 1
# >>> a is b
# True
# >>> a == b
# True
# >>> id(a)
# 12777000
# >>> id(b

# print(4**-1)
# print(1/2)
# print(int('12',10))
# print(complex(45.2))
# print(round(3.6))
# import math
# for each_dot in range(10):
#     print(round(math.pi,each_dot))

# print(oct(230948231))
# chr() ord(a)
# print(0.1)

# while True:
#     year = (input("请输入年份：(q退��?)"))
#     if year == "q":
#         break
#     else:
#         intyear = int(year)
#         if intyear % 4 == 0 and intyear % 100 != 0:
#             print("这是闰年")
#         elif intyear % 4 == 0 and intyear % 100 == 0:
#             print("闰年")
#         elif year == "q":
#             break
#         else:
#             print("不是闰年")

# money=float(input("请输入一美元一下的数字:(两位小数)"))
# total=money*100
# arr=[]
#
# cont=divmod(total,25)
# cont2=divmod(cont[1],10)
# cont3=divmod(cont2[1],5)
# cont4=divmod(cont3[1],1)
# print(cont[0])
# arr.append(cont[0])
# arr.append(cont2[0])
# arr.append(cont3[0])
# arr.append(cont4[0])
#
# totalcont=0
# print(arr)
# # for i in range(4):
# #     totalcont=totalcont+arr[i]
# # print(totalcont)
# for i in arr:
#     totalcont = totalcont + i
#
# print(int(totalcont))

# while True:
#
#     num1=input("请输入表达式��?(q退��?)")
#     if num1=="q":
#         break
#     else:
#     # print(num1)
#         if "+" in num1:
#             collec=num1.split('+')
#             print(num1+"=",(float(collec[0])+float(collec[1])))
#         elif "-" in num1:
#             collec=num1.split('-')
#             print(num1 + "=" ,(float(collec[0]) - float(collec[1])))
#         elif "*" in num1:
#             if "**" in num1:
#                 collec = num1.split('**')
#                 # print(collec)
#                 print(num1 + "=", (float(collec[0]) ** float(collec[1])))
#             else:
#                 collec = num1.split('*')
#                 print(num1 + "=" ,(float(collec[0]) * float(collec[1])))
#         elif "/" in num1:
#             collec = num1.split('/')
#             print(num1 + "=" ,(float(collec[0]) / float(collec[1])))

# # print(56L+78L) l和L不在混合��?
# arr=[]
# arr2=[]
# for i in range(21):
#     if i%2==0:
#         arr.append(i)
#     else:
#         arr2.append(i)
# print(arr)
# print(arr2)
# while True:
#     judge_divide = input("亲输入两个连续的整数��?(用|隔开,q退��?)")
#     if judge_divide=="q":
#         break
#     else:
#         get_num = judge_divide.split("|")
#         num1 = int(get_num[0])
#         num2 = int(get_num[1])
#         if num1 % num2 == 0:
#             print("True")
#         else:
#             print("False")
#
# balence=float(input("请输入初始现金："))
# payment=float(input("请输入每月花费："))
# print("\t\t",'Amount Remaining')
# print('pymt#','\t','paid','\t','balance')
# i=0
# print(i,'\t','$',0.00,'\t','$',balence)
# while balence>0:
#     if balence < payment:
#         payment = balence
#         balence=0.00
#
#     else:
#         balence = round(balence - payment,2)
#
#     print(i+1,'\t','$',payment,'\t','$',balence)
#     i += 1
#
# a=list('abcdedcd')*3
# print(a)
# b=[1,2,3,4,5][::2]
# print(b)
# a="abcdefgh"
# print('nihao')
#
# for i in range(len(a)):
#
#     b=a[:-i]
#     print(b)


#!/usr/bin/env python
# coding=utf-8

# a=(1,2,3,'abc')
# name="mayuyuhehehelink"
# show_name=tuple(name)
# b=list(a)
# c=tuple(b)
# print(b)
# print(c)
# print(show_name,"")
# a=zip((91,"abc",3))
# print(a)
# b="abcdef"
# b[1]='o'
# print(b)
# while True:
#
#     id_name=input("请输入一个标识符：(q退出)")
#     if id_name=="q":
#         break
#     else:
#         id_name_content=list(id_name)
#
#         if id_name_content[0] not in "abcdefghijklmnopqrstuvwxyz_":
#             print("非法变量名")
#         else:
#             another=id_name[1:]
#             for rest_word in another:
#                 if rest_word not in "abcdefghijklmnopqrstuvwxyz_":
#                     print("非法变量")
#                 else:
#                     break
#             print("变量和法")

# print("%(name)s你是%(adress)s" % {"name":"liuzhaoyang",'adress':"xiguo"})
# a=sadada
# repr(a)
# a=chr(12)
# # from string import Template
# # s=Template("你好${name}地址${jianxi}")
# # b=s.substitute(name="liuzhaoyang",jianxi="jianx")
# # print(b)
# print(a)
# a="asc".center(20)
# print(a)
# a=chr(12)


# b=a
# print(b)
#
# a="ahhh\"sdjsdj\"s"
# print(a)
# import string
# s='%sD%s' % ("a","b")
# print(s)
# def get_max_number(input_zero_one):
#     ls_zero=input_zero_one.split("1")
#     ls_one=input_zero_one.split("0")
#     ls_zero.extend(ls_one)
#
#     print(max([len(i) for i in ls_zero]))
#
# if __name__=='__main__':
#     input_zero_one=input("请输入数字：")
#     get_max_number(input_zero_one)
# print("10101011111111111000".split("1"))
# print("10101011111111111000".split("0"))
#
# codec='utf-8'
# file='test.txt'
#
# hello_out='hello,world'
# bytes_out=hello_out.encode(encoding=codec)
# print(type(bytes_out))
# file_src=open(file,'w+')
# file_src.write(hello_out)
# file_src.close()
#
# file_open=open(file,'r')
# bytes_in=file_open.read()
# file_open.close()
#
# hello_in=bytes_in.encode(codec)
#
# print(hello_in)
# print(bytes_in)
#
# a=["a","b","c","e"]
# a.remove('a')
# print(a)

# stack=[]
#
# def pushit():
#     stack.append(input("请输入字符串：").strip())
#
# def popit():
#     if len(stack)==0:
#         print("栈内没有元素")
#     else:
#         print('remove [','stack.pop()',']')
#
# def viewstack():
#     print(stack)
#
# CMDs={'u':pushit,'o':popit,'v':viewstack}
#
# def show_menu():
#     pr="""
#         p(U)sh
#         p(O)p
#         (V)iew
#         (Q)uit
#
#     enter choice:"""
#
#     while True:
#         while True:
#             try:
#                 choice=input(pr).strip()[0].lower()
#             except(EOFError,KeyboardInterrupt,IndexError):
#                 choice="q"
#             print('\nyou picked:[%s]'% choice)
#             if choice not in 'uovq':
#                 print("没有该选项")
#             else:
#                 break
#             if choice=="q":
#                 break
#             CMDs[choice]()
# if __name__=='__main__':
#     show_menu()

# stack=[]
# def pushit():
#     stack.append(input("请输入字符串：").strip())
#
# def popit():
#     if len(stack)==0:
#         print("栈内没有元素")
#     else:
#         popitem=stack.pop()
#         print('已经删除了',popitem)
#
# def viewstack():
#     print(stack)
# while True:
#     choice=input("请选模式：(push,pop,view额，q)")
#     if choice=="push":
#         pushit()
#     elif choice=="pop":
#         popit()
#     elif choice=="view":
#         viewstack()
#     else:
#         print("非法输入")
#         if choice=="q":
#             break

# stack=[]
#
# def pushit():
#     stack.append(input("请输入元素："))
#
# def delete():
#     fist_out=stack[0]
#     stack.remove(stack[0])
#     print("已经删除了",fist_out)
#
# def view():
#     print(stack)
#
# while True:
#     choice=input("请选模式：(p,d,v，q)")
#     if choice == "p":
#         pushit()
#     elif choice == "d":
#         delete()
#     elif choice == "v":
#         view()
#     else:
#         print("非法输入")
#         if choice == "q":
#             break

# print(type(('abc',)))
# a='abdnkshdsklfJSKADJSKJKSDFJSDS45454'
# b='aSAD'
# print(b in a)
# num=input("请输入数字：")
# for i in reversed(sorted(num.split())):
#     print(i)
# strings=input("请输入字符串：")
# pieces=strings.split()
# print(pieces)
# print(strings)

# num_str=input("请输入一个数字：")
# num_num=int(num_str)
# arr=([].append(i) for i in range(1,num_num+1))
# # fac_list=range(1,num_num+1)
# print(arr)
# # i=0
# # while i<len(arr):
# #     if num_num%arr[i]==0:
# #         del arr[i]
# #         i+=1
# # print(arr)
#
#
#
# num_str=input("shuru:")
# num_num = int(num_str)
# fac_list = range(1, num_num+1)
# print ("BEFORE:", fac_list)
#
#
# i = 0
#
#
# while i < len(fac_list):
#
#
#     if num_num % fac_list[i] == 0:
#         del fac_list[i]
#
#     i = i + 1
#
# print ("AFTER:", 'fac_list')

# string=input("亲输入非数字字符串：")
# content=[]
# item=list(string)
# print(item)
# for i in item:
#     if i.isupper():
#         e=i.lower()
#         content.append(e)
#
#     else:
#         e=i.upper()
#         content.append(e)
# # result=unicode(content)
#
# name=''.join(content)
#
# print(name)
# a=dict([[1,2],["a","sd"]])
# print(a)
# print(hash(12) ==hash("12"))
# idst={'age':'12','name':'liuzy','add':'xiguo'}
# print(idst.keys())
# print(idst.values())
# print(idst.get('name'))
# a=('a',[1,2,3],'b')
# a[1][0]=0
# print(a)


# db={}
#
# def newuser():
#     prompt='login desired:'
#     while True:
#         name=input(prompt)
#         if name in db.keys():
#             print('name taken,try another')
#             continue
#         else:
#             break
#     pwd=input('passwd:')
#     db[name]=pwd
#
# def olduser():
#     name=input('login:')
#     pwd=input('password:')
#     passwd=db.get(name)
#     if passwd==pwd:
#         print('welcome',name)
#     else:
#         print('login incorrect')
# def showmenu():
#     prompt= """
#     (N)ew user login
#     (E)xisting user login
#     (Q)uit
#
#     enter choice:"""
#     done=False
#     while not done:
#
#         chosen=False
#         while not chosen:
#             try:
#                 choice=input(prompt).strip()[0].lower()
#             except(EOFError,KeyboardInterrupt):
#                 choice='q'
#             print('\nyou picked:[%s]'% choice)
#             if choice not in 'neq':
#                 print('invalid option,try again')
#             else:
#                 chosen=True
#         if choice =='q':done=True
#         if choice=='n':newuser()
#         if choice=='e':olduser()
#
# if __name__=='__main__':
#     showmenu()
# a=set('abdcdfdsfds')
# b=a.pop()
# print(b)
# print(a)
# a=zip([1,2,3,4,5,6],["abc","def","ghi","jkl","mkl","sda"])
# b=dict(a)
# for each in b:
#     c=[].append(each)
#     d=[].append(b[each])
# print(c)
# #
# # print(e)
# x=1
# y=2
# smaller=x if y>x else y
# print(smaller)
# passwd_list=['1994','2004']
# valid=False
# count=3
# while count>0:
#     input1=input("passwd:")
#     for eachpass in passwd_list:
#         if input1==eachpass:
#             valid=True
#             break
#     if not valid:
#         print('invalid input')
#         count-=1
#         continue
#     else:
#         break

# a=iter('asdfghj')
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())

# a=(i**2 for i in range(9) if i%2==0)
# b=list(a)
# print(b)
# num=input("请输入：").split()
# beg=int(num[0])
# end=int(num[1])
# length=int(num[2])
# a=([i for i in range(beg,end,length)])
# print(a)
# isinstance(u"我", string)

# def shusu(num):
#     if num==2:
#         print(num)
#     else:
#         if num%2==1:
#             if num % 3 != 0 and num % 5 != 0 or num%7==0:
#                 print(num)
#
#             else:
#                 if num % 6 == 0 and num % 10 == 0 or num % 14 == 0:
#
#                     print('false')
#                 else:
#                     print(num)
#                 print(num)
#         else:
#             print('False')
#
# for i in range(101):
#     shusu(i)
# def isPrime(n):
#     if n <= 1:
#         print('False')
#     i = 2
#     while i*i <= n:
#         if n % i == 0:
#             print('False')
#         i += 1
#     print(n)
# def isPrime(n):
#     if n <= 1:
#         print('False')
#     if n == 2:
#         print(n)
#     if n % 2 == 0:
#         print('False')
#     i = 3
#     while i * i <= n:
#         if n % i == 0:
#             print('False')
#         i += 2
#     print(n)
#
# for i in range(101):
#     isPrime(i)

# def is_prime(n):
#     for i in range(1,int(n / 2)):
#         if n%i==0 :
#             print('false')
#         else:
#             print(n)
# for q in range(101):
#     is_prime(q)
# print(1//2)
# def is_prime(n):
#     if n%2==1 and (n//2) !=0:
#         for i in range(1,11):
#             if n%((n-1)*i)!=0:
#                 print(n)
#             else:
#                 print('false')
#     else:
#         print('false')
#
# for q in range(100):
#     is_prime(q)
#
# def isPrime1(n):
#     if n==0 or n==1:
#         print('false')
# 	for i in range(2,n):
# 		if n % i == 0:
# 			return False
# 	return True
# for q in range(100):
#     isPrime1(q)


# def is_primer(n):
#     if n==0 or n==1:
#         print('false')
#     else:
#         for i in range(2,n):
#             if n%i==0:
#                 return False
#         print(n)
# for q in range(100):
#     is_primer(q)
# arr=[]
# num=int(input('请输入一个数：'))
# for i in range(1,num):
#     if num%i==0:
#         arr.append(i)
#     else:
#         print(i)
# print(arr)
# def isPrime1(n):
# num=int(input("请输入一个数："))
# n=num
# arr=[]
# if n == 0 or n == 1:
#     pass
# else:
#     for i in range(2, n):
#         if n % i == 0:
#
#             arr.append(i)
# print(arr)

# for q in range(1,num):
#     if isPrime1(q):
#         if isPrime1((num//q)):
#             arr.append(q)
# print(arr)
# f = open('..\me','w+')
# f.tell()

# file_name=input('请输入一个文件名包括后缀名：')
# fobj=open(file_name,'a+')
# while True:
#     a_line=input('请输入一行文字：（q退出）')
#     if a_line !='q':
#         fobj.write('%s'% a_line+'\n')
#     else:
#         break
# fobj.close()
#
# text=open(file_name,'r')
# for each in text:
#     print(each)

# import sys,os
# print(sys.stdout)
# print(os.path)
# print(os.listdir('../'))

# import os
# for tmpdir in ('/tmp',r'c:\temp'):
#     if os.path.isdir(tmpdir):
#         break
#     else:
#         print('没有该目录')
#         tmpdir=''
# os.mkdir('test')
#
# tmpdir='./test'
# if tmpdir:
#     # 切换工作目录
#     os.chdir(tmpdir)
#     cwd=os.getcwd()
#     print('现在的工作目录是：',cwd)
#     # 创建目录
#     print('创建测试目录：')
#     os.mkdir('example')
#     # 切换到新建的目录
#     os.chdir('example')
#     cwd=os.getcwd()
#     print("新的工作目录是：",cwd)
#     # 获取所有该目录下的文件名
#     print('路径重的所有文件：',os.listdir(cwd))
#
#     print('创建测试文件:')
#     fobj=open('test','w+')
#     fobj.write('liu\n')
#     fobj.write('zhao\n')
#     fobj.write('yang\n')
#
#     fobj.close()
#
#     print('查看是否真的创建文件成功')
#     print(os.listdir(cwd))
# #     对文件重命名
#     print('正在重命名文件：')
#     os.rename('test','liuzhaoyang.txt')
#     print('重命名成功',os.listdir(cwd))
#
#     path=os.path.join(cwd,os.listdir(cwd)[0])
#     print('文件的绝对路径是：',path)
#     print('patnname,basename',os.path.split(path))
#     print('filename,extension',os.path.splitext(os.path.basename(path)))
# #     展现文件内容
#     print('文件内容是：')
#     fobj=open(path)
#     for each_item in fobj:
#         print(each_item)
#     fobj.close()
#
# #     删除文件
#     print('正在删除文件:')
#     os.remove(path)
#     print('跟新目录文件内容：',os.listdir(cwd))
# #     改变工作目录
#     os.chdir(os.pardir)
#     print('现在在父目录：')
# #     删除测试目录
#     print('正在删除测试目录：')
#     os.rmdir('example')
#     print('完成')

# import urllib.request
# res=urllib.request.urlopen('http://www.bilibili.com/')
# html=res.read()
# html=html.decode('utf-8')
# print(html)

# import urllib.request
# for i in range(20):
#     name=str(i)
#
#     res=urllib.request.urlopen('https://placekitten.com/500/600')
#     name=res.read()
#     with open('cat_500_600'+str(i)+'.jpg','wb') as f:
#         f.write(name)
#
# import urllib.request
# for i in range(1):
#     name=str(i)
#
#     res=urllib.request.urlopen('https://placekitten.com/500/600')
#     name=res.read()
#     with open('cat_500_600'+str(i)+'.jpg','wb') as f:
#         f.write(name)
# print(res.info())


# import urllib.parse,urllib.request
# import json
#
# data={}
# data['type']='AUTO'
# data['i']='i love you'
# data['doctype']='json'
# data['xmlVersion']='1.8'
# data['keyfrom']='fanyi.web'
# data['ue']='UTF-8'
# data['typoResult']='true'
# data['action']="FY_BY_CLICKBUTTON"
# data=urllib.parse.urlencode(data).encode('utf-8')
#
# url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.google.co.jp/'
# res=urllib.request.urlopen(url,data)
#
# html=res.read().decode('utf-8')
# html=html.strip()
#
# # print(html['translateResult'][0][0]['src'])
# # with open('translate.txt','w+') as file:
# #     file.write(html.strip())
# print(html)
# print(type(html))


# import urllib.parse
# import urllib.request
# import json
#
# content=input("请输入要翻译的内容：")
# url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.google.co.jp/'
# head={}
# head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36'
# data={}
# data['type']='AUTO'
# data['i']=content
# data['doctype']='json'
# data['xmlVersion']='1.8'
# data['keyfrom']='fanyi.web'
# data['ue']='UTF-8'
# data['typoResult']='true'
# data['action']="FY_BY_CLICKBUTTON"
# data=urllib.parse.urlencode(data).encode('utf-8')
#
# res=urllib.request.urlopen(url,data)
#
# html=res.read().decode('utf-8')
#
# target=json.loads(html)
#
# print(target['translateResult'][0][0]['tgt'])

# import urllib.request
# import random
#
# url='http://www.whatismyip.com.tw'
# iplist=['110.72.204.12:8080']
#
# proxy_support=urllib.request.ProxyHandler({'http':random.choice(iplist)})
#
# opener=urllib.request.build_opener(proxy_support)
#
# urllib.request.install_opener(opener)
#
# res=urllib.request.urlopen(url)
# html=res.read().decode('utf-8')
#
# print(html)
# def safe_float(obj):
#     try:
#         retval= float(obj)
#     except ValueError:
#         retval='could not convert non-number to float'
#
#
# safe_float([0,1])
# 时间空间大家聚聚上看到是
# '''

#
# def safe_float(obj):
#     'safe version of float'
#     try:
#         retval=float(obj)
#     except (ValueError,TypeError) as e:
#         retval=str(e)
#     return retval
# def main():
#     '处理所有数据'
#     log=open('cardlog.txt','w')
#     try:
#         ccfile=open('carddate.txt','r')
#     except IOError as e:
#         log.write('no txns this month\n')
#         log.close()
#         return
#     txns=ccfile.readlines()
#     ccfile.close()
#     total=0.00
#     log.write('account log:\n')
#
#     for each_txn in txns:
#         result=safe_float(each_txn)
#         if isinstance(result,float):
#             total+=result
#             log.write('data....processed\n')
#         else:
#             log.write('ignored:%s'% result)
#     print('$%.2f(new balence)'%(total))
#     log.close()
#
# if __name__=='__main__':
#     main()

# assert 1===

# from operator import add, sub
# from random import randint, choice
#
# ops = {'+': add, '-': sub}
# MAXTRIES = 2
#
#
# def doprob():
#     op = choice('+-')
#     nums = [randint(1, 10) for i in range(2)]
#     nums.sort(reverse=True)
#     ans = ops[op](* nums)
#     pr = '%d %s %d=' % (nums[0], op, nums[1])
#     oops = 0
#     while True:
#         try:
#             if int(input(pr)) == ans:
#                 print('correct')
#                 break
#             if oops == MAXTRIES:
#                 print('answer\n%s%d' % (pr, ans))
#             else:
#                 print('incorect...try again')
#                 oops += 1
#         except(KeyboardInterrupt, EOFError, ValueError) as e:
#             print(e, 'try later again')
#
#
# def main():
#     while True:
#         doprob()
#         try:
#             opt = input('again?[y]'.lower())
#             if opt and opt[0] == 'n':
#                 break
#         except(KeyboardInterrupt, EOFError) as e:
#             break
# if __name__ == '__main__':
#     main()

# a=input('qingsuru:')
# print(eval(a))

# a=lambda x:x+3
# print(a(5))
#
# def foo():
#     m=3
#     def bar():
#         n=4
#         print(m+n)
#
# print(m)
# bar()

# def counter(num=0):
#     count=[num]
#     def incr():
#         count[0]+=1
#         return count[0]
#     return incr
# coo=counter(5)
# print(coo)
# print(coo(),coo())
# print()
# print(coo())

# def foo():
#     m=3
#     def bar():
#         n=4
#         print(m+n)
# # print(m)
# bar()

class AddBookEntry:
    'address book entry class'
    def __init__(self,nm,ph):
        self.name=nm
        self.phone=ph
        print('creat instance for:',self.name,self.phone)
    def up_date_phone(self,new_phone):
        self.phone=new_phone
        print('update phone for:',self.phone)

    def __del__(self):
        pass
#
# new1=AddBookEntry('liu',575563079)
# new1.up_date_phone(45464)
# print(new1.__dict__)
# # print(new1.__name__)
# print(new1.__doc__)
# print(dir(AddBookEntry))

# class X(AddBookEntry):
#     def __init__(self):
#         print('初始化')
#     def __del__(self):
#         # super().__del__()
#         AddBookEntry.__del__(self)
#         print('删除应用')
#
# a=X()
# b=a
# c=a
# print(id(a),id(b),id(c))
# del(a)
# del(b)
# del(c)

# class HotelRoomCalc(object):
#     'hotelroom rate calculate'
#     def __init__(self,rt,sales=0.085,rm=0.1):
#         # """HotelRoomCalc default arguments:
#         # sales tax==8.5% and room tax ==10%
#         # """
#         self.salesTax=sales
#         self.roomRate=rt
#         self.roomTax=rm
#     def calcTotal(self,days=1):
#         'calculate total;default to daily rate'
#         daily=round(self.roomRate*(1+self.roomTax+self.salesTax),2)
#         return float(days)*daily
#
# sfo=HotelRoomCalc(299)
# print(sfo.calcTotal(2))



#
#
# import urllib.request
#
#
#
# url='http://www.qiushibaike.com/'
#
#
# res=urllib.request.urlopen(url)
#
# html=res.read().decode('utf-8')
#
#
#
# print(html)
# 正则表达式
# import re
# patt='^w[3]\.\w[9]\.\@(\w)+\.(\w)+$'
# patt=re.compile(patt)
# print(re.match(patt,'www.575563079@qq.com'))
# 三元运算符有点像一个列表生成器
# x=5
# y=3
# smaller=[x if x<y else y]
# print(smaller)

# import re
# m=re.match('foo','food is not good')
# if m != None:
#     print(m.group())
# print(m)

# import re
# m=re.search('foo','not food is not good')
# if m != None:
#     print(m.group())
# print(m)
# 匹配多个字符串
# import re
# an='.{2}end'
# m=re.match(an,'sbend')
# if m!=None:
#     print(m.group())
# import re
# m=re.search('[cr][23][dp][o2]','anannsdnskdjr2p2dsdsds')
# if m is not None:
#     print(m.group())

# patt='\w+@(\w+\.)*\w+\.com'
# rm=re.match(patt,'nobody@sdasdasd.xxxx.xsx.ss.com')
# if rm is not None:
#     print(rm.group())

# m=re.match('^the','thenandnsk sjds')
# if m is not None:
#     print(m.group())
# r=re.findall('(abc)|(sd)','abc hjsd jsdskk s abc abc')
# print(r)
# m=re.subn('a','abcd','and a number a')
# print(m)
#
# import re
# # f=open('user_agent.txt','r+')
# # for each_line in f.readlines():
# #     print(re.split('\s\s+|\t',each_line))
# # f.close()
# r=re.search('\bbend','bend')
# print(r)
#
# from random import randint,choice
# from string import ascii_lowercase
# from sys import maxsize
# from time import ctime
#
# doms=('com','edu','net','org','gov')
#
# for i in range(randint(5,10)):
#     dtint=randint(0,10000000)
#     print(dtint)
#     dtstr=ctime(dtint)
#     shorter=randint(4,7)
#     em=''
#
#     for j in range(shorter):
#         em+=choice(ascii_lowercase)
#     longer=randint(shorter,12)
#     dn=''
#
#     for j in range(longer):
#         dn+=choice(ascii_lowercase)
#
#     print('%s::%s@%s.%s::%d-%d-%d' % (dtstr,em,dn,choice(doms),dtint,shorter,longer))
#
# print(maxsize)
# print(ctime())
# from socket import *
# from time import ctime
# from sys import *
#
# HOST=''
# PORT=21567
# BUFSIZE=1024
# ADDR=(HOST,PORT)
#
# tcp_ser_sock=socket(AF_INET,SOCK_STREAM)
# tcp_ser_sock.bind(ADDR)
# tcp_ser_sock.listen(5)
#
# while True:
#     print('等待连接')
#     tcp_cli_sock,addr=tcp_ser_sock.accept()
#     print('链接来自：',addr)
#
#     while True:
#         data=tcp_cli_sock.recv(BUFSIZE)
#         if not data:
#             break
#         tcp_cli_sock.send(str.encode(ctime()),data)
#         tcp_cli_sock.close()
# tcp_ser_sock.close()

# # 导入socket，sys模块
# import socket
# import sys
#
# # 创建socket对象
# server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#
# # 获取本地主机名
# host=socket.gethostname()
#
# port=9999
#
# # 绑定端口和主机
# server_socket.bind((host,port))
#
# # 设置最大连接数，超过后柱塞排队
# server_socket.listen(5)
#
# while True:
# #     建立客户端链接
#     client_socket,addr=server_socket.accept()
#     print('链接地址：%s' % str(addr))
#     msg='欢迎访问mayuyu.site'+'\r\n'
#     client_socket.send(msg.encode('utf-8'))
#     client_socket.close()
# from socket import *
# import sys
# s = socket(AF_INET,SOCK_STREAM)
# # 建立连接:
# s.connect(('127.0.0.1', 8888))
#
# while True:
#     word_client=input('请输入对话：')
#     s.send(word_client.encode('utf-8'))
# # # 接收欢迎消息:
# # print(s.recv(1024).decode('utf-8'))
# # for data in [b'Michael', b'Tracy', b'Sarah']:
# #     # 发送数据:
# #     s.send(data)
# #     # print(s.recv(1024).decode('utf-8'))
# # s.send(b'exit')
# # s.close()

# import re
# pat='(abc)(am)(cm)'
# pat=re.compile(pat)
# print(re.match(pat,'abcamcm').group(3))
# print(re.search(pat,'abcamcm').group())

# import pymysql
# conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='root',db='mysql',charset='UTF8')
# curse=conn.cursor()
# curse.execute('show tables')
# for i in curse:
#     print(i)
# curse.close()
# conn.close()


#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# import socket
# from time import ctime
#
# '''
# host为空表示bind可以绑定到所有有效地址上
# port 必须要大于1024
# bufsiz为缓冲区 我们设置为1K
# '''
# host = ''
# port = 23456
# bufsiz = 1024
# ADDR = (host,port)
#
# tcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# tcpSerSock.bind(ADDR)
# tcpSerSock.listen(5)   #参数表示允许多少连接同时连进来
#
# try:
#     while True:
#         '''
#         进入服务器的无限循环中，等待连接到来
#         有链接时，进入对话循环，等待客户发送数据，如果消息为空，表示客户端已经退出，等待下一个客户端连接
#         得到客户端消息后在消息前加一个时间戳后返回
#         '''
#         print('waiting for connection...')
#         tcpSerSock,addr = tcpSerSock.accept()
#         print('...connected from ',addr)
#
#         while True:
#             data = tcpSerSock.recv(bufsiz)
#             print(data)
#             if not data:
#                 print('在这里出错了')
#                 break
#             tcpSerSock.send('[%s] %s'.encode('utf-8') %(ctime(),data))
# except BaseException as e:
#     tcpSerSock.close()  #记住在服务器退出时记得关闭

# import re
# patt=r'(([1]\d?\d|[2][0-4]\d|[25]\d)\.){3}([01]?\d?\d|[2][0-4]\d|[25]\d)|((\d?|[2][0-4]\d|[25]\d)\.){3}(\d?|[2][0-4]\d|[25]\d)'
# result=re.search(patt,'000009.1.0.0')
# print(result)

# datetime模块
# from datetime import datetime
# now=datetime.now().timestamp().__int__()
# print(now)
# print(type(now))
# # 获取指定的时间和日期
# dt=datetime(2015,4,18,12,59,22)
# print(dt)
# # 获取指定时间的unix时间戳
# ts=datetime(2015,4,18,12,59,22).timestamp()
# print(ts)
# # unix时间戳转换为指定时间
# timem=1429333162.0
# stp=datetime.fromtimestamp(timem)
# print(stp)
# # str转换为datetime
# cday=datetime.strptime('2015-6-1 18:19:59','%Y-%m-%d %H:%M:%S')
# print(cday)
# # datetime转换为str输出
# nday=datetime.now().strftime('%a,%b %d %H:%M')
# print(nday)

# collections集合模块
# from collections import namedtuple,deque
# point=namedtuple('point',['x','y','z'])
# p=point(1,2,3)
# print(p.x)
# print(p.y)
# print(p.z)
#
# q=deque([1,2,3])
# q.append(5)
# q.appendleft([8,'name'])
# print(q)
#
# from collections import OrderedDict
# a=dict([('a',1),('c',2),('b',3)])
# print(a)
# b=OrderedDict([('a',1),('b',3),('c',2)])
# print(b)


# from collections import OrderedDict
# d = dict([('a', 1), ('b', 2), ('c', 3)])
# print(d)
# od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# import hashlib
#
# md5 = hashlib.md5()
# md5.update('我是你大爷'.encode('utf-8'))
# print(md5.hexdigest())
# import itertools
# natuals = itertools.count(1)
# ns = map((lambda x: x <= 10), natuals)
# print(list(ns))


# 装饰器
# def now():
#     print("2016.8.3")
#
# now()
# f=now
# f()
#
#
#
# print(id(f))
# print(f.__name__)
# print(now.__name__)


# def shout(word="yes"):
#     return word.capitalize()+"!"
# print(shout())
#
# scream=shout
# print(scream())
# del shout
# try:
#     print(shout())
# except NameError as e:
#     print(e)
#
# print(scream())
#
# def talk():
#     def whisper(word="yes"):
#         return word.lower()+"..."
#     print(whisper())
# talk()
# try:
#     print(whisper())
# except NameError as e:
#     print(e)
#
# def getTalk(type="shout"):
# #     定义函数
#     def shout(word="shout"):
#         return word.capitalize()+"!"
#     def whisper(word="yes"):
#         return word.lower()+"..."
# #     返回函数
#     if type=="shout":
#         return shout
#     else:
#         return whisper
# talk=getTalk()
# print(talk())
# print(getTalk("whisper")())
#
# def bread(func):
#     def wrapper():
#         print("</......\>")
#         func()
#         print("<00000000>")
#     return wrapper
#
# def inget(func):
#     def wrapper():
#         print("#tomas")
#         func()
#         print("salad")
#     return wrapper
# @bread
# @inget
# def sandwich(food="--hanm--"):
#     print(food)
#
# sandwich()

# sandwich=bread(inget(sandwich))
# sandwich()

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import time
# url = "https://eastlakeside.gitbooks.io/interpy-zh/content/args_kwargs/Usage_args.html"
# filehandle = urlopen(url)
# html = filehandle.read()
# with open('git2.html','wb') as file:
#     file.write(html)
#
# soup = BeautifulSoup(html,'lxml')
# tags = soup.findAll('li', {'class':'chapter'})
#
# links = []
# for tag in tags:
#     links.append(tag.a.attrs['href'])
#
#
# # # print(links)
# def complete_link(current_url, url):
#     from urllib.parse import  urljoin
#     dest_url = urljoin(current_url, url)
#     return dest_url
#
# dest=[]
# for i in links:
#     url=complete_link("https://eastlakeside.gitbooks.io/interpy-zh/content/args_kwargs/Usage_args.html",i)
#     dest.append(url)
#
# print(len(dest))
# for url_str in dest:
#
#     filehandle2 = urlopen(url_str)
#     html = filehandle.read()
#     print("正在处理"+url_str)
#     if "html" not in url_str:
#         url_str+="index.html"
#     print(url_str[-1:-6])
#     # with open(url_str[-1:-6], 'wb') as file:
#     #     file.write(html)
#     # time.sleep(2)

#清晰数据
# strings=['', '', '', '', '', '', '', '', '', '', 'パイパン全裸奴隷 夫の部下に剃毛調教された巨乳妻 本田岬', '', '', '', '', '高清', '', '', '', '', 'JUFD-612', ' / ', '2016-06-30', '', '', '', '']
# a=[]
# for i in strings:
#     if i =='' or i==' / ':
#         pass
#     else:
#         a.append(i)
# print(a)

# import random
# UserAgent = [
#     'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)',
#     'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2)',
#     'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
#     'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
#     'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',
#     'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
#     'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
#     'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
#     'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13',
#     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
#     'Mozilla/5.0 (iPhone; U; CPU like Mac OS X) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/4A93 Safari/419.3',
#     'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Version/3.1 Safari/525.13'
# ]
#
# for i in range(200):
#     user_agent = UserAgent[random.randint(0, len(UserAgent) - 1)]
#     print(user_agent)

# a=['sdsds',123]
# b=str(a)
# print(type(b))

# a='asd12d'
# b=a.upper()
# print(b)
# import hashlib
#
# import json
# import rsa
# import base64
# import requests
# import time

# req=requests.get('https://passport.bilibili.com/login?act=getkey&_= + '+time.ctime())
# hash_key=req.text
# hash_key_list=list(hash_key)
# hash=hash_key[8:25]
# key=hash_key[62:-30]
# key_list=key.split('\\n')
# key="".join(i for i in key_list)
# # print(key)
# # key=key_list[0]+key_list[1]+key_list[2]+key_list[3]
# passwd=730089615
# psd=hash+str(passwd)
#
#
# base_decode=base64.b64decode(key)
# (base_decode, base_decode) = rsa.newkeys(1024)
# print(base_decode)
# # 对密文加密
# rsa_pass=rsa.encrypt(psd.encode(),base_decode)
# password=base64.b64encode(rsa_pass).decode('utf-8')
# print(password)
#
# with open('../python_spider/lagou_job_java.txt','r',encoding='utf-8') as file:
#     line=file.readline()
#     a='任职要求'
#     try:
#         if a in line:
#             print('a')
#         b=line.index(a)
#         c=line[:179]
#         print(c)
#         print(b)
#     except Exception as e:
#         pass
#     print(line)

# import time
# time.sleep(0.6)
# str='0123456789'
# print(str[:5:-1])
# print(str[::-2])
# with open('./source_file/ip_bus.txt','r') as file:
#     for i in file:
#         print(i)


# a='\n\n明天周二(09月06日)\n\n白天\n\n\n阵雨\n26℃\n东'
# print(a.replace('\n',""))
#
#
# job_name=input('请输入职位名（如php）:').title()
# print(job_name)

# import urllib.parse
# url='https://www.baidu.com'
# url_list=urllib.parse.urlparse(url)
# print()


#! -*-coding:utf-8 -*-
'''
Function:计算拉勾网编程语言的关键词排名
Author:蘭兹
'''


from urllib import request, parse
from bs4 import BeautifulSoup as Bs
from collections import Counter
import lxml
import json
import datetime
import xlsxwriter
import re

starttime = datetime.datetime.now()

url = r'http://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC'

keyword = input('请输入您所需要查找的关键词 : ')


# 获取职位的查询页面(参数分别为网址，当前页面数，关键词)
def get_page(url, pn, keyword):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
        'Host': 'www.lagou.com',
        'Connection': 'keep-alive',
        'Origin': 'http://www.lagou.com'
        }
    if pn == 1:
        boo = 'true'
    else:
        boo = 'false'
    # 通过页面分析，发现浏览器提交的FormData包括以下参数
    data = parse.urlencode([
        ('first', boo),
        ('pn', pn),
        ('kd', keyword)
        ])
    req = request.Request(url, headers=headers)
    page = request.urlopen(req, data=data.encode('utf-8')).read()
    page = page.decode('utf-8')
    return page


# 获取所需的岗位id,每一个招聘页面详情都有一个所属的id索引
def read_id(page):
    tag = 'positionId'
    page_json = json.loads(page)
    page_json = page_json['content']['result']
    company_list = []
    for i in range(15):
        company_list.append(page_json[i].get(tag))
    return company_list


# 获取当前招聘关键词的最大页数，大于30的将会被覆盖，所以最多只能抓取30页的招聘信息
def read_max_page(page):
    page_json = json.loads(page)
    max_page_num = page_json['content']['totalPageCount']
    if max_page_num > 30:
        max_page_num = 30
    return max_page_num


# 获取职位页面，由ositionId和BaseUrl组合成目标地址
def get_content(company_id):
    fin_url = r'http://www.lagou.com/jobs/%s.html' % company_id
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
        'Host': 'www.lagou.com',
        'Connection': 'keep-alive',
        'Origin': 'http://www.lagou.com'
        }
    req = request.Request(fin_url, headers=headers)
    page = request.urlopen(req).read()
    content = page.decode('utf-8')
    return content


# 获取职位需求（通过re来去除html标记），可以将职位详情单独存储
def get_result(content):
    soup = Bs(content, 'lxml')
    job_description = soup.select('dd[class="job_bt"]')
    job_description = str(job_description[0])
    rule = re.compile(r'<[^>]+>')
    result = rule.sub('', job_description)
    return result


# 过滤关键词：目前筛选的方式只是选取英文关键词
def search_skill(result):
    rule = re.compile(r'[a-zA-z]+')
    skill_list = rule.findall(result)
    return skill_list


# 对出现的关键词计数，并排序，选取Top80的关键词作为数据的样本
def count_skill(skill_list):
    for i in range(len(skill_list)):
        skill_list[i] = skill_list[i].lower()
    count_dict = Counter(skill_list).most_common(80)
    return count_dict


# 对结果进行存储并生成Area图
def save_excel(count_dict, file_name):
    book = xlsxwriter.Workbook(r'C:\Users\Administrator\Desktop\%s.xls' % file_name)
    tmp = book.add_worksheet()
    row_num = len(count_dict)
    for i in range(1, row_num):
        if i == 1:
            tag_pos = 'A%s' % i
            tmp.write_row(tag_pos, ['关键词', '频次'])
        else:
            con_pos = 'A%s' % i
            k_v = list(count_dict[i-2])
            tmp.write_row(con_pos, k_v)
    chart1 = book.add_chart({'type': 'area'})
    chart1.add_series({
        'name': '=Sheet1!$B$1',
        'categories': '=Sheet1!$A$2:$A$80',
        'values':  '=Sheet1!$B$2:$B$80'
    })
    chart1.set_title({'name': '关键词排名'})
    chart1.set_x_axis({'name': '关键词'})
    chart1.set_y_axis({'name': '频次（/次）'})
    tmp.insert_chart('C2', chart1, {'x_offset': 25, 'y_offset': 10})

######################################################################################

if __name__ == '__main__':
    max_pn = read_max_page(get_page(url, 1, keyword))  # 获取招聘页数
    fin_skill_list = []  # 关键词总表
    for pn in range(1, max_pn):
        print('***********************正在抓取第%s页信息***********************' % pn)
        page = get_page(url, pn, keyword)
        company_list = read_id(page)
        for company_id in company_list:
            content = get_content(company_id)
            result = get_result(content)
            skill_list = search_skill(result)
            fin_skill_list.extend(skill_list)
    print('***********************开始统计关键词出现频率***********************')
    count_dict = count_skill(fin_skill_list)
    print(count_dict)
    file_name = input(r'请输入要保存的文件名：')
    save_excel(count_dict, file_name)
    print('***********************正在保存到桌面***********************')
    endtime = datetime.datetime.now()
    time = (endtime - starttime).seconds
    print('总共用时：%s s' % time)







