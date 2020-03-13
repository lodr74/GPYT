import pyWars
import codecs


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    print(data1)
    answers = []
    for i in data1:
        print(i)
        x,y = i.split(',')
        print("x is : %d and y is %d" % (int(x),int(y)))
        if int(y) % int(x) == 0:
            answers.append('True')
        else:
            answers.append('False')
    return answers

print(game.answer(25,answer1(game.data(25))))