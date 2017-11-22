#!/usr/bin/python
# -*- coding:utf-8 -*-
#
# x=1        #x=int(1)
# #id #type #value
# print(id(x))   #身份
# print(type(x)) #类型
# print(x)       #值
# #
#is  身份运算
x=300
y=300
print(x is y)
#==   判断的值
print(x == y)
#
#
class Chinese:
    country = 'China'
    def __init__(self,name,age):
        # print('====>')
        self.name=name #p1.name='egon'
        self.age=age #p1.age=18

    def talk(self):
        print('say chinese',self)

#
# #类的第一种用法：实例化
# p1=Chinese('egon',18) #__init__(p1,'egon',18)
#
#
# #类的第二种用法：属性引用（增删改查）
# # print(Chinese.country) #类的数据属性
# # print(Chinese.__init__) #类的函数属性
# # Chinese.__init__(1,2,3) #1.name=2
#
# # print(Chinese.__dict__) #查看类的属性字典，或者说名称空间
#
# # print(Chinese.country)
# # print(Chinese.__dict__['country'])
#
#
#
#
# #对象
# p1=Chinese('egon',18) #__init__(p1,'egon',18)
# #
# # print(p1.name)
# # print(p1.age)
# #
# #
# # print(p1.__dict__)
# # print(p1.__dict__['name'])
#
#
# #类型与类是统一的
# # print(type(p1))
#
#
# p1=Chinese('egon',18) #__init__(p1,'egon',18)
# p2=Chinese('alex',1000) #__init__(p1,'egon',18)
# # print(id(p1.country))
# # print(id(p2.country))
# # print(id(Chinese.country))
# #
# # print(Chinese.talk)
# # print(p1.talk)
# # print(p2.talk)
#
# # print(p1)
# # p1.talk()
# # print(p2)
# # p2.talk()
# Chinese.talk(p1)
#
#
#定义在类内部的变量，是所有对象共有的，id全一样
#定义在类内部的函数，是绑定到所有对象的，是给对象来用，obj.func() 会把obj本身当做第一个参数出入

#绑定方法：绑定到谁身上，就是给谁用的，谁来调用就会自动把自己当做第一个参数传入
#
#
#
# print(p1.x) #先从p1.__dict__,找不到再找Chinese.__dict__,找不到就会报错