import pyWars
import codecs


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    #print("Entering loop")
    answer = codecs.encode(data1,'rot-13')
    print("The Answers is: " + answer)
    return answer

print(game.answer(2,answer1(game.data(2))))