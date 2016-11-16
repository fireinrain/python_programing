#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang

# import glob
# import os
#
# a=os.scandir('E')
# for i in a:
#     print(i)
# dirs=glob.glob(r'.')
# for i in dirs:
#     print(i)




# import ctypes
# import os
# import platform
#
#
#
# # 获取系统盘符号
# def get_driver_name():
#
#     if platform.system()=='Windows':
#         #获取系统盘符，只能win下使用
#         lpBuffer = ctypes.create_string_buffer(78)
#         ctypes.windll.kernel32.GetLogicalDriveStringsA(ctypes.sizeof(lpBuffer), lpBuffer)
#         vol = lpBuffer.raw.split('\x00'.encode())
#         drive_list_raw=list(i.decode('utf-8') for i in vol)
#
#         space=drive_list_raw.index('')
#         # print(space)
#         drive_list_raw=drive_list_raw[:space]
#         drive_list=[]
#         for i in drive_list_raw:
#             if os.path.isdir(i):
#                 drive_list.append(i)
#
#         # print(drive_list)
#     else:
#
#         # 第二种方法是遍历字母，拼接为dir，判断是否是dir
#         drive_list=[]
#         for i in range(65,91):
#             vol = chr(i) + ':'
#             if os.path.isdir(vol):
#                 drive_list.append(vol)
#     return drive_list
#
#
# def walk_file(dirs,file_type=None):
#     visited={}
#     target=[]
#     for (this_dir,current_dir_dirs,file_here) in os.walk(dirs):
#         # print(current_dir_dirs)
#         this_dir=os.path.normpath(this_dir)
#         # print(this_dir)
#         # fixcase_this_dir=os.path.normcase(this_dir)
#         # print(fixcase_this_dir)
#         # if fixcase_this_dir in visited:
#         #     continue
#         # else:
#         #     visited[fixcase_this_dir]=True
#         for file_name in file_here:
#             if file_type in file_name:
#                 file_path = os.path.join(this_dir,file_name)
#                 file_size = os.path.getsize(file_path)
#                 file_size = file_size/(1024**2)
#                 target.append([file_size,file_path])
#     # print(target)
#     return target
#
# def biggist_file(*target):
#     big_list=sorted(target)
#
#     return big_list
#
# def write_to_file(small_to_big,biggist):
#     with open('file.txt','w',encoding='utf-8') as file:
#         number = len(small_to_big)
#         big=biggist[1]
#         size=biggist[0]
#         file.write('----------共找到%d个结果-------\n' % number)
#         file.write('-------->最大文件为：%s==%.2f MB\n' % (big,size))
#         for item in small_to_big:
#             line=item[1]+'--->'+str(item[0])+'MB'
#             file.write(line+'\n')
#             # print(line)
#
#         print('查找完成')
#
# def main():
#     while True:
#         patter=input('请选择查询模式：（A：全盘），（S：自定义），（C,退出）')
#         if patter in'Cc':
#             break
#         else:
#
#             if patter in 'Aa':
#                 file_type = input("请输入要搜索的文件相关符号：")
#                 dirs=get_driver_name()
#                 with open('file.txt','w',encoding='utf-8') as file:
#                     for dir in dirs:
#                         target = walk_file(dir, file_type)
#                         for item in target:
#                             print(item)
#             elif patter in 'Ss':
#                 dir=input('请输入要查询的路径：')
#                 file_type = input("请输入要搜索的文件相关符号：")
#                 target = walk_file(dir, file_type)
#                 # aim_list=biggist_file(target)[-1][0]
#                 aim_list=biggist_file(target)
#                 # 将文件按照从大到小排列
#                 small_to_big=sorted(aim_list[0])
#                 # 获取最大文件
#                 biggist=small_to_big[-1]
#                 # 获取文件数
#                 # number=len(aim_list)
#                 write_to_file(small_to_big,biggist)
#
#                 # print(aim_list)
#
#
#
# if __name__=='__main__':
#     main()

# import random
# a=random.randrange(1000)
# print(type(a))

# import time
# import requests
#
# # from tomorrow import threads
# # 创建进程池
# from multiprocessing import Pool
# # 创建线程池
# from multiprocessing.dummy import Pool as ThreadPool
#
# urls = [
#     'http://tieba.baidu.com',
#     'http://v.baidu.com',
#     'https://www.hao123.com',
#     'http://www.baidu.com',
#     'http://news.baidu.com',
# ]
# urls=urls*10
#
# def download(url):
#     req=requests.get(url).text
#     print(req)
#
# pool=ThreadPool(4)
# start = time.time()
# results=pool.map(download,urls)
# print(type(results))
# end = time.time()
# print ("Time: %f seconds" % (end - start))
# pool.close()
# pool.join()
# name='KAWD-680 kawaiiさくらゆら×S1天使もえ Wエンジェル 初レズ解禁＆仲良し共演 4時間SPECIAL'
# import os
# name1=''.join(i for i in name.split() if i or i not in '*')
# name2=''.join(name.split('*'))
# print(name1)
# print(name2)
# os.mkdir(name2)

# def pas():
#     a=0
#     for i in range(1000000):
#         i+1
#     return a
#
# if __name__=='__main__':
#     num='|'*len(range(50))
#     count=0
#     for n in range(50):
#         b=len(range(50))
#         pas()
#         print('*'*count+num[count:])
#         count+=1
# import sys,time
# j = '*'
# if __name__ == '__main__':
#     for i in range(1,61):
#         j += '*'
#         print(str(int((i/60)*100))+'%  ||'+j+'->'+"\r",end='')
#
#         time.sleep(0.5)
#
# a=682
# for i in range(1,683):
#     print(i)

# def fibna():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
# for i in fibna():
#     print(i)

# def countdown(n):
#     while n > 0:
#         yield n
#         n -= 1
# a=countdown(10)
# a.next()
# a.next()
#
# (1,2,3,4).next()

# class Foo:
#
#     def Bar(self):
#         print('bar')
#     def Hello(self,name):
#         print('hello,%s' % name)
#
# obj=Foo()
# obj.Bar()
# obj.Hello('消遣')
#
# # class Peolpe:
# #     def __init__(self,name,age,sex,hobby):
# #         self.name=name
# #         self.age=age
# #         self.sex=sex
# #         self.hobby=hobby
# #
# #     def introduce(self):
# #         print(self.name,self.age,self.sex,self.hobby)
# #
# # class Game_Player(Peolpe):
# #     def __init__(self,name,age,sex,hobby,hp):
# #         Super().__init__()
# #         self.hp=hp
# #
# # player=Game_Player('xiaolan',12,'male','basketball',1000)
# # player.introduce()
#
# import jieba
#
#
#
#
# def open_file() :
#     filename = 'lagou_job_java.txt'
#     f = open(filename,'rb')
#     file_list = f.readlines()
#     f.close()
#     return file_list
#
# def list_encode(file_list):
#     line_container=[]
#     for i in file_list:
#         each_line=i.decode('utf-8')
#         line=each_line.split()
#
#
#         line_container.append(line)
#
#     return line_container
#
#
# def process(line_container):
#     tf={}
#     for line_list in line_container:
#         for strings in line_list:
#
#             seg_list = jieba.cut(strings,cut_all=False)
#             for word in seg_list:
#                 if word in tf:
#                     tf[word]+=1
#                 else:
#                     tf[word]=1
#     return tf
#     #
#     # tf={}
#     # for seg in seg_list :
#     #     #print seg
#     #     seg = ''.join(seg.split())
#     #     if (seg != '' and seg != "\n" and seg != "\n\n") :
#     #         if seg in tf :
#     #             tf[seg] += 1
#     #         else :
#     #             tf[seg] = 1
#     #
#     # f = open("result.txt","w+")
#     # for item in tf:
#     #     #print item
#     #     f.write(item+"  "+str(tf[item])+"\n")
#     # f.close()
#
# def select_sort(lists):
#     count=len(lists)
#     for i in range(0,count):
#         min=1
#         for j in range(i+1,count):
#             if lists[min]>list[j]:
#                 min=j
#             lists[min],lists[i]=lists[i],lists[min]
#     return lists
#
# if __name__ == '__main__' :
#     file=open_file()
#     bbt=list_encode(file)
#     result=process(bbt)
#     list_container=list(result.items())
#     container=[]
#     for i in list_container:
#
#         cover=[i[1],i[0]]
#         container.append(cover)
#
#     container_sort=sorted(container)
#
#
#
#     with open('result_java.txt','w+',encoding='utf-8') as file:
#         for item in container_sort:
#
#             file.write(item[1]+str(item[0])+'\n')

# import re
# import requests
# import http.cookiejar
# import time
# import json
#
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:48.0) Gecko/20100101 Firefox/48.0',
#            'Origin':'http://huaban.com',
#            "Referer": 'http://huaban.com/'}
# filename = 'cookie'
#
# # 建立一个会话，可以把同一用户的不同请求联系起来；直到会话结束都会自动处理cookies
# session = requests.Session()
# # 建立LWPCookieJar实例，可以存Set-Cookie3类型的文件。
# # 而MozillaCookieJar类是存为'/.txt'格式的文件
# session.cookies = http.cookiejar.LWPCookieJar(filename)
# # 若本地有cookie则不用再post数据了
# try:
#     # 参数ignore_discard=True表示即使cookies将被丢弃也把它保存下来
#     # 它还有另外一个参数igonre_expires表示当前数据覆盖（overwritten）原文件
#     session.cookies.load(filename=filename, ignore_discard=True)
# except:
#     print('Cookie未加载！')
#
# def login(username, password):
#     """
#     输入自己的账号密码，模拟登录bilibili
#     """
#     # 检测到11位数字则是手机登录
#     if re.match(r'\d{11}$', account):
#         print('使用手机登录中...')
#         url = 'https://huaban.com/auth/'
#         data = {'_ref':'frame',
#                 'email': account,
#                 'password':password,
#
#                 }
#     else:
#         print('使用邮箱登录中...')
#         data = {'_ref': 'frame',
#                 'email': account,
#                 'password': password,
#
#                 }
#     # 若不用验证码，直接登录
#     try:
#         result = session.post(url, data=data, headers=headers)
#         # print((result.text))
#     # 要用验证码，post后登录
#     except:
#         print('登入失败')
#         result = session.post(url, data=data, headers=headers)
#         # print((result.text))
#     # 保存cookie到本地
#     session.cookies.save(ignore_discard=True, ignore_expires=True)
#
# if __name__ == '__main__':
#     account = input('输入账号：')
#     secret = input("输入密码：")
#     login(account, secret)
#     # 设置里面的简介页面，登录后才能查看。以此来验证确实登录成功
#     get_url = 'http://huaban.com/'
#     # allow_redirects=False 禁止重定向
#     resp = session.get(get_url, headers=headers, allow_redirects=False)
#     print(resp.text)
#
# import requests
# import re
# import os
# import os.path
#
# class HuabanCrawler():
#     """ 抓去花瓣网上的图片 """
#
#     def __init__(self):
#         """ 在当前文件夹下新建images文件夹存放抓取的图片 """
#         self.homeUrl='http://huaban.com/favorite/illustration/'
#         # self.homeUrl = "http://huaban.com/favorite/beauty/"
#         self.images = []
#         if not os.path.exists('./images'):
#             os.mkdir('./images')
#
#     def __load_homePage(self):
#         """ 加载主页面 """
#         return requests.get(url = self.homeUrl).text
#
#     def __make_ajax_url(self, No):
#         """ 返回ajax请求的url """
#         return self.homeUrl + "?i5p998kw&max=" + No + "&limit=20&wfl=1"
#
#     def __load_more(self, maxNo):
#         """ 刷新页面 """
#         return requests.get(url = self.__make_ajax_url(maxNo)).text
#
#     def __process_data(self, htmlPage):
#         """ 从html页面中提取图片的信息 """
#         prog = re.compile(r'app\.page\["pins"\].*')
#         appPins = prog.findall(htmlPage)
#         # 将js中的null定义为Python中的None
#         null = None
#         true = True
#         if appPins == []:
#             return None
#         result = eval(appPins[0][19:-1])
#         for i in result:
#             info = {}
#             info['id'] = str(i['pin_id'])
#             info['url'] = "http://img.hb.aicdn.com/" + i["file"]["key"] + "_fw658"
#             if 'image' == i["file"]["type"][:5]:
#                 info['type'] = i["file"]["type"][6:]
#             else:
#                 info['type'] = 'NoName'
#             self.images.append(info)
#
#     def __save_image(self, imageName, content):
#         """ 保存图片 """
#         with open(imageName, 'wb') as fp:
#             fp.write(content)
#
#     def get_image_info(self, num=20):
#         """ 得到图片信息 """
#         self.__process_data(self.__load_homePage())
#         for i in range((num-1)//20):
#             self.__process_data(self.__load_more(self.images[-1]['id']))
#         return self.images
#
#     def down_images(self):
#         """ 下载图片 """
#         print("{} image will be download".format(len(self.images)))
#         for key, image in enumerate(self.images):
#             print ('download {0} ...'.format(key))
#             try:
#                 req = requests.get(image["url"])
#             except :
#                 print('error')
#             imageName = os.path.join("./images", image["id"] + "." + image["type"])
#             self.__save_image(imageName, req.content)
#
#
# if __name__ == '__main__':
#     hc = HuabanCrawler()
#     hc.get_image_info(1000)
#     hc.down_images()
# import os
# strs='SSPD-124 原作:御堂 乱 女教師 テニス部・奴隷合宿'
# title_deal = ''.join(strs.split(':'))
# print(title_deal)
# os.mkdir(title_deal)

# import threading
# import logging
#
#
# def get_logger():
#     logger=logging.getLogger('threading_example')
#     logger.setLevel(logging.DEBUG)
#
#     fh=logging.FileHandler('threading.log')
#     fmt='%(asctime)s-%(threadName)s-%(levelname)s-%(message)s'
#     formatter=logging.Formatter(fmt)
#     fh.setFormatter(formatter)
#
#     logger.addHandler(fh)
#     return  logger
#
#
# def doubler(number,logger):
#     """可被线程使用的函数
#     """
#     # print(threading.currentThread().getName()+'\n')
#     # print(threading.current_thread().getName()+'\n')
#
#     logger.debug('doubler function exexuting')
#     result=number*2
#     logger.debug('doubler function ended with:{}'.format(result))
#
#     # print(number*2)
#     # print()
#
#
# if __name__=='__main__':
#     logger=get_logger()
#     thread_name=['xiao','mei','qian','hai','ming']
#     for i in range(5):
#         my_thread=threading.Thread(target=doubler,name=thread_name[i],args=(i,logger))
#         my_thread.start()
#
# import threading
#
# total=15
#
# def update_total(amount):
#     global total
#     total+=amount
#     print(total)
#
# if __name__=='__main__':
#     for i in range(10):
#         my_thread=threading.Thread(target=update_total,args=(5,))
#         my_thread.start()


# -*- coding: utf-8 -*-
# 2016/9/18 13:55
# """
# -------------------------------------------------------------------------------
# Function:   将网上的版本修改为2.x
# Version:    1.0
# Author:     SLY
# Contact:    slysly759@gmail.com
#
# -------------------------------------------------------------------------------
# """
# # ! /usr/bin/python3
# # _encoding:utf-8_
# # Written by liuzhaoyang
#
# # 下载花瓣网的素材
# # 功能
# # 1.查询关键词
# # 2.自定义下载张数
#
# import re
# import os
# import requests
# from time import sleep, time
# from random import choice
# from multiprocessing.dummy import Pool as ThreadPool
#
# # 这个多线程就让我帮你加上去吧
#
# page_count = 1
# photo_number = 0
# down_data = []
#
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
# user_agent = choice(UserAgent)
# head = {'User-Agent': user_agent}
# TimeOut = 30
#
#
# # 这个user-agent池以后可以考虑借用
#
#
# def downfile(down_data):
#     print("开始下载：", down_data[2])
#
#     # 处理传传进来的参数
#     # 文件名有的不符合规范，所以要处理
#     name_string=down_data[0]
#     # name=[''.join(i) for i in name_list if i in '?、\*" <>|']
#     # 还没有解决文件名过滤问题
#     # for i in ['?', '、', '\\', '*', '\"', '<', '>', '|']:
#     #     name_string = name_string.strip(i)
#     # print(name_string)
#     try:
#         resource = requests.get(down_data[1], stream=True, headers=head).content
#         with open(name_string+'.jpg', 'wb') as file:
#             file.write(resource)
#     except Exception as e:
#         # print("下载失败", e)
#         with open(down_data[2]+ '.jpg', 'wb') as file:
#             file.write(resource)
#
#
# def request_page_text(url):
#     try:
#         Page = requests.session().get(url, headers=head, timeout=TimeOut)
#         Page.encoding = 'utf-8'
#         return Page.text
#     except Exception as e:
#         print("请求失败了...重试中(5s)", e)
#         sleep(5)
#         print("暂停结束")
#         request_page_text(url)
#
#
# def request_url_download(url):
#     # print(url)
#
#     global photo_number
#     text = request_page_text(url)
#     pattern = re.compile('{"pin_id":(\d*?),.*?"key":"(.*?)",.*?"raw_text":"(.*?)",.*?"like_count":(\d*?),.*?"repin_count":(\d*?),.*?"username":"(.*?)".*?}', re.S)
#     # 参数re.S 是正则表达式，编译参数标识re.DOTALL，即.匹配除、\n 所有字符
#     '''
#     这个正则表达式有点吊，学的不错.
#     但是由于传输的是一个很规范，如果是我，我会考虑正则然后eval直接用.这里就懒得写了
#     效率上并没有进行统计
#     '''
#     img_query_items = re.findall(pattern, text)
#     max_pin_id = 0
#     # print(img_query_items)
#
#     for url_items in img_query_items:
#         max_pin_id = url_items[0]
#         x_key = url_items[1]
#         # 图片标题
#         x_file_title=url_items[2]
#         x_like_count = int(url_items[3])
#         x_repin_count = int(url_items[4])
#         # 图片收集地址
#         x_author=url_items[5]
#
#         # 这里是判断图片的热度
#         # if (x_repin_count > 10 and x_like_count > 10) or x_repin_count > 100 or x_like_count > 20:#暂时不要
#         print("开始下载第{0}张图片".format(photo_number))
#         url_item = url_image + x_key
#         # filename = down_dir + str(max_pin_id) + ".jpg"
#         # 修改文件名为网页上真实标题
#         filename=x_file_title
#         if os.path.isfile(filename):
#             print("文件存在：", filename)
#             continue
#         if photo_number >= image_numbers:
#             # 结束函数
#             return
#         down_data.append([filename, url_item,str(max_pin_id)])
#         # downfile(filename, url_item)
#         photo_number += 1
#
#     global page_count
#     page_count += 1
#     print('获取第%s链接成功' % page_count)
#     request_url_download(url_query + str(page_count))
#
#     return down_data
#
#
# if __name__ == '__main__':
#     start_time = time()
#     url_image = 'http://hbimg.b0.upaiyun.com/'
#     query_string = input('请输入要查询的关键词：')
#     # url = "http://huaban.com/search/?q="+query_string
#     global image_numbers
#     image_numbers = int(input('下载多少张：'))
#     down_dir = query_string
#     url_query = "http://huaban.com/search/?q=" + query_string + "&per_page=20&wfl=1&page="
#     if not os.path.exists(down_dir):
#         os.makedirs(down_dir)
#         os.chdir(down_dir)
#     else:
#         os.chdir(down_dir)
#     image_info_urls = request_url_download(url_query + str(page_count))
#     print(image_info_urls)
#     # input('.....')
#     # 开启线程池
#     pool = ThreadPool(4)
#     result=pool.map(downfile, image_info_urls)
#     pool.close()
#     pool.join()
#     # for i in image_info_urls:
#     #     downfile(i)
#     end_time = time()
#     print('共下载%s张素材，耗时%.2fs' % (image_numbers, end_time - start_time))

#
# import pymysql
#
#
# connection=pymysql.connect(host="localhost",
#                            port=3306,user='root'
#                            ,password='root'
#                            ,db='test'
#                            ,cursorclass=pymysql.cursors.DictCursor)
# cursor=connection.cursor()
#
# connection.set_charset('utf8')
# cursor.execute('SET NAMES utf8;')
# cursor.execute('SET CHARACTER SET utf8;')
# cursor.execute('SET character_set_connection=utf8;')
# sql0="create table users (email CHAR (20),password CHAR (20))"
#
# cursor.execute(sql0)
# connection.commit()
# sql="insert into users (email,password) values ('575563079@qq.com','730089615')"
#
# cursor.execute(sql)
# connection.commit()
#
#
# sql2="SELECT 'id','password' FROM  users  WHERE 'email'='575563079@qq.com'"
# cursor.execute(sql2)
# connection.commit()
#
#
# connection.close()
#
# for i in cursor:
#     print(i)
#
# s='美女'
# print(repr(s))
# print(s.encode(encoding='utf-8').decode('ascii'))

# import tornado.ioloop
# import tornado.web
#
# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write("Hello, 你好")
#
# def make_app():
#     return tornado.web.Application([
#         (r"/*", MainHandler),
#     ])
#
# if __name__ == "__main__":
#     app = make_app()
#     app.listen(8000)
#     tornado.ioloop.IOLoop.current().start()

# import asyncio
#
# @asyncio.coroutine
# def wget(host):
#     print('wget %s...' % host)
#     connect = asyncio.open_connection(host, 80)
#     reader, writer = yield from connect
#     header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     yield from writer.drain()
#     while True:
#         line = yield from reader.readline()
#         if line == b'\r\n':
#             break
#         print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
#     # Ignore the body, close the socket
#     writer.close()
#
# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()


# def produce(c):
#     c.send(None)
#     n=0
#     while n<5:
#         n=n+1
#         print('producing %s' % n)
#         r=c.send(n)
#         print('consumer return:%s' % r)
#     c.close()
#
# def consumer():
#     r=''
#     while True:
#         n=yield  r
#         if not n:
#             return
#         print('consuming: %s' % n)
#         r='200ok'
#
# c=consumer()
# produce(c)
#
# import asyncio
#
# # Borrowed from http://curio.readthedocs.org/en/latest/tutorial.html.
# @asyncio.coroutine
# def countdown(number, n):
#     while n > 0:
#         print('T-minus', n, '({})'.format(number))
#         yield from asyncio.sleep(1)
#         n -= 1
#
# loop = asyncio.get_event_loop()
# tasks = [
#     asyncio.ensure_future(countdown("A", 2)),
#     asyncio.ensure_future(countdown("B", 3))]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()


# tornado框架尝试
# import tornado.ioloop
# import tornado.web
#
# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write("Hello, world")
#
# def make_app():
#     return tornado.web.Application([
#         (r"/", MainHandler),
#     ])
#
# if __name__ == "__main__":
#     app = make_app()
#     app.listen(8888)
#     tornado.ioloop.IOLoop.current().st

# import urllib.parse
#
# string="你好"
# ss=urllib.parse.quote(string)
# print(ss)
# import time
# 导入所需的模块
# from bs4 import BeautifulSoup
# import re
#
# # 一段html的字符串
# html_doc = """
# <html>
#     <head>
#         <title>The Dormouse's story </title>
#     </head>
# <body>
# <p class="story">Once upon a time where three little sisters; and their names were>
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
# <a href="http//example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
#
# <p class="stroy">...</p>
#
# """
#
# # 创建beautifulSopu对象
# soup = BeautifulSoup(html_doc, 'html.parser')
#
# # 查找html中出现的所有链接
# print("获取所有链接：")
#
# links = soup.find_all('a')
# for link in links:
#     print(link.name, link['href'], link.get_text())
#
#
# # 查找html文件中lacie的链接
# print
# '获取lacie的链接'
# link_node = soup.find('a', href="http://example.com/lacie")
# http//example.com/lacie
# print(link_node.name, link_node.get_text())
#
#
# # 利用正则表达式进行模糊匹配
# print('正则模糊匹配:')
#
# link_node = soup.find_all('a', href=re.compile(r"ill"))
# print(link_node.name, link_node['href'], link_node.get_text())
#
#
# # 获取标题的文字
# print('获取p段落文字')
# link_node = soup.find('p', class__='title')
#
# print(link_node.name, link_node['href'], link_node.get_text())

# import string,os
# strings=string.printable
# blist=[1,52,8,7]
# the_byte=bytes("hello".encode())
# print(the_byte)
# blist1='[1,52,8,7]'
# print([blist1.encode()[i] for i in range(len(blist1.encode()))])
# print(the_byte)
# print(len(strings))
# poem="heoooejloooascs sadsa sdas"
# file=open('xxx.txt','r')
# file.seek(15)

# new_file=file.readlines()
# print(file.tell())

# file.close()
# print(new_file)

# import csv
# validate=[["name","xiaoqian"],["age",12],["height",123]]
# with open('validate','w') as file:
# 	csvout=csv.writer(file)
# 	csvout.writerows(validate)
# with open('validate','r') as files:
# 	csvout=csv.reader(files)
# 	[print(i) for i in csvout if i]
# 	# for i in csvout:
# 	# 	print(i)

# rrr=csv.reader(file('validate','r'))
# for i in rrr:
# 	print(i)

# import ElementTree

# letters=['I','L','o','v','e','y','o','u']
# [print(i.join(letters)) for i in letters]
# print(if(False=True):return "yes")

# import pickle
# strings="i love xiaoqian"
# pickled=pickle.dumps(strings)
# print(pickled)
# pickle_to_str=pickle.loads(pickled)
# print(pickle_to_str)
#
# data=dict(name='xiaoqian',age=12)
# tall=data.get('xiaoqian',132)
# print(tall)
# print(data)


# from flask import Flask, request, session, redirect, url_for
#
# app = Flask(__name__)
# app.secret_key = "A0Zr98j/3yX R~XHH!jmN]LWX/,?RT"
#
#
# @app.route('/')
# def v_inbox():
#     if 'username' in session:
#         return "<h1>%s\mailbox</h1>" % session['username']
#     else:
#         return 'not authorized go to login<a href="%s">here</a> to authorize yourself' % url_for('v_auth')
#
#
# @app.route('/login', methods=['POST', 'GET'])
# def v_auth():
#     if request.method == "GET":
#         return '''
#                 <form action="%s" method="POST">
#                     <input type="text" name="username" placeholder="input your username">
#                     <input type="password" name="password" placeholder="input your password">
#                     <input type="submit" value="submit">
#                 </form>
#                 ''' % url_for('v_auth')
#
#
#     if request.method == "POST":
#         session['username'] = request.form['username']
#         return 'authorized! go to inbox<a href="%s">here</a> to check mail' % url_for('v_inbox')
#
# app.run(host='0.0.0.0', port=8000)


from wsgiref.simple_server import make_server

class WSGI_APP:
    def __call__(self,environ,start_response):
        start_response('200 OK',[('Context-Type','text/plain')])
        return 'such a tiny wsgi app!'

app = WSGI_APP()
httpd = make_server('0.0.0.0',8000,app)
print('start server')
httpd.serve_forever()

