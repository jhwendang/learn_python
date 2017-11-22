import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #创建实例
server.bind(("0.0.0.0",8001))   #绑定ip端口
server.listen(5)                #监听消息
print("-------------start to listen..........")

while True:                           #循环可以一直通讯
    conn,client_addr = server.accept() #建立连接后在这个地方卡住，等待客户端连接
    print(conn,client_addr)

    while True:                       #循环收发信息，一次1024个字节没发送完
        try:
            data = conn.recv(1024)      #声明每一次接收1024字节，因为有时候是大文件
            print("recv from cli:",data.decode()) #先打印信息，下面再发送
            conn.send(b"got your msg")  #在python3里所以的socket发送都只能是bytes格式，所以加b
        except ConnectionResetError as e:
            print(e)
            break
