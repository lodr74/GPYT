import pyWars
import codecs


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    #print("Entering loop")
    #print(type(data1))
    answer =  data1 + data1[::-1] + data1
    print("The Answers is: " + answer)
    return answer

print(game.answer(7,answer1(game.data(7))))