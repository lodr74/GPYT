'''
'Data will give you a Python 2 string. Submit a Python 3 string.'
>>> game.data(85)
b'run away! run away!'


'''

import pyWars
import time

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
  return data1.decode('utf8')

        
print(game.answer(85,answer1(game.data(85))))
game.logout