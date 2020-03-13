import pyWars
import codecs


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    print(data1)
    full_list = data1[0] + data1[1]
    print(full_list)
    res = []
    for i in full_list:
        if i not in res:
            res.append(i)
    res.sort()
    print(res)
    return res

print(game.answer(23,answer1(game.data(23))))