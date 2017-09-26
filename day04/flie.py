#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther : Jianghao
# Date : 2017/9/23

# import re,os
# def ip_change(func):
#     def wrapper(*args,**kwargs):
#         real_ip=func(*args,**kwargs)
#         #return real_ip
#         if real_ip:
#            os.system('/bin/bash /data/scripts/nginx-gai-ip.sh {0}'.format(real_ip))
#     return wrapper
#
# @ip_change
# def checkip(ip):
#     p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
#     if p.match(ip):
#         return ip
#
# with open('/data/www/ftp-var2/changeip.txt','r') as f:
#     date=f.read()
#
# checkip(date)


import re,os,time

def tail(func):
    def wrapper1(filepath):
        while True:
            f = open(filepath, 'r')
            ip=f.readline().strip()
            if ip:
                func(ip)
                # print (ip)
                f.close()
                f = open(filepath, 'w')
                f.close()
                os.system('/bin/chmod 666 {0}'.format(filepath))
            else:
                # time.sleep(0)
                f.close()
            time.sleep(300)
    return wrapper1

def ip_change(func):
    def wrapper2(*args,**kwargs):
        real_ip=func(*args,**kwargs)
        if real_ip:
            os.system('/bin/bash /data/scripts/nginx-gai-ip.sh {0}'.format(real_ip))
            # print ('ok')
    return wrapper2

@tail
@ip_change
def checkip(ip):
    p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    if p.match(ip):
        return ip


checkip(filepath='/data/www/ftp-var2/changeip.txt')


