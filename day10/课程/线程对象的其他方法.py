#!/usr/bin/python
# -*- coding:utf-8 -*-
n=11111111111111111111111111111111111
import time
from threading import Thread
import threading
def work():
    time.sleep(2)
    print('%s say hello' %(threading.current_thread().getName()))


if __name__ == '__main__':
    t=Thread(target=work)
    # t.setDaemon(True)
    t.start()
    t.join()
    print(threading.enumerate()) #当前活跃的线程对象，是一个列表形式
    print(threading.active_count()) #当前活跃的线程数目
    print('主线程',threading.current_thread().getName())