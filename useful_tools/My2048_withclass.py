#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com

# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 14:15:39 2014

@author: kelvin
"""

import random


class game2048:
    totalScore = 0
    v = [[2, 8, 8, 2],
         [4, 2, 4, 8],
         [2, 4, 2, 0],
         [4, 2, 4, 0]]
    '''
    v = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]
    '''

    def __init__(self):
        for i in range(4):
            self.v[i] = [random.choice([0, 0, 0, 2, 2, 4]) for x in range(4)]

    def display(self):
        print('{0:4} {1:4} {2:4} {3:4}'.format(self.v[0][0], self.v[0][1], self.v[0][2], self.v[0][3]))
        print('{0:4} {1:4} {2:4} {3:4}'.format(self.v[1][0], self.v[1][1], self.v[1][2], self.v[1][3]))
        print('{0:4} {1:4} {2:4} {3:4}'.format(self.v[2][0], self.v[2][1], self.v[2][2], self.v[2][3]))
        print('{0:4} {1:4} {2:4} {3:4}'.format(self.v[3][0], self.v[3][1], self.v[3][2], self.v[3][3]))
        print('得分为:{0:4}'.format(self.totalScore))
        print('游戏是否结束:{0:4}'.format(self.isOver()))

    # 重新排列
    def align(self, vList, direction):
        for i in range(vList.count(0)):
            vList.remove(0)
        zeros = [0 for x in range(4 - len(vList))]
        if direction == 'left':
            vList.extend(zeros)
        else:
            vList[:0] = zeros

    # 将相同的元素相加，返回新增积分
    def addSame(self, vList, direction):
        increment = 0
        if direction == 'left':
            for i in [0, 1, 2]:
                if vList[i] == vList[i + 1] and vList[i + 1] != 0:
                    vList[i] *= 2
                    vList[i + 1] = 0
                    increment += vList[i]
        else:
            for i in [3, 2, 1]:
                if vList[i] == vList[i - 1] and vList[i - 1] != 0:
                    vList[i] *= 2
                    vList[i - 1] = 0
                    increment += vList[i]
        return increment

    # 处理行和方向,返回新增积分
    def handle(self, vList, direction):
        self.align(vList, direction)
        increment = self.addSame(vList, direction)
        self.align(vList, direction)
        self.totalScore += increment  # 直接加到总值
        return increment

    # 判断游戏是否结束
    def judge(self):

        if self.isOver():
            print('你输了，游戏结束!')
            return False
        else:
            if self.totalScore >= 2048:
                print('你赢了，游戏结束！但是你还可以继续玩。')
            return True

    # 判断游戏是否真正结束
    def isOver(self):
        N = self.calcCharNumber(0)
        if N != 0:
            return False
        else:
            for row in range(4):
                flag = self.isListOver(self.v[row])
                if flag == False:
                    return False
            for col in range(4):
                # 将矩阵中一列复制到一个列表中然后处理
                vList = [self.v[row][col] for row in range(4)]
                flag = self.isListOver(vList)
                if flag == False:
                    return False
        return True

    # 判断一个列表是否还可以合并
    def isListOver(self, vList):
        for i in [0, 1, 2]:
            if vList[i] == vList[i + 1] and vList[i + 1] != 0:
                return False
        return True

    def calcCharNumber(self, char):
        n = 0
        for q in self.v:
            n += q.count(char)
        return n

    def addElement(self):
        # 统计空白区域数目 N
        N = self.calcCharNumber(0)
        if N != 0:
            # 按2和4出现的几率为3/1来产生随机数2和4
            num = random.choice([2, 2, 2, 4])
            # 产生随机数k，上一步产生的2或4将被填到第k个空白区域
            k = random.randrange(1, N + 1)  # k的范围为[1,N]
            n = 0
            for i in range(4):
                for j in range(4):
                    if self.v[i][j] == 0:
                        n += 1
                        if n == k:
                            self.v[i][j] = num
                            return

    def moveLeft(self):
        self.moveHorizontal('left')

    def moveRight(self):
        self.moveHorizontal('right')

    def moveHorizontal(self, direction):
        for row in range(4):
            self.handle(self.v[row], direction)

    def moveUp(self):
        self.moveVertical('left')

    def moveDown(self):
        self.moveVertical('right')

    def moveVertical(self, direction):
        for col in range(4):
            # 将矩阵中一列复制到一个列表中然后处理
            vList = [self.v[row][col] for row in range(4)]
            self.handle(vList, direction)
            # 从处理后的列表中的数字覆盖原来矩阵中的值
            for row in range(4):
                self.v[row][col] = vList[row]

    # 主要的处理函数
    def operation(self):
        op = input('operator:')
        if op in ['a', 'A']:  # 向左移动
            self.moveLeft()
            self.addElement()
        elif op in ['d', 'D']:  # 向右移动
            self.moveRight()
            self.addElement()
        elif op in ['w', 'W']:  # 向上移动
            self.moveUp()
            self.addElement()
        elif op in ['s', 'S']:  # 向下移动
            self.moveDown()
            self.addElement()
        else:
            print('错误的输入。请输入 [W, S, A, D] 或者是其小写')

            # 开始


print('输入：W(上移) S(下移) A(左移) D(右移), press <CR>.')
g = game2048()
flag = True
while True:
    g.display()
    flag = g.judge()
    g.operation()
    flag = g.judge()