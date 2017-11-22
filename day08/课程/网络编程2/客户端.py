#!/usr/bin/python
# -*- coding:utf-8 -*-

import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(('127.0.0.1',8080)) #拨通电话

while True: #通信循环
    msg=input('>>: ').strip()
    if not msg:continue #防止客户端发空
    phone.send(msg.encode('utf-8')) #发消息

    back_msg=phone.recv(1024)

    print(back_msg.decode('utf-8'))

phone.close()