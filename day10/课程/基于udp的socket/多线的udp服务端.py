#!/usr/bin/python
# -*- coding:utf-8 -*-

import socketserver

class MyUDPhandler(socketserver.BaseRequestHandler):
    def handle(self):
        client_msg,s=self.request
        s.sendto(client_msg.upper(),self.client_address)

if __name__ == '__main__':
    s=socketserver.ThreadingUDPServer(('127.0.0.1',8080),MyUDPhandler)
    s.serve_forever()