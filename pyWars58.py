'''
>>> game.question(58)
'Open the SOFTWARE registry file stored in the /home/student/Public/registry directory. Ignoring case,
submit a sorted list of all of the wireless SSIDs (FirstNetwork) in the Unmanaged network profile that
begin with the letter in .data()'

>>> game.data(58)
'r'
>>>

'''

import pyWars
from Registry import Registry


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")
rdir = "/home/student/Public/registry"
rkey = "/home/student/Public/registry"

def answer1(data1):
    print("Searching the Unmanaged network for networks that begin with: %s" % data1)
    handle = Registry.Registry("/home/student/Public/registry/SOFTWARE")
    regkey = r"Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged"
    SSID = []
    for eachsubkey in handle.open(regkey).subkeys():
        SSID.append(eachsubkey.value("FirstNetwork").value())
    print("The SSID list is:")
    print(SSID)
    result = sorted(filter(lambda x: x.casefold().startswith(data1), SSID))
    return result

    
print(game.answer(58,answer1(game.data(58))))
game.logout