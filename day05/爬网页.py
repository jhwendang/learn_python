#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther : Jianghao
# Date : 2017/9/29

from urllib.request import urlopen #爬网页

def index(url):
    def get():
        return urlopen(url).read()
    return get

oldboy=index('http://crm.oldboyedu.com')

print(oldboy().decode('utf-8'))