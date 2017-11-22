#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther : Jianghao
# Date : 2017/11/4

# class ParentClass1:   #定义父类
#     pass
#
# class ParentClass2:   #定义父类
#     pass
#
# class SubClass1(ParentClass1):   #单继承，基类是ParentClass1，派生类是SubClass
#     pass
#
# class SubClass2(ParentClass1,ParentClass2):   #python支持多继承，用逗号分隔开多个继承的类
#     pass
#
# print(SubClass1.__base__)
# print(SubClass2.__bases__)


#寻找继承关系
#继承的好处一：减少冗余代码
#在子类定义新的属性，覆盖掉父类的属性,称为派生
#
# class Animal:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#     def eat(self):
#         print('eating')
#     def talk(self):
#         print('%s 正在叫' %self.name)
#
#
# class People1(Animal):                           #继承
#     def __init__(self, name, age, sex,education):
#         Animal.__init__(self,name,age,sex)
#         self.education=education
#
# class People2(Animal):
#     def __init__(self, name, age, sex,education):
#         Animal.__init__(self,name,age,sex)
#         self.education=education
#     def talk(self):                             #派生
#         print('%s say hello' %self.name)
#
# class Pig(Animal):
#     pass
#
# peo1=People1('alex',18,'male','小学肄业')   #调用People1.__init__
# peo2=People2('alex',18,'male','小学肄业')   #调用People2.__init__
# pig1=Pig('wupeiqi',20,'female')
#
# print(peo1.education)                      #继承并且有自己的属性
# peo1.talk()                                  #继承
# peo2.talk()                                  #派生
# pig1.talk()                                  #继承

#
# class Foo:
#     @property   #装饰器，做成了数据属性
#     def test(self):
#         print('from fooo')
#     # test=property(test)
#
# f=Foo()
# # f.test()   #就可以不用这样调
# f.test       #test成为了数据参数


class People:
    def __init__(self,name):
        self.__name=name

    @property                #装饰器成属性
    def name(self):
        return self.__name

    @name.setter            #@的setter方法，便可以再次封装
    def name(self,value):
        if not isinstance(value,str):               #这两行是做判断是否为字符
            raise TypeError('名字必须是字符串类型') #
        self.__name=value   #赋值给原来的_People__name,修改name值


p=People('egon')
print(p.name)    #原来的值
p.name='egon666' #修改值
print(p.name)