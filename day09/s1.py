#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther : Jianghao
# Date : 2017/11/22

from multiprocessing import Process
import time

# # 方法一：
def cs(dd):
    print("start %s" %dd)
    time.sleep(2)
    print("stop%s" %dd)


if __name__ == '__main__':
    p1=Process(target=cs,args=('jh',),name='cs')
    p2 = Process(target=cs, args=('jh2',), name='cs2')
    p3 = Process(target=cs, args=('jh3',), name='cs3')
    p4 = Process(target=cs, args=('jh4',), name='cs4')
    p5 = Process(target=cs, args=('jh5',), name='cs5')
    p_l = [p1,p2,p3,p4,p5]
    # for ps in p_l:
    #     ps.start()
    # for pj in p_l:
    #     pj.join()
    p1.daemon=True
    p1.start()
    p1.terminate()
    print('父进程')

# # 方法二：
# class P_Process(Process):
#     def __init__(self,name):
#         super().__init__()
#         self.name = name
#     def run(self):
#         print("start %s" %self.name)
#         time.sleep(2)
#         print("stop %s" %self.name)
#
# if __name__ == '__main__':
#     p1=P_Process('jh')
#     p1.start()
#     time.sleep(1)
#     print('父进程')