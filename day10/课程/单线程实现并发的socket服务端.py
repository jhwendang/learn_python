#!/usr/bin/python
# -*- coding:utf-8 -*-
from gevent import monkey;monkey.patch_all()
from socket import *
import gevent
def server(ip,port):
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind((ip,port))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        print('client',addr)
        gevent.spawn(talk,conn,addr)

def talk(conn,addr): #通信
    try:
        while True:
            res=conn.recv(1024)
            if not res:break
            print('client %s:%s msg:%s' %(addr[0],addr[1],res))
            conn.send(res.upper())
    except Exception:
        pass
    finally:
        conn.close()

if __name__ == '__main__':
    server('127.0.0.1', 8080)