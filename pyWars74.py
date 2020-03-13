'''
'NAME:Session-stumper - You are pen testing a web application.
When testing the web application, you once logged in and were
presented with another user ID (not the one you logged in with).
This is a clear case of a session number collisions.  Given example
values for the key, salt and session id determine the algorithm that
is used to calculate the session id.   The last element in the list will
contain a key and a salt.  You must calculate the associate session ID and
submit that ID.  (Hint: Things are not nearly as random as they appear.) '

>>> game.data(74)
[6285, 1577859153,  '9456798862E1577865438F1056790997'], [8724, 1577859153, '8898798862E1577867877F1000990997'],
[12543, 1577859153, '8072898862E1577871696F9184009973'], [14541, 1577859153, '6074898862E1577873694F7186009973'],
[10070, 1577859153, '4340798862A1577869223B5451909973'], [4091, 1577859153, '5534798862A1577863244B6645909973'],
[2124, 1577859153,  '8832798862E1577861277F9943909973'], [14772, 1577859153, '6404898862E1577873925F7516009973'],
[15030, 1577859153, '4925898862E1577874183F6037009973'], [6515, 1577859153, '9776798862A1577865668B1088790997'],
[10447, 1577859153, '']]


      key    salt        session
['],[6285, 1577859153, '9456798862E1577865438F1056790997

'''

import pyWars


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    salt,key,blank = data1[-1]
    middle = salt+key
    first = int(str(middle)[::-1])+1111111111
    last = first + 1111111111
    return "{0}E{1}F{2}".format(first, middle, last)

for i in range(20):        
    print(game.answer(74,answer1(game.data(74))))

game.logout