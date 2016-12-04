#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com

import curses
from random import randrange,choice
from collections import defaultdict

# 用户操作行为
actions = ['Up','Left','Down','Right','Restart','Exit']

# 获取有效按键的asicc值
letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']

# 将用户按键行为与相应的值关联
actions_dict = dict(zip(letter_codes,actions*2))
print(actions_dict)
