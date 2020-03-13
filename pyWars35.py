'''

'The Data() method will return a tuple.  The first item in the tuple contains the absolute path of a
gzip compressed file in your virtual machine.  The second item in the tuple is a line number.  Retreieve
that line number from the specified file and submit it as a string.'



('/home/student/Public/log/dmesg.2.gz', 25)

'''

import pyWars
import codecs
import gzip

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    i = 0
    x = gzip.open(data1[0],"rt")
    print(data1)
    y = x.readlines()
    #print("The length of y is: %d: " % len(y))
    z = y[data1[1]-1]
    print(z)
    return z
            
print(game.answer(35,answer1(game.data(35))))
game.logout