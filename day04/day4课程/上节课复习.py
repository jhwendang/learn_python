#!/usr/bin/python
# -*- coding:utf-8 -*-
# def foo():
#     print('you see what')
#
#
#
#
#
# foo()
# foo()
# foo()
# foo()
# foo()
# foo()
# foo()
# foo()




#函数即变量


# foo()
# def foo():
#     print('ssssssss')

#定义函数就相当于在定义一个变量
#     函数名就是变量名
#     函数值就是函数体
#
# 如果没有实现定义函数，而直接引用，就相当于在引用一个不存在变量名

#所以：函数的使用一定要遵循：先定义后调用

# def bar():
#     print('from bar')
#
# def foo():
#     print('from foo')
#     bar()
#
# foo()






#定义阶段
# def foo():
#     print('from foo')
#     bar()
#
# def bar():
#     print('from bar')
#
#
# #使用
# foo()



#定义阶段
# def foo():
#     print('from foo')
#     bar()
#
# #使用
# foo()
#
# def bar():
#     print('from bar')




# def select(sql):
#     print('select function')
#
#
# def interactive():
#     msg = input('>>: ')
#     l = msg.split()
#     print(l)
#     func=l[0]
#
# interactive()



#
# def my_max(x,y):
#     return x if x > y else y
#
# x='asdfsafsafasdfasdfsadfasdfsadf'
#
#
# print(my_max)
# print(x)
#
# my_max

# l=['a','b','c']
# for i in range(len(l)):
#     print(i)



# def foo(x,y):
#     print(x,y)

# foo(2,1)

# foo(y=1,x=2)
#
#
# foo(1,y=2,x=1)


# def register(name,age=18):
#     print(name,age)
#
# register('egon')
#
#
# def auth(driver):
#     pass
#
# def auth(driver='ldap'):
#     pass
#
#
# auth()


# def foo(x,y,*args):
#     print(x,y)
#     print(args)

# foo(1,2,3,4,5,6,7)

# foo(1,2,[3,4,5])
# foo(1,2,*[3,4,5]) #foo(1,2,3,4,5)
#
# def foo(x,y,z):
#     print(x,y,z)
#
# # foo(*[1,2,3]) #foo(1,2,3)
#
# foo(**{'x':1,'z':3,'y':2})





# def foo(x,y,**kwargs):
#     print(kwargs)
#
# # foo(1,y=2,a=1,b=2,c=3)
#
# foo(x=1,y=2,**{'a':1,'b':2}) #foo(x=1,y=2,a=1,b=2)


# def index(name):
#     print('welcome %s' %name)
#
# def wrapper(*args,**kwargs):
#     print('哈哈哈哈啊')
#
#     #args=(1,2,3,4) kwargs={'a':1,'b':2}
#
#     #index(1,2,3,4,a=1,b=2)
#     index(*args,**kwargs)
#
# wrapper('egon')
# wrapper(name='egon')




def foo(x,*,a,b):
    pass

foo(1,a=6,b=7)
