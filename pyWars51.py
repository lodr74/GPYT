'''

>>> game.question(51)
"The data() method will return a string that you must convert to a scapy packet by calling 'somevar = Ether(.data())'.   Submit the payload of the packet."

>>> game.data(51)
b'\x00PV\xad8\x8b\x00PV\xadC0\x08\x00\x05/\x00>h"\x00\x00\x0b\x06W9\n\n\n\n\xb4\xddg?w\xc3\x04Dw\xc34\xd8\xfe\xcf\xc4\xa0Z\x02\x1d)\xa4\\g\xb6killall -9 perl4017048'
>>>
'''

import pyWars
import re
from scapy.all import *

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")

def answer1(data1):
    testvar = Ether(data1)
    return testvar[IP].load
    
    
print(game.answer(51,answer1(game.data(51))))
game.logout