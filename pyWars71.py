'''
>>> game.question(71)
'NAME:JSON-Parsing - You queried a web base API that returns a URL encoded JSON string.
Decode the string, load the string as a json object, and return the 2nd index of the data element. '
>>> game.data(71)
'%7B%22message%22%3A+%22What+is+your+quest%22%2C+%22data%22%3A+%5B%22something+completely+different%22%2C+
%22welcome-to-sans%22%2C+%22thats+no+ordinary+rabbit%22%5D%2C+%22error%22%3A+%22thou+count+to+three%2C+no+more%2C+no+less%22%7D'

'''

import pyWars
import json
import urllib.parse
import re


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    print("The api string is : \n %s" % data1)
    print(urllib.parse.unquote(data1))
    x = urllib.parse.unquote(data1)
    x = x.replace("+","")
    y = json.loads(x)
    return y["data"][1]

print(game.answer(71,answer1(game.data(71))))

game.logout