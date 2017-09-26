#!/usr/bin/python
# -*- coding:utf-8 -*-

# 个人账户文件：user|pwd|3|0
# 商品文件
# 查看商品分页展示
# 购物历史模糊检索

# users_list = []
# f = open("users.txt", "r", encoding="utf-8")
# # for line in f.readlines(): # 一下读到内存
# for line in f: # 一下读到内存
#     users_tmp = line.strip().split("|")  # 保存分割后的列表
# f.close()
#
#
#
# while True:
#     user_name = input("用户名：")
#     pwd = input("密码：")
#     pass

# 商品列表
# goods_list = []
# with open("goods.txt", "r", encoding="UTF-8") as f:
#     for line in f:
#         goods_tmp = line.strip().split("|")
#         goods_list.append(goods_tmp)
# print(goods_list)
#
# for i in enumerate(goods_list, 1):
#     print(i)
#
# # 分页
# while True:
#     shopping_cart = []
#     page_num = input("请输入要浏览的页码数").strip()
#     if page_num.isdigit():  # 判断输入的是不是数字
#         page_num = int(page_num)  # 转成int类型
#         # 判断是不是能被2整除
#         # 能被2整除总页数就正好是 len(goods_list) / 2 页
#         # 不能被2整除总页数就是（len(goods_list) / 2）+1页
#         if page_num > 0 and len(goods_list) / 2 + 1:  # 输入的页码是有效的话
#             start = (page_num -1) * 2
#             end = page_num * 2
#             for i in enumerate(goods_list[start:end], 1):
#                 print(i)
#             chosen = input("你要买啥：").strip()
#             if chosen.isdigit():
#                 chosen = int(chosen)
#                 if 0< chosen <= len(goods_list[start:end]):
#                     # 判断价格能不能购买
#                     # 添加进购物车
#                     shopping_cart.append(goods_list[start:end][chosen - 1])
#                     print(goods_list[start:end][chosen - 1], "现已加入豪华午餐...")
#                 else:
#                     print("请从新输入...")
#             # 输入Q退出
#             elif chosen.upper() == "Q":
#                 print("再见")
#                 # 将购物历史写入文件
#             else:
#                 print("请重新输入...")


# 购物历史的模糊检索
# 字符串的in操作
with open("history.txt", "r", encoding="UTF-8") as f:

    kw = input("请输入关键字：").strip()
    while True:
        for line in f:
            # 判断关键字是否在商品名上
            if kw in line.strip().split("|")[0]:
                print(line)
        else:  # for 循环完整走完，没有break的时候走这个else
            print("没有找到相关记录...")
            break


