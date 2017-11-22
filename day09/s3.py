#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther : Jianghao
# Date : 2017/11/22

from multiprocessing import Pool
import time
def work(n):
    time.sleep(1)
    return n


if __name__ == '__main__':
    pool=Pool()
    for i in range(6):
        #异步applyasync用法：如果使用异步提交的任务，主进程需要使用jion，等待进程池内任务都处理完，然后可以用get收集结果，否则，主进程结束，进程池可能还没来得及执行，也就跟着一起结束了
        res=pool.apply_async(work,args=(i,))
        # time.sleep(1)
        print(res.get())
        # res_l.append(res)
        #
        # for aa in res_l:
        #     print(aa.get())

    # print(res.get())

    #同步apply用法：主进程一直等apply提交的任务结束后才继续执行后续代码
    # res=q.apply(work,args=(2,))
    # print(res)