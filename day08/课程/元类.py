#!/usr/bin/python
# -*- coding:utf-8 -*-
# s="print(x)"
# g={'x':100000000}
# l={'x':1}
# exec(s,g,l)

# s="y=2"
# exec(s,g,l)

# print(g)
# print(l)



# s="""
# global y
# y=2
# """
# exec(s,g,l)
# print(g)
# print(l)

# x=1
# with open('exec_test.py','r',encoding='utf-8') as f:
#     s=f.read()
#     # print(s)

# class Foo:
#     pass


# obj=Foo()
# print(type(obj))
#
# print(type(Foo))
# def func():
#     class Foo:
#         pass
#
#     print(Foo)
#
# func()



x=555

class Chinese(object):
    country='China'
    x=11
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def talk(self):

        print(Chinese.x)
        print(x)
        print('%s is talking' %self.name)

# print(Chinese)
f=Chinese(1,2)
print(f.talk())
# print(Chinese.__dict__)
# print(Chinese.__bases__)

#创建类的三要素:
# 1 类名
# 2 继承的父类
# 3 类体
#

#第一步:准备
# class_name='Chinese'
# class_bases=(object,)
# class_body="""
# country='China'
# def __init__(self,name,age):
#     self.name=name
#     self.age=age
# def talk(self):
#     print('%s is talking' %self.name)
# """
# class_dic={}
# exec(class_body,globals(),class_dic)
# # print(class_dic)
#
# #第二步：用type实例化出Chinese
# Chinese=type(class_name,class_bases,class_dic)
# print(Chinese)



# class Mymeta(type):
#     def __init__(self,cls_name,cls_bases,cls_dic):
#         for key,value in cls_dic.items():
#             # print(key,value)
#             if key.startswith('__'):
#                 continue
#             if not callable(value):
#                 continue
#             if not value.__doc__:
#                 raise TypeError('函数%s 必须有注释' %key)
#         super().__init__(cls_name,cls_bases,cls_dic)
#         #type('Foo',(object,),{})
# class Foo(metaclass=Mymeta): #Foo=Mymeta('Foo',(object,),{})
#     x=1
#     def f1(self):
#         'f1 function'
#         print('from f1')
#     def f2(self):
#         'f2 function'
#         print('from f2')




'''
# __call__
__new__
__init__
'''
# class Meta:
#     def __call__(self, *args, **kwargs):
#         #制造对象
#         Mymeta.__new__
#         #初始化对想
#         Mymeta.__init__
# class Mymeta(type):
#     def __init__(self,name,bases,dic):
#         print('__init__')
#         super().__init__(name,bases,dic)
#     def __new__(cls, *args, **kwargs):
#         # print('__new__',args)
#         # print('__new__',kwargs)
#         return type.__new__(cls,*args,**kwargs)
# class Foo(metaclass=Mymeta): #Foo=Mymeta('Foo',(object,),{}) #Mymeta.__init__(Foo,'Foo',(object,),{})
#     pass


# class Mymeta(type):
#     def __call__(self, *args, **kwargs): #self=Foo,args=('egon',) kwargs={'age':18}
#         #调用__new__制造对象
#         # print(args,kwargs)
#         obj=self.__new__(self) #Foo.__new__
#         # print(obj)
#         #调用__init__初始化对象
#         self.__init__(obj, 'egon', age=18)
#
#         #返回对象
#         return obj
# class Foo(metaclass=Mymeta): #Foo=Mymeta('Foo',(object,),{}) #Mymeta.__init__(Foo,'Foo',(object,),{})
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __new__(cls, *args, **kwargs):
#         return object.__new__(cls,*args,**kwargs)
#
# obj=Foo('egon',age=18) #Foo.__init__(obj,'egon',age=18)
# print(obj)
# print(obj.__dict__)


# class Mymeta(type):
#     def __init__(self,cls_name,cls_bases,cls_dic):
#         # print(self)
#         # print(cls_name)
#         # print(cls_bases)
#         # print(cls_dic)
#         pass
#
#     def __call__(self, *args, **kwargs):
#         print('mymeta.__call__')
#         #new新建obj
#
#         #初始化
#
#         return obj
# class Chinese(object,metaclass=Mymeta):
#     # Chinese=Mymeta('Chinese',(object,),{})
#     # Mymeta.__init__(Chinese,'Chinese',(object,),{})
#     x=1
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
# obj=Chinese('egon',18) #__call__('egon',18)
# print(obj)

