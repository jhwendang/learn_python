#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther : Jianghao
# Date : 2017/9/16

# dic={'a':1,'b':2,'c':3}
# # print(dic['a'])
# # while True:
# for item1 in dic.keys():
#     # print(item1)
#     print(dic[item1])
#     # print(dic['a'])

#
# n=0
# while n < len(dic):
#     print(dic[n])
#     n+=1

def A():
    x = 1
    def B():
        print(x)
    return B

f=A()
print(f)

x=100
f()
print(x)