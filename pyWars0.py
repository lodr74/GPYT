import pyWars
import codecs


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")

'''
>>> game.login("mleigh","N0Passw0rd")
'Login Successful'
>>> game.question(1)
'Submit the sum of .data()+ 5. '
>>> game.data(1)
86

'''


print(game.answer(0,game.data(0)))