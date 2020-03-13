import pyWars
import codecs


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    print(data1)
    data2 = ["this","python","stuff","really","is","fun"]
    print(data2)
    a = ''
    for i in data2:
        if a is '':
            a = i
        else:
            a = a + data1 + i 
    print(a)
    return a

print(game.answer(20,answer1(game.data(20))))