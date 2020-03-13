import pyWars
import codecs


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    i = 1
    answer = []
    while i != data1:
        answer.append(i)
        i += 1
    return answer

print(game.answer(13,answer1(game.data(13))))