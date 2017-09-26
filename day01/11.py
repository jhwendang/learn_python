#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther : Jianghao
# Date : 2017/9/14

#!/usr/bin/env python
# -*- coding:utf-8 -*-

# import datetime

#打开数据库
f1 = open('db','r')
date = f1.read()
f1.close()
# print(date)
#格式化，列表中嵌套字典
user_info_list = []   #声明是个字典：
user_str_list = date.split('\n')   #左右移除空白
for item in user_str_list:         #取值
    v = {}
    temp = item.split("|")
    v['username'] = temp[0]
    v['password'] = temp[1]
    v['times'] = temp[2]
    user_info_list.append(v)

login_status = 3
while login_status > 0:
    while login_status > 0:
        name = input("请输入用户名：")
        pwd = input("请输入密码：")
        for item in user_info_list:
            if name == item['username']:
                if int(item['times']) > 0:
                    if pwd == item['password']:
                        print("登录成功，欢迎您！")
                        item['times'] = 3
                        login_status = 0
                        break
                    else:
                        login_status -= 1
                        if login_status == 0:
                            print("尝试次数超限，登录失败")
                        else:
                            print("账号或密码错误，请重新输入！")
                        item['times'] = int(item['times']) - 1
                        break
                else:
                    print("用户已被锁定,请联系管理员解锁！")
                    login_status = 0
                    break
        else:
            login_status -= 1
            if login_status == 0:
                print("尝试次数超限，登录失败")
            else:
                print("账号或密码错误，请重新输入！")
    # 变成字符串
    line = ''
    i = 1
    for item2 in user_info_list:
        if i < user_info_list.__len__():
            line = line + item2['username'] + '|' + item2['password'] + '|' + str(item2['times']) + '\n'
            i = i + 1
        else:
            line = line + item2['username'] + '|' + item2['password'] + '|' + str(item2['times'])
    # 写入文件
    f2 = open("db", 'w')
    f2.write(line)
    f2.close()
