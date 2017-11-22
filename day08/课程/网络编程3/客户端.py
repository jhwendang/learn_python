#!/usr/bin/python
# -*- coding:utf-8 -*-

import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(('127.0.0.1',8080)) #拨通电话

while True: #通信循环
    cmd=input('>>: ').strip()
    if not cmd:continue #防止客户端发空
    phone.send(cmd.encode('utf-8')) #发消息

    cmd_res=phone.recv(1024)

    print(cmd_res.decode('gbk'))
phone.close()