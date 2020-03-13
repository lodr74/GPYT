'''
>>> game.question(59)
'Open the NTUSER.DAT registry file stored in the /home/student/Public/registry directory.
Submit the sum of all the values in the key specified in .data()'

>>> game.data(59)
u'ROOT\\SOFTWARE\\REGLAB\\Software\\Startup\\Dialog'

'''

import pyWars
from Registry import Registry


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")

def answer1(data1):
    print(type(data1))
    regkey = data1
    print(regkey)
    print("Searching the regsitry key: %s" % regkey)
    handle = Registry.Registry("/home/student/Public/registry/NTUSER.DAT")
    #print(type(handle))
    #print(dir(handle))
    x = 0
    regfuk = handle.open(regkey[5:])
    #print(type(regfuk))
    #print(dir(regfuk))
    datval = (sum(map(lambda x:int(x.value()), regfuk.values())))
    return datval
   
print(game.answer(59,answer1(game.data(59))))
game.logout