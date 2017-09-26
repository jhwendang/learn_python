#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther : Ji anghao
# Date : 2017/9/18


# def f1():
#     def f2():
#         print('from f2')
#         def f3():
#             print('from f3')
#         f3()
#
# # f1()
# x = 1
def f1():
    # x = 1
    def f2():
        print(x)
    return f2

f=f1()
print(f)

x=100
f()
print(x)





