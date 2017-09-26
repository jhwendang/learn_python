#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther : Jianghao
# Date : 2017/9/14
# #作业1
# v1 = [11,22,33,44,55,66,77,88,99,90]
# v2 ={'k1':[],'k2':[]}
#
# for item in v1:
#     if item < 66:
#         v2['k1'].append(item)
#     else:
#         v2['k2'].append(item)
# print(v2)

# #作业2
# v=2000
# goods = [
#                 {"name": "电脑", "price": 1999},
#                 {"name": "鼠标", "price": 10},
#                 {"name": "游艇", "price": 20},
#                 {"name": "美女", "price": 998},
# ]
# while True:
#     num = input('>>>')
#     num = int(num)
#     if goods[num]['price'] <= v:
#         print("添加成功")
#         v = v - goods[num]['price']
#         print(haiv)
#     else:
#         print("余额不足")
#         break

# #作业3
# dic = {
#                 "河北": {
#                     "石家庄": ["鹿泉", "藁城", "元氏"],
#                     "邯郸": ["永年", "涉县", "磁县"],
#                 },
#                 "河南": {
#                     ...
#                 },
#                 "山西": {
#                     ...
#                 }
# }
#
# for v in dic.keys():
#     print(v)
# inp = input("请输入:")
# n=str(dic[inp])
# if n == '{Ellipsis}':
#     print("无下一级")
# else:
#     for v1 in dic[inp].keys():
#         print(v1)
#     inp1 = input("请输入:")
#     for a in dic[inp][inp1]:
#         print(a)