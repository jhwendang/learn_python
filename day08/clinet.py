#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther : Jianghao
# Date : 2017/11/17

import socket
import struct
import json

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("172.168.101.130",8001))

while True:                         #通讯循环
    msg = input('>:').strip()
    if len(msg) == 0:continue       #如果长度等于0，表示没输入信息，continue跳出此次循环，不发送
    client.send(msg.encode())        #encode变成字节发送
    print("client send:",msg)        #打印输入了什么

    #######直接得到数据长度，但这样会报头黏包或者报头数据太长了：################
    # # data1 = client.recv(1024)      #先接收发送信息的长度（据观察，第一次收的信息只会收服务端第一次send，不会收到第二次send,以后的则会混在一起），对应server的方法1
    # # total_size = int(data1.decode())
    # data1 = client.recv(4)        # 先接收发送信息的长度，解包得到固定长度
    # total_size = struct.unpack('i', data1)[0]
    ##############通过报头长度得到报头数据，通过报头数据得到数据长度：#######
    #获取报头长度：
    head_struct = client.recv(4)
    head_len = struct.unpack('i', head_struct)[0]
    #获取报头数据，bytes格式：
    head_bytes = client.recv(head_len)
    #bytes转换成字符串格式（得到的是json格式）
    head_json = head_bytes.decode('utf-8')
    #json里得到报头数据，通过报头数据得到数据长度
    total_size = json.loads(head_json)['total_size']   #此处的'total_size'是自定义的报头格式
    print(total_size)                 #打印长度

    recved_size = 0
    res = b''                         #收到的就是bytes格式，所以初始也得是
    while recved_size < total_size:
        data2 = client.recv(1024)     #每次收1024个字节
        res += data2                  #每次循环把收到的加到定义res里
        recved_size += len(data2)     #受到一次就加一次长度，为了避免最后一次不到1024个字节，所以以收到的实际长度为准

    print('---------------recved--------------------')
    print(res.decode())               #输出总数据，记住server什么平台就用什么格式转，因为得到res的subprocess模块会转成对应平台bytes

client.close()                        #关闭连接，放在循环外