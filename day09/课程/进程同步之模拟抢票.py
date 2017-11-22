#!/usr/bin/python
# -*- coding:utf-8 -*-
from multiprocessing import Process,Lock
import json
import time
import random
def work(dbfile,name,lock):
    # lock.acquire()
    with lock:
        with open(dbfile,encoding='utf-8') as f:
            dic=json.loads(f.read())

        if dic['count'] > 0:
            dic['count']-=1
            time.sleep(random.randint(1,3)) #模拟网络延迟
            with open(dbfile,'w',encoding='utf-8') as f:
                f.write(json.dumps(dic))
            print('\033[43m%s 抢票成功\033[0m' %name)
        else:
            print('\033[45m%s 抢票失败\033[0m' %name)
    # lock.release()


if __name__ == '__main__':
    lock=Lock()
    p_l=[]
    for i in range(100):
        p=Process(target=work,args=('a.txt','用户%s' %i,lock))
        p_l.append(p)
        p.start()


    for p in p_l:
        p.join()
    print('主进程')