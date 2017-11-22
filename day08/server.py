#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther : Jianghao
# Date : 2017/11/17

import socket
import subprocess
import struct
import json

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #创建实例
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #解决四次挥手的time_wait状态在占用地址问题(客户端还没来及关闭)
server.bind(('0.0.0.0',8001))                              #绑定ip端口
server.listen(5)                                           #监听连接队列,半连接池，最多接受5个
print("-------------start to listen..........")

while True:                              #连接循环，可以一直建立
    conn,client_addr = server.accept()    #建立连接后在这个地方卡住，等待客户端连接
    print(conn,client_addr)               #打印连接对象和客户端地址
    while True:                          #循环收发信息，与conn的通信循环
        try:                              #针对windows平台下客户端断开链接，try监控异常，这样就可以输出错误但不会中断（避免conn的此次连接被客户端破坏掉了，服务端还要用时的异常终止）
            client_msg = conn.recv(1024)   #声明每一次接收1024字节，因为有时候是大文件
            if not client_msg:break      #针对linux系统平台下客户端断开链接,linux客户端单方面断开并不会抛异常，上面的recv也不会阻塞，会一直收空然后死循环。所以判断为空则break
            msg = client_msg.decode()     #bytes转换成字符串，统一默认utf-8
            print('recv from client: %s' %msg)      #先打印信息，下面再发送
            # subprocess.run(msg)                   #在linux上运行命令，但不保存结果,不用这个
            res_obj = subprocess.Popen(msg, shell=True, stdout=subprocess.PIPE,     #在linux上执行命令，标准正确输出
                                                         stderr=subprocess.PIPE)     #标准错误输出
            err = res_obj.stderr.read()                                             #read错误结果
            if err:                                                                #如果存在错误，则输出错误，下面的不存在则输出正确
                res = err
            else:
                res = res_obj.stdout.read()                                         #read正确结果,注意客户端需要decode转成字符串并且用服务端对应平台编码
            #######直接发送数据长度，但若是特别长的报头数据struct打出的包不够长
            ## conn.send(str(len(res)).encode())            #方法1.发送长度过去,只能发送bytes格式，encode又只能是对字符串 ---》这种不能固定长度的长度，会黏包
            # conn.send(struct.pack('i', len(res)))         #方法2.发送长度过去,只能发送bytes格式 --》把len的长度打成固定长度的bytes包
            #######所以需要把报头长度发送过去，再发送报头，再发送数据。通过报头长度得到报头数据，通过报头数据再得到数据长度
            head_dic = {'filename':None, 'hash':None, 'total_size':len(res)}  #自定义报头格式，前面的随意，可以只定义长度'total_size'
            #报头数据转成字符串（字典转字符串用json），便于socket传输
            head_json = json.dumps(head_dic)
            #为避免报头过长struct把报头的长度打成固定长度的bytes包发送过去
            conn.send(struct.pack('i', len(head_json)))
            #发送报头数据
            conn.send(head_json.encode('utf-8'))
            conn.send(res)                                #发送内容，res本身就是bytes，不用encode
            # conn.send('真是！！！'.encode())            #发送信息，在python3里所有的socket发送都只能是bytes格式，所以要么加b''要么encode
        except ConnectionResetError as e:
            print(e)
        # except Exception:                               #也可以这样，用万能异常，不输出异常
            break                                        #出问题，中断所在循环接受下一个连接
    conn.close()                                      #中断循环后关闭此次conn连接

server.close()                                            #关闭实例