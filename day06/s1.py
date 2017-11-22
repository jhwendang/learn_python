#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther : Jianghao
# Date : 2017/11/3

import json
#
# s1 = '{"key1":"value1"}'      #字符串只能是这个格式的,才能被json转换   通过loads进行反序列化时,必须使用双引号
# s2 = json.loads(s1)           #使用loads反序列化
#
# print(s1,type(s1))
# print(s2,type(s2))
#
# d1 = {'key2':'value2'}
# d2 = json.dumps(d1)
#
# print(d1,type(d1))
# print(d2,type(d2))   #经dumps处理之后，dict变为str

# import json
#
# d1 = {'key2':'value2'}
# json.dump(d1,open('序列化.json','w'))    #将d1序列化，并写入文件

# import json
#
# e1 = json.load(open('序列化.json','r'))      #读取json文件,反序列化
# print(e1,type(e1))


d = [1,2,3,4,5]

print(d,type(d))

json.dump(d,open('1.json','w'))

print(json.load(open('1.json','r')))