#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang

"""
虫蚁赛跑
"""
import random

ant_point=random.randint(0,20)
worm_point=random.randint(0,20)
print('ant_point:',ant_point,'worm_point:',worm_point)

step=[-2,+2,-3,+3]

while ant_point != worm_point:
    ant_step=random.choice(step)
    if 0<=ant_point+ant_step<=20:
        ant_point+=ant_step

    worm_step=random.choice(step)
    if 0<=worm_point+worm_step<=20:
        worm_point+=worm_step
    print('ant_point:', ant_point, 'worm_point:', worm_point)