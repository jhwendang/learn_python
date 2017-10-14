# import spam


#import导入模块干的事：
'''
1.产生新的名称空间
2.以新建的名称空间为全局名称空间，执行文件的代码
3.拿到一个模块名spam，指向spam.py产生的名称空间
'''
# money=1000000000000000000000000000000000000000000
# print(spam.money)
# print(spam.read1)
# spam.read1()
# def read1():
#     print('from test.py')
# spam.read2()

#
# money=10
# spam.change()
# print(money)

import spam as x
# print(x.money)



# from ... import ...

# from spam import money,read1,read2,change

'''
1.产生新的名称空间
2.以新建的名称空间为全局名称空间，执行文件的代码
3.直接拿到就是spam.py产生的名称空间中名字
'''

'''
from ... import ...
优点:方便，不用加前缀
缺点：容易跟当前文件的名称空间冲突

'''

# print(money)
# read1()

# money=10
# del money
# print(money)


#
# def read1():
#     print('=========from test.py read1')
# read2()
# import time
# money=100
# print(money)
# time.sleep(200)
#
# read1=10000000
# from spam import read1
# read1()




# from spam import *
#
# print(money)
# read1()


# __all__=['money']
# from spam import *
# print(money)
#
# read1()