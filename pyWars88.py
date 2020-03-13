'''
>>> game.question(88)
'How many bytes are required to store the character from .data()?'
>>> game.data(88)

>>> 

'''

import pyWars
import time

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
  return len(data1.encode('utf-8'))

        
print(game.answer(88,answer1(game.data(88))))
game.logout