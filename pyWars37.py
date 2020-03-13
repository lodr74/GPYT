'''

'Data contains a comma separated list of user names and passwords in the format user1 :
password1, user2 : password2, etc.   One of those passwords is the answer.  Guess which one. '

>>> game.data(37)
'Aiden : 123456 , Jayden : porsche , Max : firebird , Riley : prince , Liam : rosebud , Ethan : password ,
Jack : guitar , Avery : butter , Dylan : beach , Caleb : jaguar , Addison : 12345678 , James : chelsea ,
Ryan : united , Andrew : froggy , NavajoElla : great , Ava : 1234 , Grace : black , Limabean : turtle ,
Emma : 7777777 , Elizabeth : cool , Genevieve : puddy , Aurora : diamond , Isabella : steelers , Bella : muffin ,
Charlotte : cooper '

'''

import pyWars
import codecs
import os
import gzip

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    lst = data1.split(",")
    i = 0
    res_dct = {}
    for i in lst:
        holder = i.split(":")
        res_dct[holder[0]] = holder[1]
    for i in res_dct:
        print("The answer is: %s" % res_dct[i])
        print(game.answer(37,res_dct[i]))
    
#print(game.answer(37,answer1(game.data(37))))
answer1(game.data(37))
game.logout