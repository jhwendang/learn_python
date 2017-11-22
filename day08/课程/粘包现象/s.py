#!/usr/bin/python
# -*- coding:utf-8 -*-

from socket import *
import time

tcp_server=socket(AF_INET,SOCK_STREAM)
tcp_server.bind(('127.0.0.1',8080))
tcp_server.listen(5)

conn,addr=tcp_server.accept()


# res1=conn.recv(5)
# res2=conn.recv(5)
# res3=conn.recv(7)
#
# print(res1)
# print(res2)
# print(res3)




# hello world
res1=conn.recv(11) #ello world
time.sleep(5) #ello worldegon666
res2=conn.recv(7)

print(res1)
print(res2)



