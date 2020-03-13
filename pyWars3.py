import pyWars
import codecs


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    #print("Entering loop")
    answer = codecs.decode(data1,'base64')
    print("The Answers is: " + str(answer))
    return answer

print(game.answer(3,answer1(game.data(3))))