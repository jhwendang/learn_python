#!/usr/bin/python
# -*- coding:utf-8 -*-

import socketserver
#MyHandler(conn, client_address, s)
class MyHandler(socketserver.BaseRequestHandler): #通讯循环
    def handle(self):
        while True:
            res=self.request.recv(1024)
            print('client %s msg:%s' %(self.client_address,res))
            self.request.send(res.upper())

if __name__ == '__main__':

    s=socketserver.ThreadingTCPServer(('127.0.0.1',8080),MyHandler)
    s.serve_forever() #链接循环