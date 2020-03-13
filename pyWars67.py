'''
>>> game.question(67)
'NAME:BigBitNumber - Data contains some stegonagraphy.   There are 8 numbers embedded in the bits of each byte in the data.
The answer is calculated by adding together the 8 long integers (one long per bit) that are striped across the 8 bits of each
byte in the data string.   So if the first byte of data contained 10110001 then the MOST significant bit of the first number is
a one because bit zero of the first byte is a 1.  The most significant bit of the second number is a zero because the value of
bit 1 (the second bit) is a zero.  The second most significant bit of number 1 is determined by bit zero of the second byte and
so one.   So If data contains the 4 bytes 11111111, 00000000, 11110000,00001111 then my 8 numbers (in binary) will be
1010,1010,1010,1010,1001,1001,1001,1001.  Add together all 8 numbers and submit a single decimal number that is their sum. '

>>> game.data(67)
"GHB910141355JLKJABABRK0!!][';l,."


'''

import pyWars
import re

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")

def answer1(data):
    total = 0
    for eachbit in zip(*map("{0:08b}".format, map(ord,data))):
        total+=int("".join(eachbit),2)
    return total

print(game.answer(67,answer1(game.data(67))))
game.logout