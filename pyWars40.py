'''

"Read the data element and submit the number of times any instance of the word
'python' (case insensitive) appears in the source. "


>>> mygame.data(41)
"Punctation characters includes all of the following: '?!.'.  PI is 3.1415.  PI is 3.1415.  "
>>> 

'''

import pyWars
import re

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    regex = re.findall(r'python',data1,re.IGNORECASE)
    print(len(regex))
    return len(regex)
    
        
print(game.answer(40,answer1(game.data(40))))
game.logout