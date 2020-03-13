'''

>>> game.question(70)
'NAME:ADPolicy - The data element contains a list of possible passwords that you have harvested from the target organizations website.
You know that their active directory policy will only allow password that have at least 1 upper, 1 lower, 1 number .   The passwords must
have 7 or more characters in it.  They also prohibit the use of any special characters in their passwords.   Return a list of password that
match their password complexity requirements.  Do not change the order of the passwords.   '
>>> game.data(70)
['camaro', 'bronco', 'boomer', 'fender', 'Hahahas', 'carter', 'cookie', 'gemini', 'firebird', 'horney', 'driver', 'debbie', 'cameron',
'heather', 'butter', 'hockey', 'flyers1', 'booboo', 'carlos', 'george', 'danielle', 'ferrari', 'butthead', 'erotic', 'Trinities2', 'Captain',
'calvin', 'Daniel2!', 'Col1ege', 'chelsea', 'cowboys', 'hooters', 'gregory', 'Poops', 'hotdog', 'Princesas4', 'broncos', 'blonde', 'dallas',
'Blahblahs', 'casper', 'charlie', 'donald', 'compaq', 'dragon', 'golden', 'Go1fer', 'bulldog', 'blazer', 'ginger', 'florida', 'giants', 'guitar',
'fishing', 'crystal', 'coffee', 'edward', 'canada', 'dennis', 'eagle1', 'Forums', 'boston', 'Pokemons', 'diablo', 'Spirits', 'flower', 'cheese',
'brandon', 'gandalf', 'cowboy', 'computer', 'braves', 'Rotimis', 'Cooper', 'Gordon', 'Qazwsxes4', 'doggie', 'gateway', 'booger', 'freddy', 'dakota',
'forever', 'bond007', 'brazil', 'einstein', 'corvette', 'Ga7or', 'blondes', 'dolphin', 'freedom', 'bonnie', 'gunner', 'Googles', 'diamond', 'dreams',
'eagles', 'chester', 'charles', 'doctor', 'falcon', 'cocacola', 'hannah', 'brandy', 'helpme', 'harley', 'extreme', 'hardcore', 'Christs12', 'dolphins',
'chicken', 'football', 'chicago', 'buster', 'hammer']
>>>


'''

import pyWars
import re

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def answer1(data1):
    pass_list = []
    for i in data1:
        if (any(x.isupper() for x in i) and any(x.islower() for x in i) and any(x.isdigit() for x in i) and len(i) >= 7):
             if re.match("^[a-zA-Z0-9]*$", i):
                pass_list.append(i)
             else:
                pass
            
    return pass_list

print(game.answer(70,answer1(game.data(70))))
game.logout