#!/usr/bin/python
# -*- coding:utf-8 -*-


#意读r的方式打开文件
# f=open('a.txt',encoding='utf-8',mode='r')
# print(f)
# data1=f.read()
# print(data1)
# print('=====================================')
# data2=f.read()
# print('data2====>',data2) #读不到内容
# f.close()


# f=open('a.txt',encoding='utf-8',mode='r')
# f.read()
#
# print('=====================================')
# f.seek(0)
# data2=f.read()
# print('data2====>',data2) #读不到内容
# f.close()

# f = open('a.txt', encoding='utf-8', mode='r')



# f.close()
# print(f.closed) #判断文件是否是关闭状态

# print(f.encoding)
# print(f.name)

# print(f.readable()) #判断文件是否是r模式打开的

# print(f.readline(),end='') #一次读一行
# print(f.readline())
# print(f.readline(),end='')


# print(f.readlines()) #读取所有行的内容，存成列表的形式


#以写w的方式打开文件:文件存在则清空，不存在则创建
# f=open('a.txt','w',encoding='utf-8')
# # f=open('b.txt','r',encoding='utf-8') #以读的方式打开文件，文件不存在则报错
# f=open('b.txt','w',encoding='utf-8')
# # print(f.writable())
#
# f.write('111111\n22222222')
# f.write('111111\n22222222')
# # f.seek(0)
# f.write('\n333333\n444444')
#
# f.writelines(['\n55555\n','6666\n','77777\n'])
# f.close()


#文件的修改
# import os
# read_f=open('b.txt','r')
# write_f=open('.b.txt.swap','w')
# for line in read_f.readlines():
#     if line.startswith('1111'):
#         line='2222222222\n'
#     write_f.write(line)
# read_f.close()
# write_f.close()
# os.remove('b.txt')
# os.rename('.b.txt.swap','b.txt')

# import os
# read_y = open('a.txt','r',encoding='utf-8')
# write_y = open('a.txt.swap','w',encoding='utf-8')
# write_y.seek()
# for line in read_y.readlines():
#     if line.startswith('1111'):
#         line = '2222'
#     write_y.write(line)
# read_y.close()
# write_y.close()
# os.remove('a.txt')
# os.rename('a.txt.swap','a.txt')

import time
with open('a.txt','r',encoding='utf-8') as f:
    f.seek(0,2)
    while True:
        line=f.readline().strip()
        if line:
            print('新增一行日志',line,1)
        time.sleep(0.5)


with open('a.txt') as yy:
    yy.seek(0)
    date = yy.read()