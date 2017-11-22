#!/usr/bin/python
# -*- coding:utf-8 -*-
# from multiprocessing import Process
# import time
# import random
# def piao(name):
#     print('%s is piaoing' % name)
#     time.sleep(random.randint(1,3))
#     print('%s is piao end' % name)
# if __name__ == '__main__':
#     p1=Process(target=piao,args=('egon',))
#     p2=Process(target=piao,args=('alex',))
#     p3=Process(target=piao,args=('wupeiqi',))
#     p4=Process(target=piao,args=('yuanhao',))
#
#     p_l=[p1,p2,p3,p4]
#     for p in p_l:
#         p.start()
#     for p in p_l:
#         p.join()
#     print('主进程')









#
# from multiprocessing import Process
# import time
# import random
# def piao(name):
#     print('%s is piaoing' % name)
#     time.sleep(random.randint(1,3))
#     print('%s is piao end' % name)
# if __name__ == '__main__':
#     p1=Process(target=piao,args=('egon',))
#     # p1.daemon=True
#     p1.start()
#
#     p1.terminate()
#     print(p1.is_alive())
#     time.sleep(1)
#     print(p1.is_alive())
#
#     print('主进程')

    # print(p1.name)
    # print(p1.pid)





# from multiprocessing import Process
# import random
# def piao(name):
#     print(name)
#
# if __name__ == '__main__':
#     for i in range(100000):
#         p=Process(target=piao,args=('进程%s' %i,))
#         p.start()


#多进程共享一套文件系统
# from multiprocessing import Process
# import time,random
#
# def work(filename,msg):
#     with open(filename,'a',encoding='utf-8') as f:
#         f.write(msg)
#
# if __name__ == '__main__':
#
#     for i in range(5):
#         p=Process(target=work,args=('a.txt','进程%s\n' %str(i)))
#         p.start()





