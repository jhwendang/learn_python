#!/usr/bin/python
# -*- coding:utf-8 -*-

#定义名字的方法
# import time
#
# name='egon'
#
# def func():
#     pass
#
# class Foo:
#     pass


#三种名称空间

#内置名称空间:随着python解释器的启动而产生
# print(sum)
# print(max)
# print(min)


# print(max([1,2,3]))

# import builtins
# for i in dir(builtins):
#     print(i)


#全局名称空间：文件的执行会产生全局名称空间，指的是文件级别定义的名字都会放入改空间



# x=1
# if x ==1 :
#     y=2
# import time
#
# name='egon'
#
# def func():
#     pass
#
# class Foo:
#     pass



# x=1
#
#
# def func():
#     money=2000
#     x=2
#     print('func')
# print(x)
# print(func)
# func()
# print(money)

# func()
# print(x)



#局部名称空间:调用函数时会产生局部名称空间，只在函数调用时临时绑定，调用结束解绑定
# x=10000
# def func():
#     x=1
#     def f1():
#         pass

'''
作用域：
    1. 全局作用域：内置名称空间，全局名层空间
    2. 局部作用：局部名称空间
'''

#名字的查找顺序：局部名称空间---》全局名层空间---》内置名称空间
# # x=1
# def func():
#     # x=2
#     # print(x)
#     # sum=123123
#     print(sum)
# func()



# def func():
#     x=2
#
# func()
#
# print(x)



#查看全局作用域内的名字：gloabls()
#查看局局作用域内的名字：locals()
# x=1000
# def func():
#     x=2

# print(globals())
#
# print(locals())
# print(globals() is locals())






# x=1000
# def func(y):
#     x=2
#     print(locals())
#     print(globals())
#
# func(1)


#全局作用域：全局有效，在任何位置都能被访问到，除非del删掉，否则会一直存活到文件执行完毕

#局部作用域的名字：局部有效，只能在局部范围调用，只在函数调用时才有效，调用结束就失效
x=1

def f1():
    print(x)

def foo():
    print(x)

def f(x):
    # x=4
    def f2():
        # x=3
        def f3():
            # x=2
            print(x)

        f3()
    f2()

f(4)





