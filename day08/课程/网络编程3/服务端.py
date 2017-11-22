#!/usr/bin/python
# -*- coding:utf-8 -*-
import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #买手机
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
phone.bind(('127.0.0.1',8080)) #插电话卡
phone.listen(5) #开机，backlog

while True: #链接循环
    print('starting....')
    conn,addr=phone.accept() #接电话
    print('cliet addr',addr)
    while True: #与conn的通信循环
        try:#针对windows平台下客户端断开链接
            client_msg=conn.recv(1024) #收消息
            if not client_msg:break #针对linux系统平台下客户端断开链接
            print('client msg: %s' %client_msg)
            conn.send(client_msg.upper()) #发消息
        except Exception:
            break
    conn.close()
phone.close()













