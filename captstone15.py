'''
>>> game.question(15)
'POINTS:6,TIMED:Y - Download the packet capture file from http://10.10.10.30/packetchallenge1.pcap.
You can download it manually using the web browser of your choice.   The data element contains an
integer representing an destination port number.  The solution is the string obtained by assembling
all characters transmitted to the DESTINATION PORT in the packet capture. '

>>> game.data(15)
'PORT=1038'
>>>




'''

import pyWars
from scapy.all import *

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")

    

def answer(data):
    port = data.split("=")
    print(port[1])
    pfile = '/home/student/Downloads/packetchallenge1.pcap'
    pcap = rdpcap(pfile)
    string = ''
    for pkts in pcap:
        if pkts.haslayer(TCP):
            if str(pkts.dport) == str(port[1]):
                string+=str(pkts[TCP].payload)
    string = string.split("=")
    return string[1]
        


print(game.answer(15,answer(game.data(15))))
game.logout
