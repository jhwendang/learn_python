#!/usr/bin/python
# -*- coding:utf-8 -*-

import queue

# q=queue.Queue(3) #先进先出--->队列
# q.put('first')
# q.put('second')
# q.put((1,2,3,4))
# # q.put((1,2,3,4))
#
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())



# q=queue.LifoQueue() #后进先出--->堆栈
# q.put('first')
# q.put('second')
# q.put((1,2,3,4))
#
# print(q.get())
# print(q.get())
# print(q.get())


q=queue.PriorityQueue() #优先级Queue
q.put((10,'a')) #数字越小，优先级越高
q.put((9,'b'))
q.put((11,'c'))

print(q.get()) #优先级越高优先取出来
print(q.get())
print(q.get())
