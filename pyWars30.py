import pyWars
import codecs


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    x = data1.get("python")
    y = data1.get("rocks")
    print("The x value is: %s and the Y value is: %s" % (x,y))
    return int(x) + int(y)

print(game.answer(30,answer1(game.data(30))))
game.logout