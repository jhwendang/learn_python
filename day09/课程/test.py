# import paramiko
#
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect('120.92.113.180', 22, 'root', 'QWE123asd')
# stdin, stdout, stderr = ssh.exec_command('df')
# print(stdout.read().decode('utf-8'))
# ssh.close()



import os,sys
import paramiko

t = paramiko.Transport(('120.92.113.180',22))
t.connect(username='root',password='QWE123asd')
sftp = paramiko.SFTPClient.from_transport(t)
# sftp.put(r'C:\Users\Administrator\Desktop\1.txt','/tmp/1.txt')
sftp.get(r'/tmp/aaa.txt','aaa.txt')
t.close()
