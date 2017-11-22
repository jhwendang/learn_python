import socket
import subprocess
import struct
import json
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

            # conn.send(struct.pack('i',len(cmd_res))) #先报报头
            head_dic={'filename':None,'hash':None,'total_size':len(cmd_res)}
            head_json=json.dumps(head_dic)
            head_bytes=head_json.encode('utf-8')

            #先发送报头的长度
            conn.send(struct.pack('i',len(head_bytes)))

            #再发送报头的bytes
            conn.send(head_bytes)

            #最后发送真实的数据
            conn.send(cmd_res)

        except Exception:
            break
    conn.close()
phone.close()













