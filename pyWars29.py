import pyWars
import codecs


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    a = []
    for i in data1.items():
        a.append(i)
    a.sort()
    return a

print(game.answer(29,answer1(game.data(29))))
game.logout