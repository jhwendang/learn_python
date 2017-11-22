#!/usr/bin/python
# -*- coding:utf-8 -*-
dic={
    'name':'alex',
    'age':9000,
    'height':'150cm',
}
with open('a.txt','w') as f:
    f.write(str(dic))


# with open('a.txt','r') as f:
#     res=eval(f.read())
#     print(res['name'],type(res))


# x="[null,true,false,1]"
# x="[None,True,1]"

# res=eval(x)
#
# print(res[0],type(res))
# import json
# res=json.loads(x)
# print(res)

import json
#序列化的过程：dic---->res=json.dumps(dic)---->f.write(res)
dic={
    'name':'alex',
    'age':9000,
    'height':'150cm',
}

res=json.dumps(dic)
print(res,type(res))
with open('a.json','w') as f:
    f.write(res)



import json
#反序列化的过程：res=f.read()---->res=json.loads(res)---->dic=res
with open('a.json','r') as f:
    dic=json.loads(f.read())
    print(dic,type(dic))
    print(dic['name'])


#json的便捷操作
import json
dic={
    'name':'alex',
    'age':9000,
    'height':'150cm',
}
json.dump(dic,open('b.json','w'))
