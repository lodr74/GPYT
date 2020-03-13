'''
>>> game.question(66)
'NAME:StegoBit - The data() is part of a file in which someone has hidden data by replacing one of the bits in each byte.
You need to figure out which of the 8 bits is being used to store encrypted data.  You will know which bit is being used
by counting the number of zeros and ones that occur in each bit.  Because they used cryptography, the bit that has an equal
number of zeros and ones is the evil bit.  Submit the answer in the form <evil bit>,<number of bits that are a 1>.  The
least significant bit is bit 1 and the most significant is bit 8. For example if the 2nd bit (00000010) contains the
encrypted data and there were 500 occurrences of the number 1 (and zero) then you would submit "2,500". '

>>> game.data(66)
'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00\xff\xfe\x00<CREATOR: gd-jpeg v1.0 (usi
>>> 


'''

import pyWars

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")

def answer1(data):
    print(data)
    occurances = len(data)//2
    print(occurances)
    echo = ' '.join(format(ord(x), '08b') for x in data)
    echo_list = echo.split(' ')
    i=0
    while i < 8:
        count = list(zip(*echo_list))[i].count("1")
        if count == occurances:
            output = str(8-i) + "," + str(occurances)
            return output
        i+=1
    #print(echo_list)


print(game.answer(66,answer1(game.data(66))))
game.logout