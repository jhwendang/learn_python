#!/usr/bin/python
# -*- coding:utf-8 -*-
#
# 生成器函数：只要函数体包含yield关键字，该函数就是生成器函数
# 生成器就是迭代器
#
# def foo():
#     return 1
#     return 2
#     return 3
#     return 4
#
# res1=foo()
# print(res1)
#
# res2=foo()
# print(res2)





# def foo():
#     print('first')
#     yield 1
#     print('second')
#     yield 2
#     print('third')
#     yield 3
#     print('fourth')
#     yield 4
#     print('fifth')
#
# g=foo()
# for i in g:
#     print(i)



# print(g)
#
# print(next(g)) #触发迭代器g的执行，进而触发函数的执行
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))



#
# def counter(n):
#     print('start...')
#     i=0
#     while i < n:
#         # return i
#         print(i)
#         i+=1
#     print('end...')
#
#
# g=counter(5)
# print(g)
# # print(next(g))


{'a':1,'b':2}










'''
yield的功能：
    1.相当于为函数封装好__iter__和__next__
    2.return只能返回一次值，函数就终止了，
    而yield能返回多次值，每次返回都会将函数暂停，下一次next会从
    上一次暂停的位置继续执行


'''

#tail -f a.txt | grep 'python'

#
# import time
# def tail(filepath):
#     with open(filepath,encoding='utf-8') as f:
#         f.seek(0,2)
#         while True:
#             line=f.readline().strip()
#             if line:
#                 yield line
#             else:
#                 time.sleep(0.2)




# t=tail('a.txt')
#
# for line in t:
#     print(line)

# def grep(pattern,lines):
#     for line in lines:
#         if pattern in line:
#             yield line
#
#
# g=grep('python',tail('a.txt'))
# print(g)
#
# for i in g:
#     print(i)






