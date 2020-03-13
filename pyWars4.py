import pyWars
import codecs


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    #print("Entering loop")
    #print(type(data1))
    answer = data1.upper()
    print("The Answers is: " + answer)
    return answer

print(game.answer(4,answer1(game.data(4))))