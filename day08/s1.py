#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther : Jianghao
# Date : 2017/11/9
#
#
# class Open:
#     def __init__(self, name,mode='r',encoding='utf-8'):
#         self.name = name
#         self.mode=mode
#         self.encoding=encoding
#         self.f=open(self.name,mode=self.mode,encoding=self.encoding)
#     def __enter__(self):
#         return self.f
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         # print('__exit__')
#         print(exc_type)
#         print(exc_val)
#         print(exc_tb)
#         self.f.close()
#         return True
#
# # obj=Open('b.txt','w')
# # print(obj)
#
#
#
# with Open('c.txt','w') as f:          #f=self.f
#     print(f)
#     1/0                                #1除以0报异常，下面代码就不会运行
#     print('===>')
#     f.write('11111\n')                 #上面代码正常的话就能运行
#     f.write('22222\n')
# #最后执行__exit__



class Student(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Student object (name=%s)' % self.name


s = Student('Michael')

print(s)