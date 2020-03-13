'''
>>> game.question(2)
'POINTS:2,TIMED:Y - The data element contains a URL.  Read the web page at that URL.  It will contain two numbers.  Add those two numbers together and submit the sum.'
>>> game.data(2)
'http://10.10.10.40/mathproblem.php?seed=728204'
'''

import pyWars
import requests

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")

def answer(data):
    r = requests.get(data)
    print(r.text)
    num1, num2 = r.text.encode('ascii','ignore').split(",")
    num1 = int(num1)
    num2 = int(num2)
    print(num1)
    print(num2)
    return num1+num2


print(game.answer(2,answer(game.data(2))))
game.logout
