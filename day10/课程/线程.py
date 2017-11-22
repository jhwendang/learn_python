#!/usr/bin/python
# -*- coding:utf-8 -*-
from threading import Thread
from multiprocessing import  Process

def work(name):
    print('%s say hello' %name)



if __name__ == '__main__':
    t=Thread(target=work,args=('egon',))
    # t=Process(target=work,args=('egon',))
    t.start()
    print('主线程')



from threading import Thread
from multiprocessing import Process

class Work(Thread):
    def __init__(self,name):
        super().__init__()
        self.name=name
    def run(self):
        print('%s say hello' % self.name)


if __name__ == '__main__':
    t = Work('egon')
    t.start()
    print('主线程')





# from threading import Thread
# from multiprocessing import  Process
# import os
# def work():
#     print('%s say hello' %os.getpid())
#
#
#
# if __name__ == '__main__':
#     t=Thread(target=work)
#     t.start()
#     print('主线程',os.getpid())