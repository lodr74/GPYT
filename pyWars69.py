'''
>>> game.question(69)
'NAME:PasswordList - You found an attacker\'s passowrd guessing dictionary on your internal system.
You have been asked how many password attempts it would have required before the attacker guessed your
weak administrator password.  The .data() returns a tuple that contains the weak admin password and
the list of passwords in the attackers dictionary. Find the location of the cracked password in the
list of possible passwords.  For example  data= ( "C", ["A","B","C","D","E"]) the answer is 2.    '

>>> game.data(69)
('Cooper', ['camaro', 'bronco', 'boomer', 'fender', 'Hahahas', 'carter', 'cookie', 'gemini', 'firebird', 'horney',
'driver', 'debbie', 'cameron', 'heather', 'butter', 'hockey', 'flyers1', 'booboo', 'carlos', 'george', 'danielle',
'ferrari', 'butthead', 'erotic', 'Trinities2', 'Captain', 'calvin', 'Daniel2!', 'Col1ege', 'chelsea', 'cowboys',
'hooters', 'gregory', 'Poops', 'hotdog', 'Princesas4', 'broncos', 'blonde', 'dallas', 'Blahblahs', 'casper', 'charlie',
'donald', 'compaq', 'dragon', 'golden', 'Go1fer', 'bulldog', 'blazer', 'ginger', 'florida', 'giants', 'guitar',
'fishing', 'crystal', 'coffee', 'edward', 'canada', 'dennis', 'eagle1', 'Forums', 'boston', 'Pokemons', 'diablo',
'Spirits', 'flower', 'cheese', 'brandon', 'gandalf', 'cowboy', 'computer', 'braves', 'Rotimis', 'Cooper', 'Gordon',
'Qazwsxes4', 'doggie', 'gateway', 'booger', 'freddy', 'dakota', 'forever', 'bond007', 'brazil', 'einstein', 'corvette',
'Ga7or', 'blondes', 'dolphin', 'freedom', 'bonnie', 'gunner', 'Googles', 'diamond', 'dreams', 'eagles', 'chester', 'charles',
'doctor', 'falcon', 'cocacola', 'hannah', 'brandy', 'helpme', 'harley', 'extreme', 'hardcore', 'Christs12', 'dolphins',
'chicken', 'football', 'chicago', 'buster', 'hammer'])


'''

import pyWars

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")

def answer1(data1):
    index = data1[1].index(data1[0])
    
    print(index)
    return index

print(game.answer(69,answer1(game.data(69))))
game.logout