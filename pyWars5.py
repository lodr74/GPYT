import pyWars
import codecs


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    #print("Entering loop")
    #print(type(data1))
    answer =  data1.find("SANS")
    print("The Answers is: " + str(answer))
    return answer

print(game.answer(5,answer1(game.data(5))))