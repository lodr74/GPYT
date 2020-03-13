import pyWars
import codecs


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    print(data1)
    #E->3,A->4,T->7,S->5,G->6
    answer = data1[2]
    #answer = data1[-1] + data1[1:-1:1] + data1[0]
    return answer

print(game.answer(12,answer1(game.data(12))))