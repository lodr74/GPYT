import pyWars
import codecs


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    print(data1)
    answers = []
    for i in data1:
        print(i)
        key = data1[i]
        answers.append(key)
    answers.sort()
    return answers

print(game.answer(28,answer1(game.data(28))))