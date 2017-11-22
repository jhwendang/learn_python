#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther : Jianghao
# Date : 2017/11/4

v1 = '姓名:%s'
aa = '姜昊1111'

new_v1 = v1%aa
print(new_v1)

new_v2 = v1%'姜昊2222'
print(new_v2)