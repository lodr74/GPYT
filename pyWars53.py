'''
>>> game.question(53)
'Read /home/student/Public/packets/web.pcap  Commands are embedded in the packet payloads between the tags <command> and </command>.  The .data() method will give you a command number.
Submit that command as a string as the answer.  For example if .data() is a 5 you submit the 5th command that was transmitted.  Ignore blank commands (ie <command></command>).'

>>> game.data(53)
13
'''

import pyWars
import re

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")
from scapy.all import *

def answer1(data1):
    print(data1)
    #print(type(data1))
    pfile = rdpcap("/home/student/Public/packets/web.pcap")
    sessions = pfile.sessions()
    sfind = r"<command>(.*?)</command>"
    counter = 0
    #print(sfind)
    for i in sessions:
        for packet in sessions[i]:
            command = re.findall(sfind,str(packet[TCP].payload))
            if len(command) == 0:
                pass
            else:
                if counter < data1-1:
                    counter = counter + 1
                else:
                    print(command)
                    return command[0]

  
print(game.answer(53,answer1(game.data(53))))
game.logout