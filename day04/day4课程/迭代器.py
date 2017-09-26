#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
迭代器
迭代的概念:重复+上一次迭代的结果为下一次迭代的初始值
重复的过程称为迭代,每次重复即一次迭代，
并且每次迭代的结果是下一次迭代的初始值

'''


while True: #只满足重复，因而不是迭代
    print('====>')


下面才为迭代
l = [1, 2, 3]
count = 0
while count < len(l):  # 只满足重复，因而不是迭代
    print('====>', l[count])
    count += 1
#
# l = (1, 2, 3)
# count = 0
# while count < len(l):  # 只满足重复，因而不是迭代
#     print('====>', l[count])
#     count += 1

# s='hello'
# count = 0
# while count < len(s):
#     print('====>', s[count])
#     count += 1
#


#为什么要有迭代器？对于没有索引的数据类型，必须提供一种不依赖索引的迭代方式

#可迭代的对象:内置__iter__方法的，都是可迭代的对象

# [1,2].__iter__()
# 'hello'.__iter__()
# (1,2).__iter__()
#
# {'a':1,'b':2}.__iter__()
# {1,2,3}.__iter__()

#迭代器：执行__iter__方法，得到的结果就是迭代器，迭代器对象有__next__方法
# i=[1,2,3].__iter__()
#
# print(i)
#
# print(i.__next__())
# print(i.__next__())
# print(i.__next__())
# print(i.__next__()) #抛出异常：StopIteration


# i={'a':1,'b':2,'c':3}.__iter__()

# print(i.__next__())
# print(i.__next__())
# print(i.__next__())
# print(i.__next__())

# dic={'a':1,'b':2,'c':3}
# i=dic.__iter__()
# while True:
#     try:
#         key=i.__next__()
#         print(dic[key])
#     except StopIteration:
#         break



# s='hello'
# print(s.__len__())
#
# print(len(s))
#
# len(s)====== s.__len__()


s={'a',3,2,4}

# s.__iter__() #iter(s)

# i=iter(s)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))


#如何判断一个对象是可迭代的对象，还是迭代器对象
from collections import Iterable,Iterator

# 'abc'.__iter__()
# ().__iter__()
# [].__iter__()
# {'a':1}.__iter__()
# {1,2}.__iter__()

# f=open('a.txt','w')
# f.__iter__()


#下列数据类型都是可迭代的对象
# print(isinstance('abc',Iterable))
# print(isinstance([],Iterable))
# print(isinstance((),Iterable))
# print(isinstance({'a':1},Iterable))
# print(isinstance({1,2},Iterable))
# print(isinstance(f,Iterable))



#只有文件是迭代器对象
# print(isinstance('abc',Iterator))
# print(isinstance([],Iterator))
# print(isinstance((),Iterator))
# print(isinstance({'a':1},Iterator))
# print(isinstance({1,2},Iterator))
# print(isinstance(f,Iterator))



'''
可迭代对象：只有__iter__方法，执行该方法得到的迭代器对象

迭代协议：
    对象有__next__
    对象有__iter__,对于迭代器对象来说，执行__iter__方法，得到的结果仍然是它本身


'''
# f1=f.__iter__()
#
# print(f)
# print(f1)
# print(f is f1)

#
# l=[]
# i=l.__iter__()
#
# print(i.__iter__())
# print(i)
# print(l)


dic={'name':'egon','age':18,'height':'180'}
# print(dic.items())

# for k,v in dic.items():
#     print(k,v)

# i=iter(dic)
# while True:
#     try:
#         k=next(i)
#         print(k)
#     except StopIteration:
#         break
# for k in dic: #i=iter(dic)  k=next(i)
#     print(k)
#     print(dic[k])
#



# l=['a','b',3,9,10]
# for i in l:
#     print(i)



# with open('a.txt','r',encoding='utf-8') as f:
#     for line in f:
#         print(line)
    # print(next(f))
    # print(next(f))
    # print(next(f))
    # print(next(f))
    # print(next(f))
    # print(next(f))
    # print(next(f))
    # print(next(f))


'''
迭代器的优点和缺点
优点：
    1.提供了一种不依赖下标的迭代方式
    2.就跌迭代器本身来说，更节省内存

缺点：
    1. 无法获取迭代器对象的长度
    2. 不如序列类型取值灵活，是一次性的，只能往后取值，不能往前退
'''
# l=[10000,2,3,4,5]
#
# i=iter(l)
#
# print(i)
# print(next(i))
#
# f=open('a.txt',encoding='utf-8')
#
# for line in f.readlines():
#     print(line)

# print(next(f))

# for line in f:
#     print(line)




# l=[10000,2,3,4,5]
#
# i=iter(l)
#
# for item in i:
#     print(item)
# print('=============================')
#
#
# for item in i:
#     print(item)

l=[10000,2,3,4,5]

i=enumerate(l)

print(next(i))
print(next(i))



