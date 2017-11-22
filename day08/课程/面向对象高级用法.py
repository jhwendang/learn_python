#!/usr/bin/python
# -*- coding:utf-8 -*-

# class Foo:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         #必须有返回值，且必须返回字符串类型
#         return '<name:%s age:%s>' %(self.name,self.age)
# obj=Foo('egon',18)
# print(obj)


# class Foo:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     # def __del__(self): #析构方法
#     #     print('del---->')
# obj=Foo('egon',18)
# del obj
# print('=============>')




class Foo:
    def __init__(self,name):
        self.name=name
    # def __getitem__(self, item):
    #     # print("getitem")
    #     return self.__dict__[item]
    # def __setitem__(self, key, value):
    #     # print("setitem",key,value)
    #     self.__dict__[key]=value
    # def __delitem__(self, key):
    #     # print('del obj[key]时,我执行')
    #     self.__dict__.pop(key)
obj=Foo('egon')
# obj.name='egon666'
# print(obj.name)
# obj['name']='egon666'
# print(obj['name'])
# # print(obj.name)
# del obj['name']
# print(obj.__dict__)







#如果没有item方法,需要判断obj的类型,函数将多出于功能无关的逻辑
# def func(obj,key,value):
#     if isinstance(obj,dict):
#         obj[key]=value #obj['name']='123123'
#     else:
#         setattr(obj,key,value)

#加上item方法,则无需判断obj的类型,不管是dict类型还是Foo类型,都以统一的一种[]的方式操作
def func(obj,key,value):
    obj[key]=value #obj['name']='123123'

dic={'name':'egon','age':18}
obj=Foo('egon')

# func(dic,'name','egon666')
# print(dic)
print(obj.__dict__)
func(obj,'name','123123123123')
print(obj.__dict__)
