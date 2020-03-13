'''
>>> game.question(63)
"NAME:Socket2 - Start the 2nd socket challenge server by running '/opt/socketchallenge2' in your VM.
Next use the socket module to connect to 127.0.0.1 UDP port 4444 and submit the string from .data().
Then follow the instructions given when you read from the socket. Hint:Testing this with netcat first might help you understand the challenge.
Look at the string in .data() and then run 'nc -u 127.0.0.1 4444' "
>>> game.data(63)
'8715108'
>>>


root@573:/home/student/Public/registry# nc -u 127.0.0.1 4444 -vvvv
localhost [127.0.0.1] 4444 (?) open
8715108
You have 2 seconds to setup a TCP Server listening on port 5933.  I will transmit a large AES Encrypted file (CBC Block mode) to you in 2 seconds.
(Hint: from Crypto.Cipher import AES) Decrypt it to get the flag.  The AES key is the string 'decryptme1234567'.  The IV is the first 16 bytes.
The TCP port and encrypted file change every time you run this challenge.  The AES key is always the same.


'''

import pyWars
import socket
from Crypto.Cipher import AES
import select
import time
import base64
import re


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")

def recvall(dasocket, timeout=.1):
    data = dasocket.recv(1)
    dasocket.setblocking(0)
    starttime=time.time()
    while time.time()-starttime < timeout:
        try:
            newdata=dasocket.recv(1024*4)
            if len(newdata) == 0:
                break
        except:
            pass
        else:
            data+=newdata
            starttime = time.time()
    dasocket.setblocking(1)
    return data.decode()


def decrypt(efile):
    key = "decryptme1234567"
    iv = efile[:16]
    #print(iv)
    aes = AES.new(key, AES.MODE_CBC, iv)
    #decd = aes.decrypt(efile)
    return aes.decrypt(efile)

def setup_server(port):
    #print(port)
    port = port[0:-1]
    bport = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    bport.bind(("", int(port)))
    # was listen(5), but I set it to 1 to see if it makes it faster
    bport.listen(5)
    connection, fromaddr = bport.accept()
    #print(connection)
    efile = recvall(connection)
    #print(type(efile))
    #efile = base64.b64decode(efile)
    #print(type(efile))
    return base64.b64decode(efile)

def connector(data1):
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.sendto(data1.encode(), ("127.0.0.1", 4444))
    output = sock.recvfrom(1024)
    return output[0].decode()

def answer1(data1):
    #print("The first pin is: %s" % data1)
    output = connector(data1)
    output_list = output.split()
    #print(decrypt(setup_server(output_list[12])))
    echo = decrypt(setup_server(output_list[12]))
    echo = re.findall(b".('.*').", echo)
    echo = echo[0].decode("utf-8").strip("'")
    return echo

print(game.answer(63,answer1(game.data(63))))
game.logout