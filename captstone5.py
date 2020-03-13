'''
>>> game.question(5)
'POINTS:3,TIMED:Y - The data element contains a comma separated string of items.
The first element is either the word LEFT or RIGHT.   If it is LEFT then you must
shift all of the other items to the LEFT and move the FIRST element to the end.
If it is RIGHT then you shift the other items to the RIGHT and move the LAST element to the beginning.
So LEFT,1,2,3 becomes 2,3,1.   RIGHT,1,2,3 becomes 3,1,2.   LEFT,5,6,7,8,9 becomes 6,7,8,9,5. '
>>> game.data(5)
'RIGHT,77,25,19,15'
>>>
'''

import pyWars

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")

def answer(data):
    print(data)
    datalist = []
    datalist = data.split(",")
    if datalist[0] == "RIGHT":
        length = len(datalist)
        i = 1
        string = ''
        while i < (length-1):
            if string is "":
                string+=datalist[i]
            else:
                string = string + "," + datalist[i]
            i+=1
        string = datalist[-1] + "," + string
    else:
        length = len(datalist)
        i = 2
        string = ''
        while i < length:
            if string is "":
                string+=datalist[i]
            else:
                string = string + "," + datalist[i]
            i+=1
        string = string +  "," + datalist[1]
 
    print(string)
    return string



print(game.answer(5,answer(game.data(5))))
game.logout
