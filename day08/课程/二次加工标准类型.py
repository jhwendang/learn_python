#!/usr/bin/python
# -*- coding:utf-8 -*-

# class List(list):
#     pass
#
# l=List([1,2,3])
# print(l)
# l.append(4)
# print(l)


class List(list):
    def __init__(self,item,tag=False):
        super().__init__(item)
        self.tag=tag
    def append(self, p_object):
        # print(p_object)
        if not isinstance(p_object,str):
            raise TypeError('%s must be str' %p_object)
        super(List,self).append(p_object)
    @property
    def mid(self):
        mid_index=len(self)//2
        return self[mid_index]
    def clear(self):
        if not self.tag:
            raise PermissionError('not permissive')
        super().clear()
        self.tag=False
# l=List([1,2,3])
# l.append(4)
# l.append('aaaaa')
# l.append('aaaaa')
# print(l)
# print(l.mid)

# l.insert(0,123123123123123)
# print(l)

# l.tag=True
# l.clear()
# print(l)


# l=[1,2,3,4,5,56,6,7,7]
#
# mid_index=len(l)//2
# print(l[mid_index])





# f=open('a.txt','r',encoding='utf-8')

#授权
import time
class Open:
    def __init__(self,filepath,mode='r',encoding='utf-8'):
        self.filepath=filepath
        self.mode=mode
        self.encoding=encoding
        self.f=open(self.filepath,mode=self.mode,encoding=self.encoding)
    def write(self,msg):
        t=time.strftime('%Y-%m-%d %X')
        self.f.write('%s %s\n' %(t,msg))
    def __getattr__(self, item):
        # print(item,type(item))
        return getattr(self.f,item)
obj=Open('a.txt','w+',encoding='utf-8')

# obj.f.write('11111\n')
# obj.f.write('2222\n')
# obj.f.write('33233\n')
# obj.f.close()


obj.write('aaaaa\n')
obj.write('bbbb\n')
obj.write('cccc\n')

# print(obj.seek)
# obj.close
obj.seek(0)
print(obj.read()) #self.f.read()
obj.close() #self.f.close()




















