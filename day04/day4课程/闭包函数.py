#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
闭包:
1. 定义在内部函数
2. 包含对外部作用域而非全局作用域的引用,
该内部函数就成为闭包函数
'''
#
# def f1():
#     x = 1
#     def f2():
#         print(x)
#
#     return f2
#
# f=f1()
# # print(f)
#
# x=100000000000000000000000000
# f()




#闭包应用：惰性计算

from urllib.request import urlopen

def index(url):
    def get():
        return urlopen(url).read()

    return get

oldboy=index('http://crm.oldboyedu.com')

# print(oldboy().decode('utf-8'))
# print(oldboy.__closure__[0].cell_contents)


# res=urlopen('http://crm.oldboyedu.com').read()
#
# print(res.decode('utf-8'))




x=1
# y=2
def f1():
    # x=1
    y=2
    def f2():
        print(x,y)
    return f2

f=f1()
print(f.__closure__[0].cell_contents)
