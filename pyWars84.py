'''
>>> game.question(84)
"NAME:Day-in-Month - Given the number of seconds since EPOCH. Calculate the day of the week and month in UTC and submit it in the form 'Day in Month'.  For example 'Thursday in April'"
>>> game.data(84)
432000.0
>>>
'''

import pyWars
import time

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    days =["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    result = time.gmtime(data1)
    result2 = time.ctime(data1)
    print("The common form is: %s" % result2)
    print("The results is: ")
    print(result)
    print("The Month # is: %s and the wday is: %s" % (result.tm_mon, result.tm_wday))
    output = days[result.tm_wday] + " in " + months[result.tm_mon-1]
    print(output)
    return(output)

        
print(game.answer(84,answer1(game.data(84))))
game.logout