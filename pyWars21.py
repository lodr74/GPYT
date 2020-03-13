import pyWars
import codecs


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    i = 1
    num_list = []
    while i < 1000:
        x = i % data1
        if x == 0:
            num_list.append(i)
        i += 1
    return num_list

print(game.answer(21,answer1(game.data(21))))
game.logout
