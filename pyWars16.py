import pyWars
import codecs


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    x = data1.split(':')
    print(x)
    y = x[1].split('$')
    print(y)
    answer = y[2]
    print(answer)
    return answer

print(game.answer(16,answer1(game.data(16))))