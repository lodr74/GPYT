'''
>>> game.question(57)
'Open the SOFTWARE registry file stored in the /home/student/Public/registry directory.
The .data() contains the name of a value in the key Microsoft\\Windows NT\\CurrentVersion\\Winlogon.  Submit its value.'
>>> game.data(57)
'DisableBackButton'
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
    regkey = handle.open("Microsoft\\Windows NT\\CurrentVersion\\Winlogon")
    reg_value = regkey.value(data1)
    print(reg_value.value())
    return reg_value.value()

    
print(game.answer(57,answer1(game.data(57))))
game.logout