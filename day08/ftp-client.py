#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther : Jianghao
# Date : 2017/11/21

import socket
import os
import json
import struct

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8002))
while True:
    msg = input(">>>").strip()
    if not msg:continue
    msg_list = msg.split()
    # print(msg_list)
    if msg_list[0] == 'put':
        if len(msg_list) == 1:
            print("no path")
            continue
        client_path = msg_list[1]
        if not os.path.isfile(client_path):
            print("'%s' is error path" %client_path)
            continue
        filename = os.path.split(client_path)[-1]
        filesize = os.path.getsize(client_path)
        data_head = {
            "action": "put",
            "filename": filename,
            "filesize": filesize,
        }
        data_json = json.dumps(data_head)
        head_size_struct = struct.pack('i', len(data_json))
        client.send(head_size_struct)
        client.send(data_json.encode())
        file_obj = open(client_path, 'rb')
        for line in file_obj:
            client.send(line)
        file_obj.close()
        print("put '%s' ok" %client_path)
    elif msg_list[0] == 'get':
        pass
    else:
        print("please input 'put' or 'get' or 'ls'")

