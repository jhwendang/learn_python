#!/usr/bin/python
# -*- coding:utf-8 -*-

from socket import *
c=socket(AF_INET,SOCK_STREAM)
c.connect(('127.0.0.1',8080))

while True:
    msg=input('>>: ').strip()
    if not msg:continue
    c.send(msg.encode('utf-8'))
    res=c.recv(1024)
    print(res.decode('utf-8'))