#!/usr/bin/python
# -*- coding:utf-8 -*-

from socket import *
s=socket(AF_INET,SOCK_DGRAM)
s.bind(('127.0.0.1',8080))


while True:
    client_msg,client_addr=s.recvfrom(1024)
    print(client_msg)
    s.sendto(client_msg.upper(),client_addr)