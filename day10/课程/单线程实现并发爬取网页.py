#!/usr/bin/python
# -*- coding:utf-8 -*-
# import requests
# import time
# # response=requests.get('https://www.python.org')
# # print(response.status_code)
# # print(response.text)
#
# def get_page(url):
#     print('GET page:%s' %url)
#     response=requests.get(url)
#     if response.status_code == 200:
#         print(response.text)
#
# start_time=time.time()
# get_page('https://www.python.org')
# get_page('https://www.yahoo.com')
# get_page('https://www.github.com')
# stop_time=time.time()
# print('run time is :%s' %(stop_time-start_time)) #11.989685773849487









from gevent import monkey;monkey.patch_all()
import requests
import time
import gevent
def get_page(url):
    print('GET page:%s' %url)
    response=requests.get(url)
    if response.status_code == 200:
        print(response.text)

start_time=time.time()
g1=gevent.spawn(get_page,url='https://www.python.org')
g2=gevent.spawn(get_page,url='https://www.yahoo.com')
g3=gevent.spawn(get_page,url='https://www.github.com')
gevent.joinall([g1,g2,g3])
stop_time=time.time()
print('run time is :%s' %(stop_time-start_time)) #8.745500326156616