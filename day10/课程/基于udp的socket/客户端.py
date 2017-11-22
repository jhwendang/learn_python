#!/usr/bin/python
# -*- coding:utf-8 -*-

from socket import *
c=socket(AF_INET,SOCK_DGRAM)

while True:
    msg=input('>>: ').strip()
    c.sendto(msg.encode('utf-8'),('127.0.0.1',8080))
    server_msg,server_addr=c.recvfrom(1024)
    print('from server:%s msg:%s' %(server_addr,server_msg))