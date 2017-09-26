#!/usr/bin/python
# -*- coding:utf-8 -*-


# print(abs(-1))
# print(all([1,2,3]))
# print(all([0,2,3]))

# print(all(''))

# print(any([0,None,'',1]))
# print(any([0,None,'']))
# print(any([]))

# print(bin(3))
# print(hex(17))
# print(oct(9))

#0 None 空===》bool值为False，其余都为True

# def func():
#     pass
# print(callable(func))


# print(chr(68))
# print(ord('D'))


# res=complex(1+2j)
# print(res.real)
# print(res.imag)


#工厂函数
# dict
# int
# str
# set
# list

# l=[] #l=list([])
# list([1,2,3])
# list(['a'])
# list(['b'])


# l=[]
# print(dir(l)) #查看一个对象下面的属性
#
# print(help(l))

# print(divmod(1000,30))

# x=range(10)
# enumerate([1,2,3]).__next__()


# cmd='print("你瞅啥")'

# dic="{'a':1,'b':2}"
# d=eval(dic)
# print(type(d),d['a'])

# with open('user.db','w',encoding='utf-8') as f:
#     user_dic={'name':'egon','password':'123'}
#     f.write(str(user_dic))

# with open('user.db','r',encoding='utf-8') as f:
#     dic=f.read()
#     print(dic,type(dic))
#     dic=eval(dic)
#     print(dic['name'])



s={1,2} #s=set({1,2}) 定义可变集合

# s.add(3)
# print(s)

# s=frozenset({1,2}) # 定义不可变集合


#哈希：
1. 只要校验的内容一致，那hash得到结果永远一样
2. 不可逆
3. 只要采用的哈希算法一样，那无论被校验的内容有多长，hash的到的结果长度都一样
# print(hash('asdfasdfsadf'))
# print(hash('asdfasdfsadf'))

# x=1
# y=x
# print(id(x),id(y))
#
# print(x is y) #判断的是身份

# a=1
# b=1
# print(a == b)  #判断的是值



# print(max([1,2,3,4]))

# print(pow(10,2,3))

l=['a',4,2,3]
# for i in reversed(l):
#     print(i)
#
# print(list(reversed(l)))

# i=reversed(l)
# for x in i:
#     print(x)
# print(list(i))



# print(round(3.141542653589127134,4))



# l=['a','b','c','d','e']
# print(l[1:4:2])
# s=slice(1,4,2)
# print(l[s])


# vars() #等于locals()


# s='helloo'
# l=[1,2,3,4,5]
#
# z=zip(s,l)
# print(z)
# for i in z:
#     print(i)


import time


m=__import__('time') #以字符串的形式导入模块

# m.sleep(3000)


#面向对象里面讲
super

isinstance
issubclass


classmethod
staticmethod
property

delattr
hasattr
getattr
setattr