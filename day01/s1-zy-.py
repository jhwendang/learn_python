#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther : Jianghao
# Date : 2017/9/14

f1 = open('db','r')
data = f1.read()
f1.close()
# print(data)
user_info_list=[]
user_str_list = data.split('\n')
# print(user_str_list)
for user_list in user_str_list:
    user=user_list.split('|')
    user_info_list.append(user)
print(user_info_list)


user = input("输入用户名：")
pwd = input("输入密码：")
for item in user_info_list:
    print(item)
    if user == item[0] and pwd == item[1]:
        print("登陆成功")
        break
    else:
        print("登陆失败")
        if user == item[0]:
        # print(item[2])
            item[2] = int(item[2]) - 1
            # print(item)
            # print(user_info_list)
            i = 2
            while i > 0 or item[2] <= 0:
                user = input("输入用户名：")
                pwd = input("输入密码：")
                if user == item[0] and pwd == item[1]:
                    print("登陆成功")
                    break
                else:
                    print("登陆失败")
                    i-=1
            else:
                print("登陆超次")
        break
print(user_info_list)

targe = user_info_list
user_last_info = ''
for user_last in targe:
    user_last_info = user_last_info + '%s|%s|%s' %(user_last[0],user_last[1],user_last[2]) + '\n'
user_last_info = user_last_info.strip()
# print(user_last_info)
f2 = open('db','w')
f2.write(user_last_info)
f2.close()