'''
>>> game.question(55)
'NAME:Wireshanked - Read /home/student/Public/packets/sessions.pcap   It is so horribly broken that Wireshark can not reassemble the TCP streams.  You will have to use scapy to get the job done.
First use .sessions() to step through the packets.  Then put the packets back into the SEQ order.  Create a string that contains the payload of the streams in timestamped order followed by the value from .data().
Submit that as the answer.'

>>> game.data(55)
'21401
'''

import pyWars
from scapy.all import *


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")
pfile = "/home/student/Public/packets/sessions.pcap"

def answer1(data1):
    pkts = rdpcap(pfile)
    answer = ""
    print(pkts)
    for eachsession in sorted( pkts.sessions().values() , key = lambda x:x[0].time):
        plistsorted = sorted( eachsession, key = lambda x:x[TCP].seq)
        answer = answer + "".join([x[Raw].load.decode() for x in plistsorted if x.haslayer(Raw)])
    print(answer + data1)
    return answer + data1

'''
    for eachsession in sorted( pkts.sessions().values() , key = lambda x:x[0].time):
        plistsorted = sorted( eachsession, key = lambda x:x[TCP].seq)
        answer = answer + "".join([x[Raw].load.decode() for x in plistsorted if x.haslayer(Raw)])
'''
   

    
print(game.answer(55,answer1(game.data(55))))
game.logout