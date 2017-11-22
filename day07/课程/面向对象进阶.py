#!/usr/bin/python
# -*- coding:utf-8 -*-


# class Foo:
#     pass
#
# class Bar(Foo):
#     pass
#
# print(issubclass(Bar,Foo))


#反射
class Chinese:
    country='China'
    def __init__(self,name,age):
        self.name=name
        self.age=age

# print(Chinese.county) #Chinese.__dict__['country']

p=Chinese('egon',18)
# print(p.name) #p.__dict__['name']
#
# print(hasattr(p,'name'))
# print(hasattr(Chinese,'country'))


# p.x=1
# print(p.__dict__)
# print(p.x)
# setattr(p,'x',1231231231231)
# print(p.__dict__)
# print(p.x)


# print(getattr(p,'x','not exist'))
# print(getattr(p,'name','not exist'))

# setattr(p,'x',123123123123123)
# if hasattr(p,'x'):
#     res=getattr(p,'x')
#     print(res)

# print(Chinese.country)
# delattr(Chinese,'country')
# print(Chinese.country)
# print(p.country)
# p1=Chinese('aaaaa',18)
# print(p1.country)

# import sys
# m=sys.modules[__name__]
# # print(m)
#
# if hasattr(m,'Chinese'):
#     res=getattr(m,'Chinese')
#     # print(res)
#     obj=res('egon',18)
#     print(obj.name)



p.name #p.__dict__['name']
getattr(p,'name') #p.__dict__['name']