import pyWars
import codecs


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    print("Data1 is : %s" % data1)
    half = int(len(data1) /2)
    print("The value of half is: %d" % half)
    print(type(half))
    answer = data1[:half][::-1] + data1[half:]
    return answer

print(game.answer(10,answer1(game.data(10))))