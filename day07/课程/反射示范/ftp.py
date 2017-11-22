#!/usr/bin/python
# -*- coding:utf-8 -*-


class FtpCLient:
    def __init__(self,host):
        self.host=host
        print('connecting...')

    def run(self):
        while True:
            inp=input('>>: ').strip()
            inp_l=inp.split()
            if hasattr(self,inp_l[0]):
                func=getattr(self,inp_l[0])
                func(inp_l)

    def get(self,arg):
        print('download file',arg[1])

f=FtpCLient('192.168.1.2')
# f.run()


# m=__import__('sys')
# print(m)
# import importlib
# m=importlib.import_module('sys')
# print(m)


property