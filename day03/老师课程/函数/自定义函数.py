#!/usr/bin/python
# -*- coding:utf-8 -*-

#为什么要定义函数？:先定义后使用，如果没有定义而直接使用，就相当于引用了一个不存在的变量名
# foo()
# def foo():
#     print('from foo')
# print(foo)

#函数的使用包含两个阶段：定义阶段和使用阶段

# 语法
# def 函数名(参数1，参数2，...):
#     """文档注释"""
#     函数体
#     return 值

# x=len('hello')
# print(x)


#定义函数的三种形式
#一：无参数函数：如果函数的功能仅仅只是执行一些操作而已，就定义成无参函数，无参函数通常都有返回值
def print_star():
    print('#'*6)

#二：定义有参函数:函数的功能的执行依赖于外部传入的参数，有参函数通常都有返回值
# def my_max(x,y):
#     res=x if x >y else y
#     return res


# 三元表达式
x=10
y=2
# if x > y:
#     print(x)
# else:
#     print(y)
#
# res=x if x > y else y
# print(res)



#三：空函数

# def auth():
#     """认证功能"""
#     pass
# auth()
def insert():
    """插入功能"""
    pass
def select():
    """查询功能"""
    pass
def delete():
    """删除功能"""
    pass
def update():
    """更新功能"""
    pass