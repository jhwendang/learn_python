#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
  一：函数对象：函数是第一类对象，即函数可以当作数据传递
    1 可以被引用
    2 可以当作参数传递
    3 返回值可以是函数
    3 可以当作容器类型的元素

'''

#1
# def foo():
#     print('from foo')

# func=foo
#
# print(foo)
# print(func)
# func()

#2
# def foo():
#     print('from foo')
#
# def bar(func):
#     print(func)
#     func()
#
# bar(foo)


#3
# def foo():
#     print('from foo')
#
# def bar(func):
#     return func
#
# f=bar(foo)
#
# print(f)
#
# f()

#4
# def foo():
#     print('from foo')
# dic={'func':foo}
#
# print(dic['func'])
#
# dic['func']()




#应用

def select(sql):
    print('========>select')

def insert(sql):
    print('========>add')

def delete(sql):
    print('=======>delete')

def update(sql):
    print('-=---->update')


func_dic={
    'select':select,
    'update':update,
    'insert':insert,
    'delete':delete
}

def main():
    while True:
        sql = input('>>: ').strip()
        if not sql:continue
        l = sql.split()
        cmd=l[0]
        if cmd in func_dic:
            func_dic[cmd](l)

main()
# def main():
#     sql = input('>>: ')
#     l = sql.split()
#     print(l)
#     if l[0] == 'select':
#         select(l)
#     elif l[0] == 'insert':
#         insert(l)
#     elif l[0] == 'delete':
#         delete(l)
#     elif l[0] == 'update':
#         update(l)



