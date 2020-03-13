'''
"Data contains a dictionary of dictionaries.  The outer dictionary contains dates in the format of Month-Year.
The value for each of those entries is another dictionary.  That dictionary contains Operating System classes as
the key and its percentage of use in the target organization as the value.  What percentage of the attack surface
was 'Vista' in '6-2017'?"

'''

import pyWars
import codecs

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    x = data1.get('6-2017').get('Vista')
    return x
            
print(game.answer(31,answer1(game.data(31))))
game.logout