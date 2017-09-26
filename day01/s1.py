#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther : Jianghao
# Da te : 2017/9/14

# a= ['alex','erc','xasx']
# i = 0
# while i<len(a):
#     print(a[i])
#     i=i+1
# a.append(123)
# print(a)
# v = {
#     'name':'jh',
#     'password':123
# }
#
# for key,val in v.items():
#     print(key,val)
import getpass
user_list = [
    {'name':'jh1','pwd':'123','times':1},
    {'name':'jh2','pwd':'123345','times':1},
    {'name':'jh3','pwd':'123345','times':1},
]

user = input('用户名：')
pwd = getpass.getpass('密码：')

for item in user_list:
    if user == item['name'] and pwd == item['pwd']:
        print('登陆成功')
        break