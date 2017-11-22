#!/usr/bin/python
# -*- coding:utf-8 -*-
# 语法错误导致的异常：应该在程序运行前就修正
# if
#
# print(
#
#
# def test:
#     pass


#逻辑上的异常：try .... except

# l=[1,2]
# l[10000000] #IndexError

# d={'a':1}
# d['b'] #KeyError


# 1/0  #ZeroDivisionError



# class Foo:
#     pass
#
# print(Foo.x) #AttributeError

# f=open('a.txt','w')
# f.close()
#
# f.write('asdfasdfasf')

# f=open('b.txt')

# msg=input('>>:')
# int(msg)
#
# 1+'asdfsadfasdf'



# try:
#     # msg=input('>>:')
#     # int(msg) #ValueError
#
#     # print(x) #NameError
#
#     d={'a':1}
#     d['b'] #KeyError
#
#     l=[1,2]
#     l[10] #IndexError
#
#     1+'asdfsadfasdf' #TypeError
#
# except ValueError as e:
#     print(e)
# except NameError:
#     print('NameError')
# except KeyError as e:
#     print(e)
#
# print('=============>')
# print('=============>')
# print('=============>')





#Exception万能异常
# try:
#     # msg=input('>>:')
#     # int(msg) #ValueError
#
#     # print(x) #NameError
#     #
#     # d={'a':1}
#     # d['b'] #KeyError
#     #
#     # l=[1,2]
#     # l[10] #IndexError
#
#     1+'asdfsadfasdf' #TypeError
#
# except Exception as e:
#     print(e)
#
# print('=============>')
# print('=============>')
# print('=============>')




# try:
#     # msg=input('>>:')
#     # int(msg) #ValueError
#     #
#     # print(x) #NameError
#     #
#     # d={'a':1}
#     # d['b'] #KeyError
#     #
#     # l=[1,2]
#     # l[10] #IndexError
#     #
#     # 1+'asdfsadfasdf' #TypeError
#     print('aaaaaa')
#
# except ValueError as e:
#     print(e)
# except NameError:
#     print('NameError')
# except KeyError as e:
#     print(e)
# except Exception as e:
#     print('Exception======>',e)
# else:
#     print('没有异常时发生会执行')
# finally:
#     print('有没有异常都会执行')
#
#
# print('=============>')
# print('=============>')
# print('=============>')


# try:
#     f=open('a.txt')
#     next(f)
#     next(f)
#     next(f)
#     # next(f)
# finally:
#     print('finally run')
#     f.close()


try:
    # msg=input(">>: ")
    # if msg.isdigit():
    #     int(msg)
    # if #Exception无法匹配语法的异常,语法异常应该在程序运行前就解决掉
except Exception as e:
    print('ee')