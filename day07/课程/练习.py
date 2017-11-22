#!/usr/bin/python
# # -*- coding:utf-8 -*-
#
# class Foo:
#     count=0     #调用方法：Cinese.count 或 sel.count
#     def __init__(self,name):
#         # count+=1       #不行，是全局的count
#         # self.count=10 #不行，是对象自己的count
#         Foo.count+=1
#         self.name=name
#
# obj1=Foo('egon1') #Foo.count+=1  Foo.count=1
# obj2=Foo('egon2') #Foo.count+=1 Foo.count=2
#
# print(Foo.count)
# print(obj1.count)
# print(obj2.count)



# class Student:
#     tag=123123123123123
#     def __init__(self,ID,name,age):
#         self.id=ID
#         self.name=name
#         self.age=age
#     def walk(self):
#         print('%s is walking' %self.name)
#
# s1=Student(1,'egon',18)
# s2=Student(2,'alex',10000)
#
# print(s1.id)
# print(s1.name)
# print(s1.age)
# print(s1.tag)
# print(s2.tag)
#
#
# # s1.walk()
# # s2.walk()
#
#
#对象之间的交互
class Garen:                                #定义英雄盖伦的类，不同的玩家可以用它实例出自己英雄;
    camp='Demacia'                            #所有玩家的英雄(盖伦)的阵营都是Demacia;
    def __init__(self,nickname,life_value=200,aggressivity=100):  #定义英雄的初始攻击力;
        self.nickname=nickname                #为自己的盖伦起个别名;
        self.life_value=life_value            #英雄都有自己的生命值;
        self.aggressivity=aggressivity        #英雄都有自己的攻击力;
    def attack(self,enemy):                  #普通攻击技能，enemy是敌人;
        enemy.life_value-=self.aggressivity   #根据自己的攻击力，攻击敌人就用敌人的生命值减攻击力。

class Riven:                                #定义英雄盖伦的类，与上面Garen类一样的方法
    camp = 'Noxus'
    def __init__(self, nickname, life_value=100, aggressivity=200):
        self.nickname = nickname
        self.life_value = life_value
        self.aggressivity = aggressivity
    def attack(self, enemy):
        enemy.life_value -= self.aggressivity

g=Garen('欧德博爱')  #实际就是在执行Garen.__init__(g1,'欧德博爱')，然后执行__init__内的如g.nickname='欧德博爱' 等代码
r=Riven('矮里渴死')

print(r.life_value)
g.attack(r) #对象交互,对象g攻击对象r  --->   #发送了一条消息，称为向g发送了attack指令
print(r.life_value)








