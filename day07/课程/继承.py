#!/usr/bin/python
# -*- coding:utf-8 -*-

# #什么是继承：一种创建新的类的方式
# class ParentClass1:
#     pass
# class ParentClass2:
#     pass
#
# class SubClass1(ParentClass1):
#     pass
# class SubClass2(ParentClass1,ParentClass2):
#     pass
#
# print(SubClass1.__bases__)
# print(SubClass2.__bases__)


# #python2中类分为：新式类与经典类
# class Foo(object): #新式类，有父类
#     pass
#
# class Bar:         #经典类，无父类
#     pass

#python3中类全都是新式类
# class Foo:         #新式类，默认继承object
#     pass
#
# print(Foo.__bases__)




#寻找继承关系


#继承的好处一：减少冗余代码
#在子类定义新的属性，覆盖掉父类的属性,称为派生
# class Animal:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def eat(self):
#         print('eating')
#
#     def talk(self):
#         print('%s 正在叫' %self.name)
#
#
# class People(Animal):
#     def __init__(self, name, age, sex,education):
#         Animal.__init__(self,name,age,sex)
#         self.education=education
#
#     def talk(self):
#         Animal.talk(self)
#         print('%s say hello' %self.name)
#
# class Pig(Animal):
#     pass
#
# class Dog(Animal):
#     pass
#
#
# peo1=People('alex',18,'male','小学肄业') #People.__init__
#
# pig1=Pig('wupeiqi',20,'female')
#
# dog1=Dog('yuanhao',30,'male')
#
# print(peo1.education)
#
#
# peo1.talk()
# pig1.talk()
# dog1.talk()




#下列代码的结果是
# class Parent:
#     def foo(self):
#         print('Parent.foo')
#         self.bar()             #s.bar()
#
#     def bar(self):
#         print('Parent.bar')
#
# class Sub(Parent):
#     def bar(self):           #重写了bar，而且自己也有s.bar，就调用这儿的
#         print('Sub.bar')
#
# s=Sub()
#
# s.foo() #s.foo









class Sub:
    def __init__(self):
        self.bar=1
    def bar(self):
        print('Sub.bar')

s=Sub()
s.bar()    #这儿会执行__init__得到 s.bar=1 。所以1()会报错

# print(s.__dict__)  #结果{'bar': 1}   #在这找bar：  s.__dict__['bar']






#
# class Animal:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def eat(self):
#         print('eating')
#
#     def talk(self):
#         print('%s 正在叫' %self.name)
#
#
# class People(Animal):
#     def __init__(self, name, age, sex,education):
#         Animal.__init__(self,name,age,sex)
#         self.education=education
#
#     def talk(self):
#         Animal.talk(self)
#         print('%s say hello' %self.name)
#
# class Pig(Animal):
#     pass
#
# class Dog(Animal):
#     pass
#
#
# peo1=People('alex',18,'male','小学肄业') #People.__init__
# pig1=Pig('wupeiqi',20,'female')
# dog1=Dog('yuanhao',30,'male')


# print(isinstance(peo1,People))
# print(isinstance(pig1,Pig))
# print(isinstance(dog1,Dog))


# print(isinstance(peo1,Animal))
# print(isinstance(pig1,Animal))
# print(isinstance(dog1,Animal))


#继承反映的是一种什么是什么的关系
#组合也可以解决代码冗余问题，但是组合反映是一种什么有什么的关系

# class People:
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#
# class Teacher(People):
#     def __init__(self,name,age,sex,salary):
#         People.__init__(self,name,age,sex)
#         self.salary=salary
#
# class Student(People):
#     pass



#
#
# class Date:
#     def __init__(self,year,mon,day):
#         self.year=year
#         self.mon=mon
#         self.day=day
#
#     def tell(self):
#         print('%s-%s-%s' %(self.year,self.mon,self.day))
#
# class Teacher(People):
#     def __init__(self,name,age,sex,salary,year,mon,day):
#         self.name=name
#         self.age=age
#         self.sex=sex
#         self.salary=salary
#         self.birth=Date(year,mon,day)
#
# class Student(People):
#     def __init__(self,name,age,sex,year,mon,day):
#         self.name=name
#         self.age=age
#         self.sex=sex
#         self.birth=Date(year,mon,day)

# t=Teacher('egon',18,'male',3000,1995,12,31)
# t.birth.tell()








# class File:#定义接口Interface类来模仿接口的概念，python中压根就没有interface关键字来定义一个接口。
#     def read(self): #定接口函数read
#         raise TypeError('类型错误')
#
#     def write(self): #定义接口函数write
#         raise TypeError('类型错误')
#
#
# class Txt(File): #文本，具体实现read和write
#     def read(self):
#         print('文本数据的读取方法')
#
#     def write(self):
#         print('文本数据的读取方法')
#
# class Sata(File): #磁盘，具体实现read和write
#     def read(self):
#         print('硬盘数据的读取方法')
#
#     def write(self):
#         print('硬盘数据的读取方法')
#
# class Process(File):
#     # def read(self):
#     #     print('进程数据的读取方法')
#     #
#     # def write(self):
#     #     print('进程数据的读取方法')
#     def xie(self):
#         pass
#
#     def du(self):
#         pass
# p=Process()
# p.read()


# t=Txt()
# p=Process()
# d=Sata()
#
# print(isinstance(t,File))
# print(isinstance(p,File))
# print(isinstance(d,File))
#
#
#
# t.read()
# p.read()
# d.read()






#抽象类
# import abc
# class File(metaclass=abc.ABCMeta):#定义接口Interface类来模仿接口的概念，python中压根就没有interface关键字来定义一个接口。
#     @abc.abstractmethod
#     def read(self): #定接口函数read
#         pass
#
#     @abc.abstractmethod
#     def write(self): #定义接口函数write
#         pass
#
# class Process(File):
#     def read(self):
#         # print('进程数据的读取方法')
#         pass
#     def write(self):
#         print('进程数据的读取方法')
#
#     # def xie(self):
#     #     pass
#     #
#     # def du(self):
#     #     pass
# p=Process()
# p.read()



#继承的实现原理
#
# class E:
#     # def test(self):
#     #     print('from E')
#     pass
#
# class A(E):
#     # def test(self):
#     #     print('from A')
#     pass
# class D:
#     # def test(self):
#     #     print('from D')
#     pass
# class B(D):
#     # def test(self):
#     #     print('from B')
#     pass
# class C:
#     # def test(self):
#     #     print('from C')
#     pass
#
# class F(A,B,C):
#     # def test(self):
#     #     print('from F')
#     pass
# f=F()
# f.test()



# class A:
#     def test(self):
#         print('from A')
#
#
# class B(A):
#     # def test(self):
#     #     print('from B')
#     pass
# class C(A):
#     # def test(self):
#     #     print('from C')
#     pass
#
# class D(B):
#     # def test(self):
#     #     print('from D')
#     pass
#
# class E(C):
#     # def test(self):
#     #     print('from E')
#     pass
# class F(D,E):
#     # def test(self):
#     #     print('from F')
#     pass
# f=F()
# f.test()





#经典类：深度优先，F->D->B->A->E->C->H
#新式类：广度优先，F->D->B->E->C->H->A
# class A:
#     # def test(self):
#     #     print('from A')
#     pass
# class B(A):
#     # def test(self):
#     #     print('from B')
#     pass
# class C(A):
#     # def test(self):
#     #     print('from C')
#     pass
#
# class D(B):
#     # def test(self):
#     #     print('from D')
#     pass
#
# class E(C):
#     # def test(self):
#     #     print('from E')
#     pass
#
# class H(A):
#     def test(self):
#         print('from H')
#     pass
# class F(D,E,H):
#     # def test(self):
#     #     print('from F')
#     pass
# f=F()
# f.test()
# print(F.mro())

#新式类：广度优先，F->D->B->E->C->H->A



# class Foo1:
#     def test(self):
#         print('from foo.test')
#
#
# class Bar(Foo1):
#     def test(self):
#         # Foo.test(self)
#         # super().test()
#         super(Bar,self).test()
#         print('bar')

# b=Bar()
# b.test()





# class Foo1:
#     # def test(self):
#     #     print('from foo1.test')
#     pass
# class Foo2:
#     def test(self):
#         print('from foo2.test')
#
#
# class Bar(Foo1,Foo2):
#     def test(self):
#         # Foo1.test(self)
#         # Foo2.test(self)
#         super().test()
#         print('bar')
# print(Bar.mro())
# b=Bar()
# b.test()







