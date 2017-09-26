#!/usr/bin/python
# -*- coding:utf-8 -*-

def foo():
    print('from foo')

def bar(name):
    print('bar===>',name)

#按照有参和无参可以将函数调用分两种
foo() #定义时无参，调用时也无需传入参数
bar('egon') #定义时有参，调用时也必须有参数


#按照函数的调用形式和出现的位置，分三种

foo() #调用函数的语句形式

def my_max(x,y):
    res=x if x >y else y
    return res

# res=my_max(1,2)*10000000 #调用函数的表达式形式
# print(res)


res=my_max(my_max(10,20),30) #把函数调用当中另外一个函数的参数
print(res)