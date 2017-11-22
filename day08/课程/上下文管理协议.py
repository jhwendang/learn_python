#!/usr/bin/python
# -*- coding:utf-8 -*-

# class Foo:
#     def __init__(self, name):
#         self.name = name
#     def __enter__(self):
#         print('__enter__')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('__exit__')
#
#
# with Foo() as x: #x=Foo()
#     print(x)
#     print('=>')
#     print('=>')
#     print('=>')
#     print('=>')


class Open:
    def __init__(self, name,mode='r',encoding='utf-8'):
        self.name = name
        self.mode=mode
        self.encoding=encoding
        self.f=open(self.name,mode=self.mode,encoding=self.encoding)
    def __enter__(self):
        return self.f
    def __exit__(self, exc_type, exc_val, exc_tb):
        # print('__exit__')
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        self.f.close()
        return True

# obj=Open('b.txt','w')
# print(obj)



with Open('c.txt','w') as f: #f=self.f
    print(f)
    1/0
    print('===>')
    f.write('11111\n')
    f.write('22222\n')

print('=======>with以外的代码')
# int('aaaaaa')
#
# raise TypeError('11111111111')