#!/usr/bin/python
# -*- coding:utf-8 -*-

# from multiprocessing import Process
# import time
# import random
#
# def piao(name):
#     print('%s is piaoing' %name)
#     time.sleep(3)
#     print('%s is piao end' %name)
#
# if __name__ == '__main__':
#     p1=Process(target=piao,args=('egon',),name='<p1>')
#     p1.start()
#     print('p1 name is %s ' %p1.name)
#     # time.sleep(1)
#     print('父进程')




from multiprocessing import Process
import time
import random
class Piao(Process):
    def __init__(self,name):
        super().__init__()
        self.name=name

    def run(self):
        print('%s is piaoing' %self.name)
        time.sleep(3)
        print('%s is piao end' %self.name)

if __name__ == '__main__':
    print('hahahahahahah=========>')
    p1=Piao('egon')
    p1.start() #p1.run
    # time.sleep(1)
    print('父进程')