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
#         self._color=None
#         self.situation=None
#         Box.obj_num+=1
#
#     def volume(self):
#         self.__volume=self.height*self.length*self.width
#         print(self.__volume)
#
#     def set_color(self,color):
#         self._color=color
#         print('设置颜色为：',self.color)
#
#     @property
#     def color(self):
#         return self._color
#
#     @color.setter
#     def color(self,color):
#         self._color=color
#
#     def get_color(self):
#         print('盒子颜色为：',self._color)
#
#     def open(self):
#         if self.situation=='closed' or self.situation==None:
#             self.situation='opend'
#         else:
#             print('不可以重复打开')
#
#     def close(self):
#         if self.situation=='opend' or self.situation==None:
#             self.situation='closed'
#         else:
#             print('不可以重复关闭')
#
#     def get_k(self):
#         return Box.obj_num
#
#     def list_att(self):
#         return self.__dict__
#
# class Number6:
#     def __init__(self):
#         pass
#
# if __name__=='__main__':
#     box1=Box(1,2,3)
#     box1.volume()
#     box1.set_color('yellow')
#     box1.get_color()
#     box1.open()
#     box1.close()
#     # box2=Box(1,2,3)
#     # box3=Box(1,2,3)
#     # box4=Box(1,2,3)
#     # box5=Box(1,2,3)
#     # box6=Box(1,2,3)
#     print(box1.get_k())
#     print(box1.list_att())

# class Washer:
#
#     def __init__(self,water=10,scour=5):
#         self._water=water
#         self.scour=scour
#     @property
#     def water(self):
#         return self._water
#     def set_water(self,water):
#         self.water=water
#
#     def set_scour(self,scour):
#         self.scour=scour
#
#     def add_water(self):
#         print('add water',self.water)
#
#
#     def add_scour(self):
#         print('add scour',self.scour)
#
#
#     def start_wash(self):
#         self.add_scour()
#         self.add_water()
#         print('start washing...')
#
# if __name__=='__main__':
#    w=Washer()
#    # w.set_scour(30)
#    # w.set_water(10)
#    print(w.water)
class Decor:
    def __init__(self, dec_class):
        self._dec_class = dec_class()

    def fun(self):
        print('开始装饰fun')
        self._dec_class.fun()

    def keep_fun(self):
        self._dec_class.keep_fun()

class Test:
    def fun(self):
        print('this is fun')

    def keep_fun(self):
        print('this is keep_fun')

if __name__=='__main__':
    a=Test()
    a.fun()