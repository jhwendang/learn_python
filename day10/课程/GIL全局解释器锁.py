#!/usr/bin/python
# -*- coding:utf-8 -*-
# from multiprocessing import Process
# from threading import Thread
# import time
# def f1():
#     res=0
#     for i in range(100000000):
#         res+=i
#
# if __name__ == '__main__':
#     p_l=[]
#     start_time=time.time()
#     for i in range(10):
#         # p=Process(target=f1) ##18.351049661636353
#         p=Thread(target=f1) #69.15695548057556
#         p_l.append(p)
#         p.start()
#     for p in p_l:
#         p.join()
#     stop_time=time.time()
#     print('run time is :%s' %(stop_time-start_time))

#I/O密集型
from threading import Thread
from multiprocessing import Process
import time
import os
def work():
    time.sleep(2) #模拟I/O操作，可以打开一个文件来测试I/O,与sleep是一个效果
    # print(os.getpid())

if __name__ == '__main__':
    t_l=[]
    start_time=time.time()
    for i in range(50):
        t=Thread(target=work) #2.0061147212982178
        # t=Process(target=work) #3.235185146331787
        t_l.append(t)
        t.start()

    for t in t_l:
        t.join()
    stop_time=time.time()
    print('run time is %s' %(stop_time-start_time))

