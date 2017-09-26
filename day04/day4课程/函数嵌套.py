#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
1 函数的嵌套调用
2 函数的嵌套定义
'''

# def max2(x,y):
#     return x if x > y else y
#
#
# def max4(a,b,c,d):
#     res1=max2(a,b)
#     res2=max2(res1,c)
#     res3=max2(res2,d)
#     return res3
#
# print(max4(10,99,31,22))



#函数的嵌套定义
def f1():

    def f2():
        print('from f2')
        def f3():
            print('from f3')
        f3()
    f2()


# f1()


