import pyWars
import codecs


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    answer = 0
    for i in data1:
        answer += 1
    return answer

print(game.answer(14,answer1(game.data(14))))