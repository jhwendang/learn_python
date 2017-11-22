#!/usr/bin/python
# -*- coding:utf-8 -*-
from threading import Thread,Lock
import time
n=100
def work():
    with mutex1:
        global n
        temp=n
        time.sleep(0.5)
        n=temp-1

if __name__ == '__main__':
    mutex1=Lock()
    t_l=[]
    for i in range(100):
        t=Thread(target=work)
        t_l.append(t)
        t.start()
    for t in t_l:
        t.join()
    print(n)
