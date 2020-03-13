'''

>>> mygame.question(41)
'Sentences end in a punctuation (period, question mark or exclamation mark) followed by two spaces.
Data contains a paragraph with multiple sentences.  Use a regular expression to findall() sentences
and submit a list of sentences. '

>>> mygame.data(41)
"Punctation characters includes all of the following: '?!.'.  PI is 3.1415.  PI is 3.1415.  "
>>> 

'''

import pyWars
import re

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    print(data1)
    regex = re.findall(r"[A-Za-z0-9].+?\w*[.?!]\s\s",data1)
    #print(regex)
    return regex
        
print(game.answer(41,answer1(game.data(41))))
game.logout