#!/usr/bin/python
# -*- coding:utf-8 -*-

#多态是同一种事物的多种形态
class Animal:
    def talk(self):
        print('正在叫')


class People(Animal):
    def talk(self):
        print('say hello')

class Pig(Animal):
    def talk(self):
        print('哼哼哼')

class Dog(Animal):
    def talk(self):
        print('汪汪汪')


class Cat(Animal):
    def talk(self):
        print('喵喵喵')

peo1=People()
pig1=Pig()
dog1=Dog()
cat1=Cat()


#多态性

# peo1.talk()
# dog1.talk()
# pig1.talk()


def func(x):
    x.talk()


func(peo1)
func(pig1)
func(dog1)
func(cat1)















