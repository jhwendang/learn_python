#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther : Jianghao
# Date : 2017/10/14

#grep -rl 'python' /root

import os

def init(func):                   #加一个装饰器，省掉初始化next()
    def wrapper(*args,**kwargs):
        res=func(*args,**kwargs)
        next(res)
        return res
    return wrapper

@init
def search(target):                 #这样便可以在执行的时候把下面的生成器opener()当参数传进来
    while True:                     #可以循环执行yield
        search_path=yield            #yield send得到值再传值给search_path
        g=os.walk(search_path)
        for par_dir,_,files in g:
            for file in files:
                file_abs_path=r'%s\%s' %(par_dir,file)
                target.send(file_abs_path)    #等同于opener().send(file_abs_path),这里调用了opener函数来运行
@init
def opener(target):
    while True:
        file_abs_path=yield
        with open(file_abs_path,encoding='utf-8') as f:
            target.send((file_abs_path,f))     #等同于cat().send(file_abs_path,f),这里调用了cat函数来运行
@init
def cat(target):
    while True:
        file_abs_path,f=yield                 #(file_abs_path,f)，通过元组传进去
        for line in f:
            target.send((file_abs_path,line))  #等同于grep().send((file_abs_path,line)) ,这里调用了grep函数来运行
                                               #这里除了把文件内容line传给grep，还需要把文件路径file_abs_path传下去，这样文件用于判断路径用于输出
                                               #yield生成器 send时候只能send一个值，但是这一个值却可以用元组的形式表达-->(file_abs_path,line)
@init
def grep(target,pattern):                     #这里除了在执行的时候把下面的生成器printer()当参数，还把需要过滤的字符传进来
    while True:
        file_abs_path,line=yield              #send过来一个元组，然后需要分别接受--->file_abs_path,line=(file_abs_path,line)
        if pattern in line:
            target.send(file_abs_path)         #等同于printer().send(file_abs_path),这里调用了printer函数来运行，同时传入file_abs_path
@init
def printer():
    while True:                              #可以循环执行yield
        file_abs_path=yield                   #运行时便把传过来的file_abs_path交给前面的file_abs_path
        print(file_abs_path)

x=r'E:\PycharmProjects\learn\day05\课程'
g=search(opener(cat(grep(printer(),'python'))))
g.send(x)