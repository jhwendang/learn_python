#!/usr/bin/python
# -*- coding:utf-8 -*-


# import sys
# print(sys.path)

from conf import settings

def run():
    print('from main')
    print('配置文件内容',settings.x,settings.y)