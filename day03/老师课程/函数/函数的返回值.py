#!/usr/bin/python
# -*- coding:utf-8 -*-

# def foo():
#     print('from foo')
#     return None
# res=foo()
# print(res)

'''
以三种情况返回值都为None：
没有return
return 什么都不写
return None
'''

# def foo():
#     print('from foo')
#     x=1
#     return x
# res=foo()
# print(res)

#return 一个值  函数调用返回的结果就是这个值


def foo():
    print('from foo')
    x=1
    return 1,[2,3],(4,5),{}
# res=foo()
# print(res) #打印结果：(1,[2,3],(4,5),{})
# a,b,c,d=foo()
# print(d)



#return 值1,值2，值3,...   返回结果:(值1,值2，值3,...)

# t=(1,2,3)
# a,_,_=t
# print(a)

# t=(1,2,3,4,5,6,7,8,9)
# a,*_,c=t
# print(a)
# print(c)