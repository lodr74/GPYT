'''
>>> game.question(10)
"POINTS:6,TIMED:N - Obtain the contents of ./flag.txt.  To begin the challenge open a new terminal and
ssh (using a ssh client not Python) into the target host with a login of 'student1' and a password of 'student1'.
Obtain the IP address of the target host and an example of ssh client syntax by reading the data element.
HINT: This challenge is NOT to brute force the student ID number."

>>> game.data(10)

'Password:student1  - ssh student1@10.10.10.30'

'''

import pyWars
import os

def answer(data):
    return "$DINNER4SIX@SOMEWHEREINAUGUSTA$"



game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")
print(game.answer(10,answer(game.data(10))))
game.logout
