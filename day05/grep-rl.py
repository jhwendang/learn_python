#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther : Jianghao
# Date : 2017/10/13

# def eater(name):
#     print('%s ready to eat' %name)
#     while True:
#         food=yield
#         print('%s start to eat %s' %(name,food))
#
#
# g=eater('alex')
# next(g)
# g.send('手指头1')
# g.send('手指头2')

# def deco(func):
#     def wrapper(*args,**kwargs):
#         res=func(*args,**kwargs)
#         next(res)
#         # next(res)
#         # return res
#     return wrapper
#
# @deco
# def eater(name):
#     print('%s ready to eat' %name)
#     while True:
#         food=yield
#         print('%s start to eat %s' %(name,food))
#
#
# g=eater('alex')
# # print(g)
# # next(g) #等同于 g.send(None)
# next(g)
# # next(g)
# # g.send('手指头')
# # g.send('脚指头')
# # g.send('别人的手指头')
# # g.send('别人的脚指

import os

def init(func):                              #加一个装饰器，省掉初始化next()
    def wrapper(*args,**kwargs):
        res=func(*args,**kwargs)
        next(res)
        return res
    return wrapper

@init
def search(opener_target):                      #这样便可以在执行的时候把下面的生成器opener()当参数传进来
    while True:                                 #可以循环执行yield
        search_path=yield                       #yield send得到值再传值给search_path
        g=os.walk(search_path)
        for par_dir,_,files in g:
            for file in files:
                file_abs_path=r'%s\%s' %(par_dir,file)
                opener_target.send(file_abs_path)  #等同于opener().send(file_abs_path),这里调用了opener函数来运行
@init
def opener(grep_target):
    while True:
        file_abs_path=yield
        with open(file_abs_path,'r',encoding='utf-8') as f:
            open_file=f.read()
            grep_target.send((file_abs_path,open_file)) #等同于grep().send((file_abs_path,open_file)) ,这里调用了grep函数来运行
                                                        #这里除了把打开了的文件open_file传给grep，还需要把文件路径file_abs_path传下去，这样文件用于判断路径用于输出
                                                        #yield生成器 send时候只能send一个值，但是这一个值却可以用元组的形式表达-->(file_abs_path,open_file)
@init
def grep(pattern):
    while True:
        file_abs_path,cat_file=yield              #send过来一个元组，然后需要分别接受--->file_abs_path,cat_file=(file_abs_path,open_file)
        if pattern in cat_file:
            print(file_abs_path)


x=r'E:\PycharmProjects\learn\day05\课程'  #x是路径
p="python"                                #p是过滤字符
s=search(opener(grep(p)))                 #把grep的执行结果（生成器）当参数传给opener函数的grep_target，又把opener的执行结果（生成器）当参数传给search函数的opener_target
s.send(x)                                 #search得到的结果本生就是生成器，不会直接执行，所以需要send