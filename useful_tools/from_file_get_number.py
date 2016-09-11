#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang

import os
import re

# 匹配视频文件并返回一个视频列表
def walk_file(dirs):
    movie_format=('MP4','mp4','rm','RM','avi','AVI','iso','ISO','wmv','WMV','mkv','MKV','mov')
    target=[]
    end=[]
    for (this_dir,current_dir_dirs,file_here) in os.walk(dirs):
        for file_name in file_here:

            target.append(file_name)
    # print(target)
    for movie in target:

        name_end = movie.split('.')[1]

        if name_end in movie_format:
            end.append(name_end)
        print(movie+'---'+name_end)
    return end
# 对视频列表进行过滤，找出有番号的小视频
def fetch_number(target):
    patter=re.compile('\w{3,4}-?\d{3}|\w{2}-?\d{4}')
    for i in target:
        try:
            result=re.search(patter,i)
            # print(result.group()+'--'+i)
        except Exception as e:
            print(i+'无法完成匹配')
            continue
def main():
    dir=input('请输入路径：')
    name_list=walk_file(dir)
    print(len(name_list))
    # fetch_number(name_list)

if __name__=='__main__':
    main()