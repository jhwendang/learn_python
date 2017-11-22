#!/usr/bin/python
# -*- coding:utf-8 -*-
from threading import Thread
def work():
    pass

if __name__ == '__main__':
    for i in range(1000):
        t=Thread(target=work)
        t.start()