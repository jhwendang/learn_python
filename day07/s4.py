#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther : Jianghao
# Date : 2017/11/8

# class Foo:
#     def __enter__(self):
#         print('__enter__')
#         return '1234'
#
#     def __exit__(self,exc_type,exec_val,exc_tb):
#         print('__exit__')
#
# with Foo() as x:
#     print('==>')
#     print(x)

class Foo:
    def __init__(self,name):
        self.name=name

    def __getitem__(self, item):
        print("====>",item)
        # return self.__dict__[item]            #通过这样修改成可以另外赋值其他属性

    # def __setitem__(self, key, value):
    #     self.__dict__[key]=value
    #     print("====>",value)                           #输出赋的值，这里表示字典形式设置时会默认执行setitem.不是字典不会

    def __delitem__(self, key):
        self.__dict__.pop(key)                 #通过这样修改成可以另外删除其他属性
        print('===>del obj[key]')

    def __delattr__(self, item):              #不是字典形式的输出
        self.__dict__.pop(item)
        print('===>del obj.key')

f1=Foo('sb')


f1.name='jh'               #不是字典形式，所以不会执行setitem
# f1['name']=18
# f1['age']=18
# f1['age1']=20
#
# print(f1['age1'])          #记住 这样其实拿不到值，需要通过getitem返回值。因为本身字典里面没有age 属性，通过这样改成了字典里可以赋值，所以需要return
print(f1['name'])          #原本有name属性，所以可以取到
#
# del f1['age']
# del f1.age1                #不同形式


# def func(obj,key,value):
#     obj[key]=value #obj['name']='123123'
#
#
# func(f1,'name','666')
# print(f1.name)