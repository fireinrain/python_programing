#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang

import os
import re
import ctypes
import platform
import time

# 获取系统盘符号
def get_driver_name():

    if platform.system()=='Windows':
        #获取系统盘符，只能win下使用
        lpBuffer = ctypes.create_string_buffer(78)
        ctypes.windll.kernel32.GetLogicalDriveStringsA(ctypes.sizeof(lpBuffer), lpBuffer)
        vol = lpBuffer.raw.split('\x00'.encode())
        drive_list_raw=list(i.decode('utf-8') for i in vol)

        space=drive_list_raw.index('')
        # print(space)
        drive_list_raw=drive_list_raw[:space]
        drive_list=[]
        for i in drive_list_raw:
            if os.path.isdir(i):
                drive_list.append(i)

        # print(drive_list)
    else:

        # 第二种方法是遍历字母，拼接为dir，判断是否是dir
        drive_list=[]
        for i in range(65,91):
            vol = chr(i) + ':'
            if os.path.isdir(vol):
                drive_list.append(vol)
    return drive_list

# 匹配视频文件并返回一个视频列表
def walk_file(dirs):
    movie_format=('MP4','mp4','rm','RM','avi','AVI','iso','ISO','wmv','WMV','mkv','MKV','mov','MOV')
    target=[]
    end=[]
    for (this_dir,current_dir_dirs,file_here) in os.walk(dirs):
        for file_name in file_here:

            target.append(file_name)
    # print(target)
    movies=[]
    for movie in target:

        name_end = movie.split('.',20)[-1]

        if name_end in movie_format:
            end.append(name_end)
            movies.append(movie)
        # print(movie+'____'+name_end)
    print('找到' + str(len(movies)) + '个视频  ', end='')
    return movies
# 对视频列表进行过滤，找出有番号的小视频
def fetch_number(target):
    patter=re.compile('^\w{3,4}-?\d{3}|^\w{2}-?\d{4}')
    cant_match=[]
    get_match=[]
    for i in target:
        try:
            result=re.search(patter,i)
            fanhao=result.group()
            get_match.append(fanhao+i)
        except Exception as e:
            # print(i+'无法完成匹配')
            cant_match.append(i)
            continue
    print('找到'+str(len(get_match))+'个含有番号的视频  ',end='')
    print('找到'+str(len(cant_match))+'个没有番号的视频',end='')
    return [get_match,cant_match]
def main():
    while True:
        time_start=time.time()
        ways_choise=input('A(全盘扫描),S(自定义模式)[接受小写]：')
        if ways_choise in 'Aa':
            driver_list=get_driver_name()
            for driver in driver_list:
                movie_list=walk_file(driver)
                result=fetch_number(movie_list)
        elif ways_choise in 'Ss':
            driver=input('请输入路径(如k:\)')
            movie_list = walk_file(driver)
            result = fetch_number(movie_list)
            print(result[0])
        time_end=time.time()

        print('共耗时：'+str(time_end-time_start)+'秒')

if __name__=='__main__':
    main()