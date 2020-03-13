import pyWars
import codecs


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    print(data1)
    x = ''
    for i in data1:
        #print("i is: %s" % i)
        x += bytes.fromhex(i).decode('utf-8')
    return x

print(game.answer(22,answer1(game.data(22))))