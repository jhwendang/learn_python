 #!/usr/bin/python
# -*- coding:utf-8 -*-
# from multiprocessing import Process,Queue
# #队列,先进先出
# q=Queue(3)
#
# q.put({'a':1})
# q.put('b')
# q.put('c')
# print(q.full())
# # q.put('d',False) #等同于q.put_nowait('d')
# # q.put('d',timeout=2)
# print(q.qsize())
#
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.empty())
# print(q.get(block=False))
# print(q.get_nowait())
# print(q.get(timeout=2))



#生产者消费者模型

# from multiprocessing import Process,Queue
# import time
# import random
#
# def consumer(q,name):
#     while True:
#         time.sleep(random.randint(1,3))
#         res=q.get()
#         print('\033[41m消费者%s拿到了%s\033[0m' %(name,res))
#
# def producer(seq,q,name):
#     for item in seq:
#         time.sleep(random.randint(1,3))
#         q.put(item)
#         print('\033[42m生产者%s生产了%s\033[0m' %(name,item))
#
# if __name__ == '__main__':
#     q=Queue()
#     c=Process(target=consumer,args=(q,'egon'),)
#     c.start()
#
#     seq=['包子%s' %i for i in range(10)]
#     producer(seq,q,'厨师1')
#
#     print('主进程')






# from multiprocessing import Process,Queue
# import time
# import random
#
# def consumer(q,name):
#     while True:
#         time.sleep(random.randint(1,3))
#         res=q.get()
#         if res is None:break
#         print('\033[41m消费者%s拿到了%s\033[0m' %(name,res))
#
# def producer(seq,q,name):
#     for item in seq:
#         time.sleep(random.randint(1,3))
#         q.put(item)
#         print('\033[42m生产者%s生产了%s\033[0m' %(name,item))
#     q.put(None)
#
# if __name__ == '__main__':
#     q=Queue()
#     c=Process(target=consumer,args=(q,'egon'),)
#     c.start()
#
#     seq=['包子%s' %i for i in range(10)]
#     p=Process(target=producer,args=(seq,q,'厨师1'))
#     p.start()
#
#     print('主进程')








from multiprocessing import Process,JoinableQueue
import time
import random

def consumer(q,name):
    while True:
        # time.sleep(random.randint(1,3))
        res=q.get()
        q.task_done()
        print('\033[41m消费者%s拿到了%s\033[0m' %(name,res))

def producer(seq,q,name):
    for item in seq:
        # time.sleep(random.randint(1,3))
        q.put(item)
        print('\033[42m生产者%s生产了%s\033[0m' %(name,item))
    q.join()                                     #在这添加q.join（消费者），然后在消费者那添加task_done()，那么消费者只要消费完就告诉生产者结束阻塞
    print('============>>')

if __name__ == '__main__':
    q=JoinableQueue()
    c=Process(target=consumer,args=(q,'egon'),)
    c.daemon=True                                #设置守护进程，主进程结束c就结束
    c.start()

    seq=['包子%s' %i for i in range(10)]
    p=Process(target=producer,args=(seq,q,'厨师1'))
    p.start()

    # master--->producer----->q--->consumer(10次task_done)
    p.join()  #阻塞等待生产者结束
    #主进程等待p结束，p等待c把数据都取完，c一旦取完数据,qjoin不阻塞生产者结束，然后p.join就是不再阻塞,进而主进程结束,主进程结束会回收守护进程c,而且c此时也没有存在的必要了
    print('主进程')






























