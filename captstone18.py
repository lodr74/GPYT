'''
'POINTS:6,TIMED:Y - After connecting to the target URL several cookies will be set in your browser.
They will all have the name pywars_XXXX where XXXX is a number.  Sort all of the cookies in numerical
order and add the values of those cookies into a single string.  Then base64 decode the string by adding
together those strings in the cookie values.  Some additional decoding may also be required.
To begin connect to the target server and examine the cookies set in your browser.
The url of the target server is specified in the data element. '


'''

import pyWars
import requests
import base64
from urllib import unquote

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")

    

def answer(data):
    newString = ''
    url = data
    s = requests.Session()
    output = s.get(url)
    cookies = s.cookies.get_dict()
    for k, v in cookies.items():
        newString+=v
    print(newString)
    deCoded = base64.b64decode(unquote(newString).decode('utf8'))
    print(deCoded)
    return deCoded
    
        


print(game.answer(18,answer(game.data(18))))
game.logout
