import pyWars
import codecs


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    print(data1)
    answers = []
    for i in data1:
        answers.append(type(i))
    return answers

print(game.answer(26,answer1(game.data(26))))