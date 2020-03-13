'''

>>> game.question(50)
"The data() method will return a string that you must convert to a scapy packet by calling 'somevar = Ether(.data())'.   Then extract the TCP Sequence number and submit it as the answer."

>>> game.data(50)
b"\x00PV\xad8\x8b\x00PV\xadC0\x08\x00U\xe5\x00(\x1a\xfe\x00\x00'\x06\xe4?\n\n\n\n\x1f\xd7O\xc3\x97\x1b\x94\x13\x93\x1e\xf3-\xb7\xdc\xd9AV\x02\x89^\xd7\x1c\x83\x1f"
>>

'''

import pyWars
import re
from scapy.all import *

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")

def answer1(data1):
    testvar = Ether(data1)
    return testvar[TCP].seq
    
    
print(game.answer(50,answer1(game.data(50))))
game.logout