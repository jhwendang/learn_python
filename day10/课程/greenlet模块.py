#!/usr/bin/python
# -*- coding:utf-8 -*-
from greenlet import greenlet

def test1():
    print('test1,first')
    gr2.switch()
    print('test1,sencod')
    gr2.switch()
def test2():
    print('test2,first')
    gr1.switch()
    print('test2,sencod')


gr1=greenlet(test1)
gr2=greenlet(test2)
gr1.switch()