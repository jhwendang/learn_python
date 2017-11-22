#!/usr/bin/python
# -*- coding:utf-8 -*-


# import subprocess
#
# res=subprocess.Popen('dir',shell=True,stdout=subprocess.PIPE)
# print(res)
# print(res.stdout.read().decode('gbk'))


import subprocess

# res=subprocess.Popen('diasdfasdfr',shell=True,
#                      stderr=subprocess.PIPE,
#                      stdout=subprocess.PIPE)
#
# print(res.stdout.read().decode('gbk'))
# print(res.stderr.read().decode('gbk'))


#ls |grep txt$
res1=subprocess.Popen(r'dir E:\wupeiqi\s17\day06',shell=True,stdout=subprocess.PIPE)
# print(res1.stdout.read())

res=subprocess.Popen(r'findstr txt*',shell=True,
                     stdin=res1.stdout,
                     stderr=subprocess.PIPE,
                     stdout=subprocess.PIPE)

print('===>',res.stdout.read().decode('gbk'))#管道取一次就空了
print('===>',res.stdout.read().decode('gbk'))
print('===>',res.stdout.read().decode('gbk'))
print('===>',res.stdout.read().decode('gbk'))
print('===>',res.stdout.read().decode('gbk'))
print('===>',res.stdout.read().decode('gbk'))
print('===>',res.stdout.read().decode('gbk'))