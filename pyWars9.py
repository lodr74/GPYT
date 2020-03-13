import pyWars
import codecs


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    answer = data1[-1] + data1[1:-1:1] + data1[0]
    return answer

print(game.answer(9,answer1(game.data(9))))