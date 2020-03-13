import pyWars
import codecs


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    x = "Pywars rocks"
    data1.append(x)
    print(data1)
    return data1

print(game.answer(17,answer1(game.data(17))))