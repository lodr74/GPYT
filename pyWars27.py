import pyWars
import codecs


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    print(data1)
    answers = []
    for i in data1:
        print(i)
        answers.append(i)
    answers.sort()
    return answers

print(game.answer(27,answer1(game.data(27))))