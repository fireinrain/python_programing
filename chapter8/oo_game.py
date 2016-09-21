#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com

# import random
#
# class Animal:
#     step=[-2,-3,+2,+3]
#
#     def __init__(self,gm,point=None):
#         self.gm=gm
#         if point is None:
#             self.point=random.randint(0,20)
#         else:
#             self.point=point
#
#     def jump(self):
#         random_step=random.choice(Animal.step)
#         if 0<=self.point+random_step<=20:
#             self.point+=random_step
#
# class Ant(Animal):
#     def __init__(self,gm,point=None):
#         super().__init__(gm,point)
#         self.gm.set_point('ant',self.point)
#
#     def jump(self):
#         super().jump()
#         self.gm.set_point('ant', self.point)
#
# class Worm(Animal):
#     def __init__(self,gm,point=None):
#         super().__init__(gm,point)
#         self.gm.set_point('worm',self.point)
#
#     def jump(self):
#         super().jump()
#         self.gm.set_point('worm', self.point)

# class Box:
#     obj_num=0
#     def __init__(self,height,length,width):
#         self.height=height
#         self.length=length
#         self.width=width
#         Box.obj_num+=1
#     def get_k(self):
#         return Box.obj_num
#     def list_att(self):
#         return self.__dict__
# box1=Box(1,2,3)
# box2=Box(1,2,3)
# box3=Box(1,2,3)
# box4=Box(1,2,3)
# box5=Box(1,2,3)
# box6=Box(1,2,3)
# print(box1.get_k())
# print(box1.list_att())


