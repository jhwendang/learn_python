#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther : Jianghao
# Date : 2017/10/25

import re
三、re模块提供的方法介绍
===========================

import re

print(re.findall('e','alex make love') )   #['e', 'e', 'e'],返回所有满足匹配条件的结果,放在列表里

print(re.search('e','alex make love').group()) #e,只到找到第一个匹配然后返回一个包含匹配信息的对象,该对象可以通过调用group()方法得到匹配的字符串,如果字符串没有匹配，则返回None。


print(re.match('e','alex make love'))    #None,同search,不过在字符串开始处进行匹配,完全可以用search+^代替match

#4
12 print(re.split('[ab]','abcd'))     #['', '', 'cd']，先按'a'分割得到''和'bcd',再对''和'bcd'分别按'b'分割
13
14 #5
15 print('===>',re.sub('a','A','alex make love')) #===> Alex mAke love，不指定n，默认替换所有
16 print('===>',re.sub('a','A','alex make love',1)) #===> Alex make love
17 print('===>',re.sub('a','A','alex make love',2)) #===> Alex mAke love
18 print('===>',re.sub('^(\w+)(.*?\s)(\w+)(.*?\s)(\w+)(.*?)$',r'\5\2\3\4\1','alex make love')) #===> love make alex
19
20 print('===>',re.subn('a','A','alex make love')) #===> ('Alex mAke love', 2),结果带有总共替换的个数
21
22
23 #6
24 obj=re.compile('\d{2}')
25
26 print(obj.search('abc123eeee').group()) #12
27 print(obj.findall('abc123eeee')) #['12'],重用了obj