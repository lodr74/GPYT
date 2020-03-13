'''
>>> game.question(6)
'POINTS:1,TIMED:Y - The data element contains two lists.  Calculate the sum of each list independently.
Submit the sum of each list separated by a comma ( ie <sum1>,<sum2).   For example [[1,1][2,2]] -> 2,4 '
>>> game.data(6)
[[9, 9, 20, 71, 31, 63], [68, 52, 11]]
>>>
'''

import pyWars

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")

def answer(data):
    return str(sum(data[0])) + "," + str(sum(data[1]))



print(game.answer(6,answer(game.data(6))))
game.logout
