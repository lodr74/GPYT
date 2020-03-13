'''

'The data() method returns an abosolute path to a directory on your file system.
Submit a sorted list of the filenames in that directory.'


>>> mygame.data(34)
'/home/student/Public/log/apache2'

'''

import pyWars
import codecs
import os

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    dir_listing = os.listdir(data1)
    print(dir_listing)
    test = sorted(dir_listing)
    print(test)
    #print(dir_listing)
    return test
            
print(game.answer(34,answer1(game.data(34))))
game.logout