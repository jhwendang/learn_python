#!/usr/bin/python
# -*- coding:utf-8 -*-
class Foo:
    def __init__(self,x):
        self.x=x #self.x=10 #self.__dict__['x']=10
    def __getattr__(self, item):
        print('getattr')
    def __setattr__(self, key, value):
        # print('setattr',key,type(key))
        # setattr(self,key,value) #obj.x=1
        self.__dict__[key]=value #self.__dict__['x']=10
    def __delattr__(self, item):
        # print('delattr')
        self.__dict__.pop(item)

obj=Foo(10)
# obj.x=1
# print(obj.__dict__)
# del obj.x

print(obj.__dict__)
obj.a=1
obj.b=2
obj.c=3
print(obj.__dict__)
del obj.c
print(obj.__dict__)
# print(obj.x)
print(obj.yyyyyyyyyyyyyyyyyyyyy)