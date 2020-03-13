import pyWars
import codecs


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    #E->3,A->4,T->7,S->5,G->6
    answer = data1.replace("E",str(3)).replace("A",str(4)).replace("T",str(7)).replace("S",str(5)).replace("G",str(6))
    #answer = data1[-1] + data1[1:-1:1] + data1[0]
    return answer

print(game.answer(11,answer1(game.data(11))))