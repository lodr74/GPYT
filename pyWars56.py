'''
>>> game.question(56)
'Open the SOFTWARE registry file stored in the /home/student/Public/registry directory.  Build a sorted list of subkeys names at the root of this file.
What is the name of the key in position .data()? '
>>> game.data(56)
17
>>>
'''

import pyWars
from Registry import Registry


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")
rdir = "/home/student/Public/registry"
rkey = "/home/student/Public/registry"

def answer1(data1):
    handle = Registry.Registry("/home/student/Public/registry/SOFTWARE")
    regkey = handle.open("")
    srtd_regkey = (sorted(list(map(lambda x:x.name(), regkey.subkeys()))))
    return srtd_regkey[data1]

    
print(game.answer(56,answer1(game.data(56))))
game.logout