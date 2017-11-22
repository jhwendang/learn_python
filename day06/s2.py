#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther : Jianghao
# Date : 2017/11/3

# import hashlib
#
# m=hashlib.md5()
# b=hashlib.md5()
#
# b.update('11111'.encode('utf-8'))
# b.update('11111'.encode('utf-8'))
# print(b.hexdigest())
#
# m.update('11111'.encode('utf-8'))
# print(m.hexdigest())
#
# import hashlib
#
# hash = hashlib.md5('exin'.encode('utf-8'))    #加盐，原本有值
# # hash = hashlib.md5()
# # hash.update('exin'.encode('utf-8'))         #这种结果也一样
# hash.update('admin'.encode('utf-8'))          #再增加
# print(hash.hexdigest())

# import  subprocess
#
# res1=subprocess.Popen('ls /Users/jieli/Desktop',shell=True,stdout=subprocess.PIPE)
#
# res=subprocess.Popen('grep txt$',shell=True,stdin=res1.stdout,stdout=subprocess.PIPE)
#
# print(res.stdout.read().decode('utf-8'))