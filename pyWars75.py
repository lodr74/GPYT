'''
>>> game.question(75)
"NAME:GREAT-HINT - The data element contains a copy of advapi32.dll.  This challenge requires that you use the pefile module
(which is not installed by default) to parse a copy of that dll and return the name of the third section of that dll.
Hint:Make sure there aren't any extra characters in your section name."


'''

import pyWars
import pefile
#import StringIO

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    #print(data1[0:128])
    sections = []
    pe = pefile.PE(data=data1)
    for section in pe.sections:
        sections.append(section.Name.decode('utf-8'))
        print(sections)
        print(section.Name.decode('utf-8'))
    return sections[2].strip('\x00')

print(game.answer(75,answer1(game.data(75))))
game.logout