'''

Data() contains the absolute path of a filename in your virtual machine.
Determine the length of the file at that path. Open and read the contents
of the file. Submit the file size (length of contents) as the answer.

>>> mygame.data(33)
'/home/student/Public/espeak-generic.conf'

'''

import pyWars
import codecs
import os

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    x = open(data1,'r').read()
    print(x)
    size = os.path.getsize(data1)
    return size
            
print(game.answer(33,answer1(game.data(33))))
game.logout