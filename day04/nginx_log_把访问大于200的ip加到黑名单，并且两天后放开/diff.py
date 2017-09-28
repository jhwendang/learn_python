#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther : Jianghao
# Date : 2017/9/28
"""
对比new和old两文件，把不同的加到add
"""

ip_n = open('iptables_new.txt', 'r')
ip_o = open('iptables_old.txt', 'r')
ip_last = open('blockips_add.txt', 'w')
for ip1 in ip_n.readlines():
    ip1_1 = ip1.strip()
    ip_o.seek(0)
    if ip1_1 not in ip_o.read():
        ip_last.write(ip1_1+'\n')
ip_n.close()
ip_o.close()
ip_last.close()









