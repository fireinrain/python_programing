#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com
import math

class MyFirstClass:
    pass

class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def reset(self):
        self.move(0,0)

    def move(self,x,y):
        self.x=x
        self.y=y

    def calculate_distance(self,other_point):
        return math.sqrt((self.x-other_point.x)**2+(self.y-other_point.y)**2)


class SecreteString:
    def __init__(self,plain_string,pass_string):
        self.__plain_string=plain_string
        self.__pass_string=pass_string

    def decrypt(self,pass_phrase):
        if pass_phrase==self.__pass_string:
            return self.__plain_string
        else:
            return

class ContactList(list):
    def search(self,name):
        """
        返回包含name的联系人
        :param name:
        :return:
        """
        matching_contacts=[]
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
            return matching_contacts


class Contact:
    all_contacts=ContactList()

    def __init__(self,name,email):
        self.name=name
        self.email=email
        self.all_contacts.append(self)

class Supplier(Contact):
    def order(self,order):
        print('if this is a real system we would send {0} order to{1}'.format(order,self.name))

class People:
    def __init__(self,name,age):
        self.name=name
        self.age=age


class LL(People):
    def __init__(self,name,age,email,addrs):
        super().__init__(name,age)
        self.email = email
        self.addrs = addrs

if __name__=='__main__':
    pass
    # people=MyFirstClass()
    # people.name='liuzhaoyang'
    # people.age='21'
    #
    # for i in people.__dir__():
    #     print(i)
    # print(str(people)+str(id(people)))

    # p1=Point()
    # p2=Point(2,3)
    #
    #
    # print(p1.calculate_distance(p2))

    # secret_string=SecreteString('heheh','nidaye')
    # print(secret_string.decrypt('nidaye'))
    # # print(secret_string.__plain_string)
    #
    # print(secret_string._SecreteString__plain_string)
    # def pp():
    #     a = 100
    #
    #     def change():
    #         nonlocal a
    #         a = 555
    #         print(a)
    #     change()
    #     print(a)
    # pp()

    # class A:
    #     pass
    #
    # class B:
    #     pass
    #
    # class C:
    #     pass
    #
    # class D(A,B):
    #     pass
    #
    # class E(B,C):
    #     pass
    #
    # class F(D,E):
    #     pass
    #
    # print(F.__mro__)





