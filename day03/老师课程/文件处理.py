#!/usr/bin/python
# -*- coding:utf-8 -*-

# f=open('a.txt','r+') #读写
# f=open('a.txt','w+') #写读
# f=open('a.txt','a+') #追加并且读

# f=open('a.txt','w')
# f.write('111111\n')
# f.close()


#上下文管理
# with open('a.txt','r',encoding='utf-8') as f,open('b.txt') as b_f:
#     # print(f.read())
#     print('====>')

#补充
# for i in range(3):
#     print(i)
#     # continue
#     if i == 1:
#         break
# else:
#     print('=============>') #当for循环不被break打断，就会执行else的代码
#
# with open('a.txt','r',encoding='utf-8') as read_f,\
#         open('aa.txt','w',encoding='utf-8') as write_f:
#
#     for line in read_f:
#         write_f.write(line)
#     else:
#         print('write successfull')

# i=0
# while i< 5:
#     print(i)
#     i+=1
#     if i == 3:
#         break
# else:
#     print('------>')




# with open('a.txt','rb') as f:
#     print(f.read().decode('utf-8'))

# with open('c.txt','wb') as f:
#     f.write('哈哈哈'.encode('utf-8'))

# f=open('sb.jpg','r',encoding='utf-8') #文本的方式读不了二进制文件
# print(f.read())

# with open('sb.jpg','rb') as read_f,\
#         open('sb_alex.jpg','wb') as write_f:
#     data=read_f.read()
#     write_f.write(data)



#不常用的，了解

# with open('a.txt','r',encoding='utf-8') as f:
#     print(f.read(4)) #数字指的是读的是字符
#
# with open('a.txt','rb') as f:
#     print(f.read(1)) #数字指的是读的是字符


# with open('a.txt','r',encoding='utf-8') as f:
#     f.seek(3) #seek内指定的数字代表字节
#     print(f.tell()) #当前光标所在的位置
#     print(f.read())

# with open('aa.txt','r+',encoding='utf-8') as f:
#     # f.seek(3) #seek内指定的数字代表字节
#     # print(f.read())
#
#     f.truncate(1)


# with open('b.txt','rb') as f:
    # f.read()
    # f.seek(3) #默认情况，是以文件起始位置作为开始，往后移动3个bytes
    # f.read(1)
    # print(f.tell())
    # f.seek(2,1) #1 代表以当前光标所在的位置为开始，往后移动2个 bytes
    # print(f.tell())

    # f.seek(-1,2) #2表以当前光标所在的位置为开始，往后移动2个 bytes
    # print(f.tell())

    # f.seek(0,2)

# with open('c.txt','r',encoding='utf-8') as f:
#     f.seek(0,2)
#     print('====>',f.read())


# tail -f access.log
import time
with open('access.log','r',encoding='utf-8') as f:
    f.seek(0,2)
    while True:
        line=f.readline().strip()
        if line:
            print('新增一行日志',line)
        time.sleep(0.5)
