#!/usr/bin/python
# -*- coding:utf-8 -*-
# import random
# proxy_ip=[
#     '1.1.1.1',
#     '1.1.1.2',
#     '1.1.1.3',
#     '1.1.1.4',
# ]
#
# print(random.choice(proxy_ip))


# import random
# print(random.sample([1,'23',[4,5]],2))

import random
# item=[1,3,5,7,9]
#
# random.shuffle(item)
# print(item)


def v_code(n=5):
    res=''
    for i in range(n):
        num=random.randint(0,9)
        s=chr(random.randint(65,90))
        add=random.choice([num,s])
        res+=str(add)
    return res

print(v_code(6))

