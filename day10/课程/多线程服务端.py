#!/usr/bin/python
# -*- coding:utf-8 -*-
from socket import *
from threading import Thread
def server(ip,port):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((ip,port))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        print('client',addr)
        t = Thread(target=talk, args=(conn, addr))
        t.start()

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