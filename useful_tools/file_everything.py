#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang

# 本脚本是实现查找有关文件名的脚本
# 返回一个文本，包含查找到的文件数和文件的具体路径和大小
# 有两个模式来选择，全盘或是指定路径
"""
ctypes用来获取系统盘符
"""


import ctypes
import os
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


# 遍历文件目录，返回查找到的文件列表
def walk_file(dirs,file_type=None):
    visited={}
    target=[]
    for (this_dir,current_dir_dirs,file_here) in os.walk(dirs):
        # print(current_dir_dirs)
        this_dir=os.path.normpath(this_dir)
        # print(this_dir)
        # fixcase_this_dir=os.path.normcase(this_dir)
        # print(fixcase_this_dir)
        # if fixcase_this_dir in visited:
        #     continue
        # else:
        #     visited[fixcase_this_dir]=True
        for file_name in file_here:
            if file_type in file_name:
                file_path = os.path.join(this_dir,file_name)
                file_size = os.path.getsize(file_path)
                file_size = file_size/(1024**2)
                target.append([file_size,file_path])
    # print(target)
    return target


# 对列表进行排序
def biggist_file(*target):
    big_list=sorted(target)
    return big_list

# 对结果写入文件
def write_to_file(small_to_big,biggist):
    with open('file.txt','w',encoding='utf-8') as file:
        number = len(small_to_big)
        big=biggist[1]
        size=biggist[0]
        file.write('----------共找到%d个结果-------\n' % number)
        file.write('-------->最大文件为：%s==%.2f MB\n' % (big,size))
        for item in small_to_big:
            line=item[1]+'--->'+str(item[0])+'MB'
            file.write(line+'\n')
            # print(line)
        print('查找完成')


# 全盘结果写入文件
def write_all_to_file(small_to_big,biggist,dir):
    with open('all_file.txt','a+',encoding='utf-8') as file:
        number = len(small_to_big)
        big=biggist[1]
        size=biggist[0]
        file.write('-----扫描%s结果-----' % dir)
        file.write('----------共找到%d个结果-------\n' % number)
        file.write('-------->最大文件为：%s==%.2f MB\n' % (big,size))
        for item in small_to_big:
            line=item[1]+'--->'+str(item[0])+'MB'
            file.write(line+'\n')
            # print(line)
        print('查找完成'+dir)
        return number


def main():
    while True:
        patter=input('请选择查询模式：（A：全盘），（S：自定义），（C,退出）')
        if patter in'Cc':
            break
        else:

            if patter in 'Aa':
                file_type = input("请输入要搜索的文件相关符号：")
                dirs=get_driver_name()
                time_start = time.time()
                counts = 0
                for dir in dirs:
                    target = walk_file(dir, file_type)
                    aim_list = biggist_file(target)

                    # 将文件按照从大到小排列
                    small_to_big = sorted(aim_list[0])
                    if small_to_big:
                        # print(small_to_big)
                        # 获取最大文件
                        biggist = small_to_big[-1]
                        # 获取文件数
                        # number=len(aim_list)

                        number_file=write_all_to_file(small_to_big, biggist,dir)
                        counts+=number_file
                    else:
                        continue
                time_end = time.time()
                print('总共耗时：%.2f ,找到文件数:%d' % (time_end-time_start,counts))

            elif patter in 'Ss':
                dir=input('请输入要查询的路径：')
                file_type = input("请输入要搜索的文件相关符号：")
                time_start=time.time()
                target = walk_file(dir, file_type)
                # aim_list=biggist_file(target)[-1][0]
                aim_list=biggist_file(target)
                # 将文件按照从大到小排列
                small_to_big=sorted(aim_list[0])
                # 获取最大文件
                biggist=small_to_big[-1]
                # 获取文件数
                number=len(small_to_big)
                write_to_file(small_to_big,biggist)
                time_end=time.time()
                print('总共耗时：%.2f ,找到文件数：%d' % (time_end - time_start,number))


if __name__=='__main__':
    main()