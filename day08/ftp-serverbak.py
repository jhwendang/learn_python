#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther : Jianghao
# Date : 2017/11/21

import socket
import struct
import json

server = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(('127.0.0.1', 8002))
server.listen(5)
while True:
    conn,client_addr = server.accept()
    print(conn,client_addr)

    while True:
        try:
            head_size_struct = conn.recv(4)
            if not head_size_struct:break
            head_size = struct.unpack('i', head_size_struct)[0]
            head_json = conn.recv(head_size).decode()
            data_head = json.loads(head_json)
            filename = data_head['filename']
            filesize = data_head['filesize']
            action = data_head['action']
            if action == 'put':
                recved_size = 0
                recved_file = open(filename, 'wb')
                while recved_size < filesize:
                    recved_data = conn.recv(4096)
                    recved_file.write(recved_data)
                    recved_size += len(recved_data)
                else:
                    print('ok!')
                recved_file.close()
            elif action == 'get':
                pass
            elif action == 'ls':
                pass
        except ConnectionError:
            break
    conn.close()
server.close()



