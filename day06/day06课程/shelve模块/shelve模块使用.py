#!/usr/bin/python
# -*- coding:utf-8 -*-

import shelve

f=shelve.open('sheve.txt')
f['student1']={'name':'egon','age':18,'height':'180cm'}
print(f['student1']['name'])
f.close()