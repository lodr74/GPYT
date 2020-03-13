import pyWars
import codecs


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    print(data1)
    a = 0
    for i in data1:
        a += int(i)
    return a

print(game.answer(18,answer1(game.data(18))))