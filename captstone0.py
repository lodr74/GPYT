import pyWars
import base64

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")

def answer(data):
    print(data)
    string = base64.b64decode(data)
    return string[::-1]


print(game.answer(0,answer(game.data(0))))
game.logout
