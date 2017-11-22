#!/usr/bin/python
# -*- coding:utf-8 -*-

# class Foo:
#     def test1(self):
#         print('test1',self)
#
#     def test2(self):
#         print('test2',self)
#
#     def test3():
#         print('test3')
# f=Foo()
# # f.test1()
# # f.test2()
# f.test3()


class Foo:
    @classmethod
    def test(cls):
        print(cls)

print(Foo.test)
f=Foo()

Foo.test()
print(Foo)
f.test()



# class Foo:
#     @staticmethod
#     def test(x,y):
#         print('test',x,y)
#
# Foo.test(1,3)
# f=Foo()
# f.test(1,10)







'''

类中定义的函数分成两大类：

　　一：绑定方法（绑定给谁，谁来调用就自动将它本身当作第一个参数传入）：

　　　　1. 绑定到类的方法：用classmethod装饰器装饰的方法。

                为类量身定制

                类.boud_method(),自动将类当作第一个参数传入

              （其实对象也可调用，但仍将类当作第一个参数传入）

　　　　2. 绑定到对象的方法：没有被任何装饰器装饰的方法。

               为对象量身定制

               对象.boud_method(),自动将对象当作第一个参数传入

             （属于类的函数，类可以调用，但是必须按照函数的规则来，没有自动传值那么一说）

　　二：非绑定方法：用staticmethod装饰器装饰的方法

　　   1. 不与类或对象绑定，类和对象都可以调用，但是没有自动传值那么一说。就是一个普通工具而已

　　　　注意：与绑定到对象方法区分开，在类中直接定义的函数，没有被任何装饰器装饰的，都是绑定到对象的方法，可不是普通函数，对象调用该方法会自动传值，而staticmethod装饰的方法，不管谁来调用，都没有自动传值一说


'''

# class Foo:
#     def test1(self):
#         pass
#     @classmethod
#     def test2(cls):
#         print(cls)
#     @staticmethod
#     def test3():
#         pass
#
# f=Foo()
# print(f.test1)
# print(Foo.test2)
# print(Foo.test3)
# print(f.test3)

#
# import settings
# class MySQL:
#     def __init__(self,host,port):
#         self.host=host
#         self.port=port
#         print('conneting...')
#     @classmethod
#     def from_conf(cls):
#         return cls(settings.HOST,settings.PORT) #MySQL('127.0.0.1',3306)
#     def select(self): #绑定到对象的方法
#         print(self)
#         print('select function')
#
# # conn=MySQL('192.168.1.3',3306)
# # conn.select()
#
# # conn1=MySQL('192.168.1.3',3306)
# conn2=MySQL.from_conf()









# import hashlib
# import time
# def create_id():
#     m=hashlib.md5(str(time.clock()).encode('utf-8'))
#     return m.hexdigest()

# print(time.clock())
# print(time.clock())
# print(time.clock())

# print(create_id())
# print(create_id())
# print(create_id())
# print(create_id())


# import hashlib
# import time
# import settings
# class MySQL:
#     def __init__(self,host,port):
#         self.id=self.create_id()
#         self.host=host
#         self.port=port
#         print('conneting...')
#
#     @staticmethod
#     def create_id(): #非绑定方法，就是类中的普通工具包
#         m=hashlib.md5(str(time.clock()).encode('utf-8'))
#         return m.hexdigest()
#
#     @classmethod
#     def from_conf(cls):
#         return cls(settings.HOST,settings.PORT) #MySQL('127.0.0.1',3306)
#     def select(self): #绑定到对象的方法
#         print(self)
#         print('select function')

# conn=MySQL('192.168.1.3',3306)
# conn.select()

# conn1=MySQL('192.168.1.3',3306)
# conn1=MySQL.from_conf()
# conn2=MySQL.from_conf()
# conn3=MySQL.from_conf()
# conn4=MySQL.from_conf()
#
# print(conn1.id)
# print(conn2.id)
# print(conn3.id)
# print(conn4.id)




#statcimethod 与classmethod的区别
# import settings
# class MySQL:
#     def __init__(self,host,port):
#         self.host=host
#         self.port=port
#         # print('conneting...')
#     # @classmethod
#     # def from_conf(cls):
#     #     return cls(settings.HOST,settings.PORT) #Mariadb('127.0.0.1',3306)
#
#     @staticmethod
#     def from_conf():
#         return MySQL(settings.HOST, settings.PORT)  # MySQL('127.0.0.1',3306)
#
#     # def __str__(self):
#     #     return '就不告诉你'
# # conn=MySQL.from_conf()
# # print(conn.host)
#
# class Mariab(MySQL):
#     # def __str__(self):
#     #     return 'host:%s port:%s' %(self.host,self.port)
#     pass
# conn1=Mariab.from_conf()
# print(conn1)











# class People:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
        def __str__(self):
            # print('run __str__')
            return 'name:%s age:%s' %(self.name,self.age)
#
# p=People('egon1',18)
# p1=People('egon2',28)
#
# print(p)
# print(p1)


# class Foo:
#     def __init__(self):
#         return 123 #抛出异常，不能有返回
#
# f=Foo()