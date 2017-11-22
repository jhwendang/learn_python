#!/usr/bin/python
# -*- coding:utf-8 -*-

# import sys
#
# print(sys.argv)


import sys,time

for i in range(50):
    sys.stdout.write('%s\r' %('#'*i))
    sys.stdout.flush()
    time.sleep(0.1)

'''
注意：在pycharm中执行无效，请到命令行中以脚本的方式执行
'''
