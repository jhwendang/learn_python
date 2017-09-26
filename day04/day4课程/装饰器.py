#!/usr/bin/python
# -*- coding:utf-8 -*-


'''
装饰器：修饰别人的工具，修饰添加功能，工具指的是函数

装饰器本身可以是任何可调用对象，被装饰的对象也可以是任意可调用对象


为什么要用装饰器：
    开放封闭原则：对修改是封闭的，对扩展是开放的
    装饰器就是为了在不修改被装饰对象的源代码以及调用方式的前提下，为期添加新功能

'''




# import time
#
# def timmer(func):
#     def wrapper(*args,**kwargs):
#         start_time=time.time()
#         res=func(*args,**kwargs)
#         stop_time=time.time()
#         print('run time is %s' %(stop_time-start_time))
#     return wrapper
#
# @timmer
# def index():
#
#     time.sleep(3)
#     print('welcome to index')
#
# index()



# import time
#
# def timmer(func):
#     def wrapper():
#         start_time=time.time()
#         func() #index()
#         stop_time=time.time()
#         print('run time is %s' %(stop_time-start_time))
#     return wrapper
#
#
# @timmer #index=timmer(index)
# def index():
#     time.sleep(3)
#     print('welcome to index')
#
#
# # f=timmer(index)
# # # print(f)
# # f() #wrapper()---->index()
#
# # index=timmer(index) #index==wrapper
#
# index() #wrapper()----->



#流程分析
# import time
# def timmer(func):
#     def wrapper():
#         start_time=time.time()
#         func()
#         stop_time=time.time()
#         print('run time is %s' %(stop_time-start_time))
#     return wrapper
#
# @timmer #index=timmer(index)
# def index():
#     time.sleep(3)
#     print('welcome to index')
#
#
# index() #wrapper()








# import time
# def timmer(func):
#     def wrapper(*args,**kwargs):
#         start_time=time.time()
#         res=func(*args,**kwargs)
#         stop_time=time.time()
#         print('run time is %s' %(stop_time-start_time))
#         return res
#     return wrapper
#
# @timmer #index=timmer(index)
# def index():
#     time.sleep(3)
#     print('welcome to index')
#     return 1
#
# @timmer
# def foo(name):
#     time.sleep(1)
#     print('from foo')
#
#
# res=index() #wrapper()
# print(res)
#
# res1=foo('egon')  #res1=wrapper('egon')
# print(res1)
#
#

# def auth(func):
#     def wrapper(*args,**kwargs):
#         name=input('>>: ')
#         password=input('>>: ')
#         if name == 'egon' and password == '123':
#             print('\033[45mlogin successful\033[0m')
#             res=func(*args,**kwargs)
#             return res
#         else:
#             print('\033[45mlogin err\033[0m')
#     return wrapper
#
#
#
# @auth
# def index():
#     print('welcome to index page')
# @auth
# def home(name):
#     print('%s welcome to home page' %name)
#
# index()
# home('egon')
#


# login_user={'user':None,'status':False}
# def auth(func):
#     def wrapper(*args,**kwargs):
#         if login_user['user'] and login_user['status']:
#             res=func(*args,**kwargs)
#             return res
#         else:
#             name=input('>>: ')
#             password=input('>>: ')
#             if name == 'egon' and password == '123':
#                 login_user['user']='egon'
#                 login_user['status']=True
#                 print('\033[45mlogin successful\033[0m')
#                 res=func(*args,**kwargs)
#                 return res
#             else:
#                 print('\033[45mlogin err\033[0m')
#     return wrapper
#
# @auth
# def index():
#     print('welcome to index page')
# @auth
# def home(name):
#     print('%s welcome to home page' %name)
# index()
# home('egon')




























#========================有参装饰器
import time
def timmer(func):
    def wrapper(*args,**kwargs):
        print('====>timmer.wrapper')
        start_time=time.time()
        res=func(*args,**kwargs) #auth_wrapper
        print('====>timmer.wrapper2')
        stop_time=time.time()
        print('run time is %s' %(stop_time-start_time))
        return res
    return wrapper



login_user={'user':None,'status':False}
def auth(driver='file'):
    def auth2(func):
        def wrapper(*args,**kwargs):
            print('=======>auth.wrapper')
            time.sleep(5)
            if driver == 'file':
                if login_user['user'] and login_user['status']:
                    res=func(*args,**kwargs)
                    return res
                else:
                    name=input('>>: ')
                    password=input('>>: ')
                    if name == 'egon' and password == '123':
                        login_user['user']='egon'
                        login_user['status']=True
                        print('\033[45mlogin successful\033[0m')
                        res=func(*args,**kwargs)
                        return res
                    else:
                        print('\033[45mlogin err\033[0m')
            elif driver == 'ldap':
                print('==========ldap的认证')
            elif driver == 'mysql':
                print('==========mysql的认证')
                return func(*args,**kwargs)
            else:
                print('=========未知的认证来源')
        return wrapper
    return auth2


@auth('file') #@auth2====>index=auth2(index)===>index=auth_wrapper
@timmer #index=timmer(auth_wrapper) #index=timmer_wrapper
def index():
    # time.sleep(3)
    print('welcome to index page')
@auth(driver='mysql')
def home(name):
    print('%s welcome to home page' %name)
index() #timmer_wrapper()
# home('egon') #wrapper('egon')