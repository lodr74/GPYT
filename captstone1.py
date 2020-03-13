import pyWars
import base64

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")

def answer(data):
    print(data)
    sel, num, string = data.split(',')
    print("Data lenght is: %i " % len(string))
    print("Character is: %s " % sel)
    print("Num is: %s " % num)
    print("String Count is: %i" % string.count(sel))
    S=0
    for pos,i in enumerate(string):
        if i == sel and S == int(num):
            print("Position is: %i" % (pos-1))
            return pos-1
        elif i == sel and S != int(num):
            S+=1
            pass
        else:
            pass


print(game.answer(1,answer(game.data(1))))
game.logout
