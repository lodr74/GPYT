'''
'POINTS:3,TIMED:Y - The data contains the name of an image in your /home/student/Public/images/icanstalku-images/ folder.
Retrieve the DateTimeOriginal EXIF tag submit its value.'


'''

import pyWars
from PIL import Image

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def get_date_taken(path):
    return Image.open(path)._getexif()[36867]

def answer(data):
    path = '/home/student/Public/images/icanstalku-images/' + data
    print(path)
    value = get_date_taken(path)
    return value
    
print(game.answer(21,answer(game.data(21))))
game.logout
