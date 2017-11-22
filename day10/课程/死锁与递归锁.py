#!/usr/bin/python
# -*- coding:utf-8 -*-

from threading import Thread,Lock,RLock
import time
class MyThread(Thread):
    def run(self):
        self.f1()
        self.f2()
    def f1(self):
        mutex.acquire()
        print('\033[45m%s 拿到A锁\033[0m' %self.name)
        mutex.acquire()
        print('\033[43m%s 拿到B锁\033[0m' % self.name)
        mutex.release()
        mutex.release()
    def f2(self):
        mutex.acquire()
        time.sleep(5)
        print('\033[43m%s 拿到B锁\033[0m' % self.name)
        mutex.acquire()
        time.sleep(10)
        print('\033[45m%s 拿到A锁\033[0m' % self.name)
        mutex.release()
        mutex.release()

if __name__ == '__main__':
    # mutexA=Lock()
    # mutexB=Lock()
    mutex=RLock()

    for i in range(20):
        t=MyThread()
        t.start()