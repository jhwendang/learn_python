#!/usr/bin/python
# -*- coding:utf-8 -*-

from multiprocessing import Manager,Process
import os
def work(d,l):
    l.append(os.getpid())
    d[os.getpid()]=os.getpid()

if __name__ == '__main__':
    m=Manager()
    l=m.list(['init',])
    d=m.dict({'name':'egon'})


    # p1=Process(target=work,args=(d,l))
    # p2=Process(target=work,args=(d,l))
    # p3=Process(target=work,args=(d,l))
    # p4=Process(target=work,args=(d,l))
    # p5=Process(target=work,args=(d,l))
    #
    # p_l=[p1,p2,p3,p4,p5]
    # for p in p_l:
    #     p.start()
    #
    # for p in p_l:
    #     p.join()

    p_l=[]
    for i in range(5):
        p=Process(target=work,args=(d,l))
        p_l.append(p)
        p.start()

    for p in p_l:
        p.join()
    print(d)
    print(l)


