#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther : Jianghao
# Date : 2017/10/14
import os

aa="pythond"
with open(r'E:\PycharmProjects\learn\day05\课程\a\b\c\d\d.txt','r',encoding='utf-8') as f:
    o=f.read()
    # print(o)
    if aa in o:
        print("ok")