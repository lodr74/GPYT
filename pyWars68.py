'''
>>> game.question(68)
"NAME:XORPart2 - Your client is using a simple XOR encoder to encrypt his data.
Just like in one of the earlier challenges, every byte in the data is XORed with
the exact same byte.   However, now you don't know what the key is.  But you do
know that his clear text data contains the string HTTP.    Determine the key,
unencrypt the data and return the customers clear text data. "

>>> game.data(68)
'SOOKzu;Z}irxzu;ti;^nitk~zu;Hlzwwtl$'

'''

import pyWars
import codecs

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")

def answer1(data1):
    print("The starting key is : %s" % data1)
    output = ""
    #print(":".join("{:02x}".format(ord(c)) for c in data1))
    x = 0
    while x < 256:
        data1 = game.data(68)
        for c in data1:
            output +=  chr(int(ord(c)) ^ x)
        if "HTTP" in output:
            print(game.answer(68,output))
            break
        x+=1
        output = ""

answer1(game.data(68))
game.logout