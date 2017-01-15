#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com
import zipfile
with zipfile.ZipFile('new.zip','r') as f:
    f_names = f.namelist()
    for name in f_names:
        try:
            data = f.read(name)
            with open(name,'wb') as child_f:
                child_f.write(data)
        except KeyError:
            print("error")