import socket
import subprocess
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #买手机
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
phone.bind(('127.0.0.1',8080)) #插电话卡
phone.listen(5) #开机，backlog
while True:
    print('starting....')
    conn,addr=phone.accept()
    print('cliet addr',addr)
    while True:
        try:
            cmd=conn.recv(1024)
            if not cmd:break
            res=subprocess.Popen(cmd.decode('utf-8'),shell=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
            err=res.stderr.read()
            if err:
                cmd_res=err
            else:
                cmd_res=res.stdout.read()

            conn.send(cmd_res) #发消息
        except Exception:
            break
    conn.close()
phone.close()













