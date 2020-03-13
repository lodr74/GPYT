'''
>>> game.question(86)
'Data will give you a Python 3 string. Submit a Python 2 string.'
>>> game.data(86)
'spam spam spam spam'
>>>

'''

import pyWars
import time

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
  return data1.encode('utf8')

        
print(game.answer(86,answer1(game.data(86))))
game.logout