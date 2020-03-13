'''
>>> game.question(20)
"POINTS:8,TIMED:Y - Transmit a UDP packet to 10.10.10.40 with the data() as the packet payload.
Your IP must be the source address and both the source and destination port must be 0.
You can use scapy to craft and send this packet by doing something like this 'send(IP(dst='10.10.10.40')/UDP(dport=0,sport=0)/<variable>.data(20))'.
The server will then transmit packets back to your address. Sniff the 3 packets sent by the server that contain the string SNIFF_CHALLENGE-<an integer>.
Example SNIFF_CHALLENGE-2341235.   The answer is a list that contains 3 strings.  The 3 strings are the integers in the order they were transmitted.
Example: ['2341235,'34123356','2928743']"
>>> game.data(20)
'START_CTF_CHALLENGE-99694189'


'''

import pyWars
from scapy.all import *
import re
import sys

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")
output = []

def pfilter(pkts):
    if pkts.haslayer("Raw"):
        item = re.findall(r"SNIFF_CHALLENGE-(\d+)",(pkts[Raw].load))
        output.append(item[0])
        print(output)
        if len(output) == 3:
            print(game.answer(20, output))
            sys.exit()

def answer(data):
    command = data
    p = send(IP(dst='10.10.10.40')/UDP(dport=0,sport=0)/data, verbose=False)
    #pkts = sniff(filter="host 10.10.10.40 and udp", prn=lambda x:x.sprintf("{IP:%IP.src% -> %IP.dst%\n}{Raw:%Raw.load%\n}"))
    pkts = sniff(filter="src host 10.10.10.40", prn=pfilter)
    
    

print(game.answer(20,answer(game.data(20))))
game.logout
