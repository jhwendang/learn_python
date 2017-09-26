#!/usr/bin/python
# -*- coding:utf-8 -*-

# 表格输出

# prettytable

# msg = "asdkfasfd\tasdfasdf\tasdfasdf\tasdfasdf\nasdkfasfd\tasdfasdf\tasdfasdf\tasdfasdf\n"
# print(msg.expandtabs(20))

# x y z
# 5x + 3y + z/3 = 100  鸡的总价钱
# x + y + z = 100  鸡的数量
# x > 0; y > 0 z > 0

# 0 < x < 20
for x in range(1, 20):
    for y in range(1, 33):  # 严谨
        z = 100 - x - y  # 满足鸡的总数量
        # 判断满不满足条件
        # 鸡的价钱要对
        # z要是3的倍数
        if 5*x + 3*y + z/3 == 100 and z % 3 == 0:
            print("公鸡:{}只，母鸡：{}只，小鸡：{}只".format(x, y, z))



