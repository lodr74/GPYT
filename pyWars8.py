import pyWars
import codecs


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    #print("Entering loop")
    print(data1)
    answer =  data1[1] + data1[4] + data1[8]
    print("The Answers is: " + answer)
    return answer

print(game.answer(8,answer1(game.data(8))))