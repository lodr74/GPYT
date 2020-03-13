import pyWars
import codecs


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    x = data1.split(',')
    print(x)
    answer = x[9]
    print(answer)
    return answer

print(game.answer(15,answer1(game.data(15))))