'''
>>> game.question(7)
'POINTS:1,TIMED:Y - Data element contains two characters.  Create a string that contains 100 of the first character and 50 of the second character.
Submit the 150 character string. '
>>> game.data(7)
'f b'

'''

import pyWars

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")

def answer(data):
    data_list = data.split()
    string = data_list[0]*100
    string = string + data_list[1]*50
    return string
    



print(game.answer(7,answer(game.data(7))))
game.logout
