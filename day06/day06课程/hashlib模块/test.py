#!/usr/bin/python
# -*- coding:utf-8 -*-


import hashlib

# m=hashlib.md5()
# m.update('asdfasdfasdfasdf你愁啥'.encode('utf-8'))
# print(m.hexdigest())

#d5c70d0ae0e94903fa7a8f3f4c682727
# m=hashlib.md5()
# with open(r'E:\wupeiqi\s17\day06\a.txt','rb') as f:
#     for line in f:
#         m.update(line)
#     md5_num=m.hexdigest()
#
# print(md5_num) #cbb9db48067b92949f98c1cd3440934d

# import hashlib
# m=hashlib.md5()
# m.update('hello'.encode('utf-8'))
# m.update('world'.encode('utf-8'))
# print(m.hexdigest()) #fc5e038d38a57032085441e7fe7010b0


# import hashlib
# m=hashlib.md5()
# m.update('helloworld'.encode('utf-8'))
# print(m.hexdigest()) #fc5e038d38a57032085441e7fe7010b0




# import hashlib
# s=hashlib.sha256()
# s.update('helloworld'.encode('utf-8'))
# print(s.hexdigest())

# import hmac
# h=hmac.new('egon123456'.encode('utf-8'))
# h.update('alex3714'.encode('utf-8'))
# print(h.hexdigest())

import hashlib
m=hashlib.md5('yihangbailushangqingtian'.encode('utf-8'))
m.update('alex3714'.encode('utf-8'))
print(m.hexdigest())