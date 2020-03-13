'''
>>> game.question(54)
"The data() method will return a tuple.   The item in position 0 in the tuple is a list of strings that you must convert to a scapy
PacketList by executing something like this 'somevar = scapy.plist.PacketList([Ether(x) for x in tuple_position_zero])'.  The resulting
packets contain malformed IP packets containing a conversation between two hosts. You need to share these packets with a third party but
do not want to reveal the internal address of a sensitive server at 10.10.10.10.   After making it a scapy packet list change the IP address
10.10.10.10 in the pcap to the IP address given to you by .data().   The answer to this challenge is an MD5 hash of packets after you modified
address.  After you have changed all the 10.10.10.10 addresses, convert your packets into a single string, calculate the MD5 hash of that
string and submit that hash. For example, 'hashlib.md5(str(list(your packet variable)).encode()).hexdigest()' "

>>> game.data(54)
([b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00E\x00\x00<\xe6\xd0@\x00@\x06U\xe9\n\n\n\n\x7f\x00\x00\x01\xcc\x1d&\xaa5\xe5
\x19%\x00\x00\x00\x00\xa0\x02\xaa\xaa\xfe0\x00\x00\x02\x04\xff\xd7\x04\x02\x08\n\x02\xd2\xff\xf5\x00\x00\x00\x00\x01\x03\x03\x07',
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00E\x00\x00<\x00\x00@\x00@\x06<\xba\x7f\x00\x00\x01\n\n\n\n&\xaa\xcc\x1d\x0e
\xc9\x88\x925\xe5\x19&\xa0\x12\xaa\xaa\xfe0\x00\x00\x02\x04\xff\xd7\x04\x02\x08\n\x02\xd2\xff\xf6\x02\xd2\xff\xf5\x01\x03\x03\x07'],
'194.0.9.214')
>>> 
'''

import pyWars
import re
from scapy.all import *
import hashlib


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
   packet_list = data1[0]
   OIP = data1[1]
   print(packet_list)
   print(OIP)
   somevar = scapy.plist.PacketList([Ether(x) for x in packet_list])
   print(type(somevar))
   print(dir(somevar))
   print(somevar[IP])
   for i in somevar:
      print(type(i))
      print(i)
        #print(i.replace("10.10.10.10",IP))
      if i[IP].src == "10.10.10.10":
            i[IP].src = OIP
      elif i[IP].dst == "10.10.10.10":
            i[IP].dst = OIP
      else:
         print("I dont know what I am doing")
   print(str(list(somevar)))
   m = hashlib.md5()
   m.update(str(list(somevar)).encode())
   return m.hexdigest()

  
print(game.answer(54,answer1(game.data(54))))
game.logout