#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang


class Orange:
    def __init__(self,weight,orchard,date_picked):
        self.weight=weight
        self.orchard=orchard
        self.date_picked=date_picked
        self.place='Basket'




class Apple:
    def __init__(self,color,weight):
        self.color=color
        self.weight=weight


class Basket:
    def __init__(self,location):
        self.location=location
        self.container='Orange'


class Barrel:
    def __init__(self,size):
        self.size=size