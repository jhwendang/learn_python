#!/usr/bin/python
# -*- coding:utf-8 -*-

#从大的角度去看，函数的参数分两种：形参(变量名)，实参（值）

#定义阶段
# def foo(x,y): #x=1,y=2
#     print(x)
#     print(y)

#调用阶段
# foo(1,2)


#详细的区分函数的参数分为五种：
# 位置参数，关键字参数，默认参数，可变长参数（*args，**kwargs）,命名关键字参数

#位置参数
# def foo(x,y,z):#位置形参:必须被传值的参数
#     print(x,y,z)
#
# # foo(1,2,3)
# foo(1,2,3) #位置实参数：与形参一一对应

#关键字参数：key=value

def foo(x,y,z):
    print(x,y,z)

# foo(z=3,x=1,y=2)

#关键字参数需要注意的问题：
# 1：关键字实参必须在位置实参后面
# 2: 不能重复对一个形参数传值
# foo(1,z=3,y=2) #正确
# foo(x=1,2,z=3) #错误

# foo(1,x=1,y=2,z=3)




#默认参数

# def register(name,age,sex='male'): #形参：默认参数
#     print(name,age,sex)
#
# register('asb',age=40)
# register('a1sb',39)
# register('a2sb',30)
# register('a3sb',29)
#
# register('钢蛋',20,'female')
# register('钢蛋',sex='female',age=19)

#默认参数需要注意的问题：
#一：默认参数必须跟在非默认参数后
# def register(sex='male',name,age): #在定义阶段就会报错
#     print(name,age,sex)

#（了解）二：默认参数在定义阶段就已经赋值了，而且只在定义阶段赋值一次
# a=100000000
# def foo(x,y=a):
#     print(x,y)
# a=0
# foo(1)

#三：默认参数的值通常定义成不可变类型



#可变长参数
def foo(x,y,*args): #*会把溢出的按位置定义的实参都接收，以元组的形式赋值给args
    print(x,y)
    print(args)
#
# foo(1,2,3,4,5)


# def add(*args):
#     res=0
#     for i in args:
#         res+=i
#     return res
# print(add(1,2,3,4))
# print(add(1,2))



# def foo(x, y, **kwargs):  # **会把溢出的按关键字定义的实参都接收，以字典的形式赋值给kwargs
#     print(x, y)
#     print(kwargs)
# foo(1,2,a=1,name='egon',age=18)


# def foo(name,age,**kwargs):
#     print(name,age)
#     if 'sex' in kwargs:
#         print(kwargs['sex'])
#     if 'height' in kwargs:
#         print(kwargs['height'])
#
# foo('egon',18,sex='male',height='185')
# foo('egon',18,sex='male')


#命名关键字参数(了解)

# def foo(name,age,*,sex='male',height):
#     print(name,age)
#     print(sex)
#     print(height)
# #*后定义的参数为命名关键字参数，这类参数，必须被传值，而且必须以关键字实参的形式去传值
# foo('egon',17,height='185')



# def foo(name,age=10,*args,sex='male',height,**kwargs):
# def foo(name,age=10,*args,sex='male',height,**kwargs):
#     print(name)
#     print(age)
#     print(args)
#     print(sex)
#     print(height)
#     print(kwargs)
#
# foo('alex',1,2,3,4,5,sex='female',height='150',a=1,b=2,c=3)


# def foo(*args):
#     print(args)

# foo(1,2,3,4) # 1,2,3,4 <=====>*(1,2,3,4)

#*['A','B','C','D'],=====>'A','B','C','D'
# foo(*['A','B','C','D']) #foo('A','B','C','D')
# foo(['A','B','C','D']) #

# def foo(x,y,z):
#     print(x,y,z)
#
# # foo(*[1,2,3]) #foo(1,2,3)
# foo(*[1,2]) #foo(1,2)


# def foo(**kwargs):
#     print(kwargs)
#
# #x=1,y=2  <====>**{'y': 2, 'x': 1}
# # foo(x=1,y=2)
#
# foo(**{'y': 2, 'x': 1,'a':1}) #foo(a=1,y=2,x=1)

# def foo(x,y,z):
#     print(x,y,z)
#
# # foo(**{'z':3,'x':1,'y':2}) #foo(x=1,z=3,y=2)
# foo(**{'z':3,'x':1}) #foo(x=1,z=3)


# def foo(x,y,z):
#     print('from foo',x,y,z)
#
# def wrapper(*args,**kwargs):
#     print(args)
#     print(kwargs)
#
#
# wrapper(1,2,3,a=1,b=2)


#
# def foo(x,y,z):
#     print('from foo',x,y,z)
# def wrapper(*args,**kwargs):
#     print(args) #args=(1,2,3)
#     print(kwargs) #kwargs={'a':1,'b':2}
#     foo(*args,**kwargs) #foo(*(1,2,3),**{'a':1,'b':2}) #foo(1,2,3,b=2,a=1)
# # wrapper(1,2,3,a=1,b=2)
# wrapper(1,z=2,y=3)



# def foo(x,y,z):
#     print('from foo',x,y,z)
# def wrapper(*args,**kwargs):
#     # print(args) #args=(1,)
#     # print(kwargs) #kwargs={'y':3,'z':2}
#     foo(*args,**kwargs) #foo(*(1,),**{'y':3,'z':2}) #foo(1,z=2,y=3)
# # wrapper(1,2,3,a=1,b=2)
# wrapper(1,z=2,y=3)
#














#补充：函数定义阶段到底干了什么事情：只检测函数体的语法，并不会执行
# def bar():
#     x
#     if 1 >2:
#           print('====>')
#
# bar()