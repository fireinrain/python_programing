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

def main(stdscr):

    def init():
        # 重置棋盘
        return 'Game'

    def not_game(state):
        #画出gameover或是win的界面
        #读取用户输入得到action，判断是重启游戏还是结束游戏
        responses = defaultdict(lambda:state) #默认是当前状态，没有行为则会停在当前状态
        responses['Restart'],responses['Exit'] = 'Init','Exit'

    def game():
        #画出当前棋盘的状态
        #读取用户的输入得到action
        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'
        #if 成功移动一步
            if 游戏胜利:
                return 'win'
            if 游戏失败:
                return 'Gameover'
    state_actions = {
        'Init':init,
        'Win':lambda :not_game('Win'),
        'Gameover':lambda :not_game('Gameover'),
        'Game':game
    }
    state = 'Init'

    # 状态机开始循环
    while True:



