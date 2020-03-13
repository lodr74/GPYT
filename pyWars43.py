'''

'Data contains a several entries with strings and integers. Each entry is separated by an exclamation mark.
Break each string every x characters where x is the integer after the comma.  For example 123456,2 becomes the list ["12", "34", "56"].
Submit a list of lists as the answer [[list for first entry],[list for second entry],[list for third entry]].  '

>>> mygame.data(43)
'ztq46y7anrr67cx5v0t77g4e,6!wcce1yg6c224xk4vt4pwpov8xt8yue,6!g0xn9bmd,2!4s9j90pi5kufmwtxtgekvf7b4pu16h,5'


'''

import pyWars
import re

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    data_set = data1.split('!')
    data_list = []
    final_list = []
    for i in data_set:
        data_list.append(i.split(','))
    for i in data_list:
        string = i[0]
        n = int(i[1])
        entry = [(string[i:i+n]) for i in range(0, len(string), n)]
        final_list.append(entry)
    return final_list

        
print(game.answer(43,answer1(game.data(43))))
game.logout