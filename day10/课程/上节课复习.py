#!/usr/bin/python
# -*- coding:utf-8 -*-


# from multiprocessing import  Process
# class Work(Process):
#     def run(self):
#         print('%s say hello' %self.name)
#
# def work(name):
#     print('%s say hello' %name)
#
# if __name__ == '__main__':
#     p=Process(target=work,args=('egon1',))
#     # p.daemon=True
#     p.start()
#     # p.terminate()
#     # p.is_alive()
#     # p.join()
#     print('主线程')

    # p=Work()
    # # p.daemon=True
    # p.start()
    # # p.join()
    # print('主线程')


# from multiprocessing import Manager,Process,Lock
# def work(d,mutex):
#     with mutex:
#         # mutex.acquire()
#         d['count']-=1
#         # mutex.release()
#
# if __name__ == '__main__':
#     mutex=Lock()
#     m=Manager()
#     d=m.dict({'count':100})
#     p_l=[]
#     for i in range(100):
#         p=Process(target=work,args=(d,mutex))
#         p_l.append(p)
#         p.start()
#
#     for p in p_l:
#         p.join()
#     print('主线程',d)
#

