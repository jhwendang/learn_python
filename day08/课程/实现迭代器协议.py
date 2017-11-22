#!/usr/bin/python
# -*- coding:utf-8 -*-

class Foo:
    def __init__(self,n,stop):   #定义停止位置
        self.n=n
        self.stop=stop
    def __next__(self):
        if self.n >= self.stop:
            raise StopIteration    #抛异常，for循环会捕捉这个异常暂停
        x=self.n
        self.n+=1
        return x                   #如果直接return self.n下次就没值了

    def __iter__(self):            #迭代器的__iter__是本身
        return self

obj=Foo(0,5)       #0 1 2 3 4
# print(next(obj))   #obj.__next__()
# print(next(obj))   #obj.__next__()

from collections import Iterator
print(isinstance(obj,Iterator))
#
for i in obj:
    print(i)