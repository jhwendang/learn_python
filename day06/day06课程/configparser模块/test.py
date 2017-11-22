#!/usr/bin/python
# -*- coding:utf-8 -*-
import configparser
config=configparser.ConfigParser()
config.read('a.ini')




# print(config.sections())
# print(config.options('section1'))
# print(config.items('section1'))

#
# print(config.get('section1','db'))
# print(type(config.get('section1','db')))
# print(type(config.getint('section1','max_conn')))
# print(config.getint('section1','max_conn'))
# print(config.getboolean('section1','enable'))
# print(config.has_option('section1','enable'))
# print(config.remove_option('section1','enable'))



config.add_section('egon')
config.set('egon','name','egon')
config.set('egon','age','18')

config.write(open('b.ini','w'))

config=configparser.ConfigParser()
config.read('b.ini')

print(config.getint('egon','age'))
print(type(config.getint('egon','age')))