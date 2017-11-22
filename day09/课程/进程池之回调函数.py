#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
from multiprocessing import Pool
import time
# import random
# import os
# def get_page(url):
#     print('正在爬取网页: %s' %url)
#     time.sleep(random.randint(1,3))
#     return {'url':url}
#
# def parse_page(page_content):
#     print('正在解析网页: %s' %page_content)
#     time.sleep(1)
#     page_content['url']=os.getpid()
#     print('解析网页的结果为:%s' %page_content)
#
#
# if __name__ == '__main__':
#     urls = [
#         'http://www.xiaohuar.com/v/',
#         'http://www.xiaohuar.com/meinv/',
#         'http://www.xiaohuar.com/news/',
#         'http://www.xiaohuar.com/news/1',
#         'http://www.xiaohuar.com/news/2',
#     ]
#     # for url in urls:
#     #     page_content=get_page(url)
#     #     res=parse_page(page_content)
#     #     print(res)
#     pool=Pool()
#     res_l=[]
#     for url in urls:
#         res=pool.apply_async(get_page,args=(url,),callback=parse_page)
#         res_l.append(res)
#
#     for res in res_l:
#         res.get()



from multiprocessing import Pool
import time,random
import requests
import re
import json

def get_page(url,pattern):
    response=requests.get(url)
    if response.status_code == 200:
        return (response.text,pattern)

def parse_page(info):
    page_content,pattern=info
    res=re.findall(pattern,page_content)

    for item in res:
        dic={
            'index':item[0],
            'title':item[1],
            'actor':item[2].strip()[3:],
            'time':item[3][5:],
            'score':item[4]+item[5]

        }
        with open('db.txt','a',encoding='utf-8') as f:
            f.write('%s\n' %json.dumps(dic))
if __name__ == '__main__':
    pattern1=re.compile(r'<dd>.*?board-index.*?>(\d+)<.*?title="(.*?)".*?star.*?>(.*?)<.*?releasetime.*?>(.*?)<.*?integer.*?>(.*?)<.*?fraction.*?>(.*?)<',re.S)

    url_dic={
        'http://maoyan.com/board/7':pattern1,
    }
    p=Pool()
    res_l=[]
    for url,pattern in url_dic.items():
        res=p.apply_async(get_page,args=(url,pattern),callback=parse_page)
        res_l.append(res)

    for i in res_l:
        i.get()

    # res=requests.get('http://maoyan.com/board/7')
    # # print(res.status_code)
    # # print(res.text)
    # pattern=re.compile(r'<dd>.*?board-index.*?>(\d+)<.*?title="(.*?)".*?star.*?>(.*?)<.*?releasetime.*?>(.*?)<.*?integer.*?>(.*?)<.*?fraction.*?>(.*?)<',re.S)
    #
    # print(re.findall(pattern,res.text))




