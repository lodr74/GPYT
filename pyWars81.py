'''
"NAME:Botnet-Encode - To begin this challenge start the program /opt/bot.  This bot listens for commands on TCP port 4444.
It uses the same encoding scheme from the previous question (Botnet-Decode).  If you haven't successfully deciphered that
message yet you should do that question first.   Once you understand the coding scheme come back.  You must encode a message
telling the bot to release the hosts on your network, then transmit it to the bot. The .data() element will contain the command
required to release hosts on your network.  Read the command from .data() then connect to the bot on port 4444 and transmit an
encoded message containing that command.  If the format of your encoded message is correct the server will give you back a response
regardless of whether your command is encoded properly.  Submit the response code from the bot as the answer.  If pyWars says the
answer is incorrect then you did not encode the message properly."
>>> game.data(81)
'purge_network(264)'

'''

import pyWars
import os
import socket

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    sock = socket.socket()
    port = 4444
    print("Connecting to data stream on port %i...." % port, flush=True)
    sock.connect(("127.0.0.1", port))
    print(sock.recv(1000).decode())
    msg = data1
    key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:len(msg)]
    enc = ['a'] * 200
    #cmd 
    for pos, eachlet in enumerate(msg):
        distance = ord(eachlet)
        offset = 0
        spacefound = False
        while not spacefound:
            spacefound = (enc[offset] == "a") and (enc[offset+distance] == 'a')
            if spacefound:
                enc[offset] = enc[offset+distance] = key[pos]
            offset += 1
    cmd = ("".join(enc),key)
    #print("Sending cmd: %s" % cmd, flush=True) 
    sock.send(str(cmd).encode())
    output = sock.recv(1000).decode()
    print(output)
    return output.split(":")[1]
        
print(game.answer(81,answer1(game.data(81))))
game.logout