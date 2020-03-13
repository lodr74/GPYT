'''
>>> game.question(3)
"POINTS:2,TIMED:Y - The data element contains a phrase.
Reverse each individual word in the sentence but not the sentence itself.
So 'This is a Test' becomes 'sihT si a tseT'.  Submit that value."
>>> game.data(3)
'What are you going to do, bleed on me?'
>>>
'''

import pyWars

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")

def answer(data):
    datalist = []
    datalist = data.split()
    string = ''
    for i in datalist:
        print(i[len(i)::-1])
        string+=i[len(i)::-1]
    print(string)
    return string



print(game.answer(3,answer(game.data(3))))
game.logout
