import socket

client = socket.socket()
client.connect(("127.0.0.1",8001))

while True:
    msg = input(">>:").strip()
    if len(msg) == 0:continue   #如果长度等于0，表示没输入信息，continue跳出此次循环，不发送
    client.send(msg.encode())    #encode变成字节发送
    print("send",msg)
    data = client.recv(1024)   #客户端收，1024字节
    print("res:",data.decode())
    total_size = int(data.decode())

    received_size = 0
    res = b''
    while  received_size < total_size:
        d = client.recv(1024)
        res += d
        f.write(d)

        received_size += len(d)
    print("---------rece done---------")
    print(res.decode())
