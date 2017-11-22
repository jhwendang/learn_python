#!/usr/bin/python
# -*- coding:utf-8 -*-

from threading import Thread,Semaphore
import time
def work(id):
    with sem:
        time.sleep(2)
        print('%s say hello' %id)

if __name__ == '__main__':
    sem=Semaphore(5)
    for i in range(20):
        t=Thread(target=work,args=(i,))
        t.start()