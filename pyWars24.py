import pyWars
import codecs


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    print(data1)
    data1.sort()
    print(data1)
    return data1

print(game.answer(24,answer1(game.data(24))))