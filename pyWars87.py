'''
>>> game.question(87)
'What is the ordinal value of the 5th character in the .data()?'
>>> game.data(87)

>>> 

'''

import pyWars
import time

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
  chr_list = []
  for i in data1:
    chr_list.append(i)
  print(len(chr_list[4]))
  print(ord(chr_list[4]))
  return ord(chr_list[4])

        
print(game.answer(87,answer1(game.data(87))))
game.logout