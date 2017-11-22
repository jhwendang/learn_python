#!/usr/bin/python
# -*- coding:utf-8 -*-

import pickle

# dic={'name':'alex','age':13}

# print(pickle.dumps(dic))
# with open('a.pkl','wb') as f:
#     f.write(pickle.dumps(dic))

# with open('a.pkl','rb') as f:
#     d=pickle.loads(f.read())
#     print(d,type(d))



# dic={'name':'alex','age':13}
# pickle.dump(dic,open('b.pkl','wb'))
# res=pickle.load(open('b.pkl','rb'))
# print(res,type(res))


#
import json
import pickle
# def func():
#     print('from func')

# json.dumps(func)# 报错，json不支持python的函数类型
# f=pickle.dumps(func)
# print(f)

# pickle.dump(func,open('c.pkl','wb'))
# res=pickle.load(open('c.pkl','rb'))
# print(res)
# res()