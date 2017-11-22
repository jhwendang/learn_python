#!/usr/bin/python
# -*- coding:utf-8 -*-

import socket
import struct
import json
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(('127.0.0.1',8080)) #拨通电话

while True: #通信循环
    cmd=input('>>: ').strip()
    if not cmd:continue #防止客户端发空
    phone.send(cmd.encode('utf-8')) #发消息

    #先收报头的长度
    head_struct=phone.recv(4)
    head_len=struct.unpack('i',head_struct)[0]

    #再收报头的bytes
    head_bytes=phone.recv(head_len)
    head_json=head_bytes.decode('utf-8')
    head_dic=json.loads(head_json)

    #最后根据报头里的详细信息取真实的数据
    print(head_dic)
    total_size=head_dic['total_size']
    recv_size=0
    data=b''
    while recv_size < total_size: #10240 +1
        recv_data=phone.recv(1024)
        data+=recv_data
        recv_size+=len(recv_data)
    print(data.decode('gbk'))
phone.close()