import pyWars
import codecs


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    print(data1)
    a = 0
    data2 = data1.split()
    print(data2)
    for i in data2:
        a += int(i)
    return a

print(game.answer(19,answer1(game.data(19))))