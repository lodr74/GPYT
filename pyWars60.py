'''
>>> game.question(60)
'NAME:Subprocess - Use the subprocess module to execute the command in data() and submit the results as a string. '

>>> game.data(60)
'uname -imnsp'


'''

import pyWars
import subprocess
import os


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")

def answer1(data1):
    print("Executing the following command: %s" % data1)
    try:
        datval = subprocess.Popen(data1, shell=True, stdout = subprocess.PIPE, stdin = subprocess.PIPE, stderr = subprocess.PIPE)
        exit_code = datval.wait()
        return str(datval.stdout.read().decode('ascii'))
    except OSError as err:
        print("OS error: {0}".format(err))
    else:
        print(game.answer(60,answer1(game.data(60))))
    
   
print(game.answer(60,answer1(game.data(60))))
game.logout