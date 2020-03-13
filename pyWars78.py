'''
>>> game.question(78)
"NAME:Odd-Binary - Binary numbers are base2.  You can represent any numbers with just two numbers, a zero and a one.
For example binary 0010 is a decimal 2.  Python easily converts between binary and decimal.  The bin() function converts
decimal numbers to binary.  For example bin(10) will produce 0b1010.  That is a 1 in the 3rd position and a 1 in the 1st position.
So it 2**3 plus 2**1 or 8+2 which is 10.  Now imagine that instead of zero and one we used other characters.
If instead of the characters '0' and '1' we used the characters '$' and 'o' respectively.   The decimal 10 would be 'o$o$'.
The data element will contain a string with two parts separated by a comma.   The first part has two characters that represent
the base 2 values.  Convert the number to decimal and submit the number.   For example, if data is '!*,*!!*!' the answer is 18."

>>> game.data(78)
'xf,ffxfffxfffxxfxff'

'''

import pyWars
import os

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")

def binaryToDecimal(n): 
    return int(n,2) 

def answer1(data1):
    string_list = data1.split(",")
    print(string_list)
    bin_rep = []
    for i in string_list[0]:
        bin_rep.append(i)
    binnum = string_list[1].replace(bin_rep[0],str(0)).replace(bin_rep[1],str(1))
    print(binaryToDecimal(binnum))
    return binaryToDecimal(binnum)
        
print(game.answer(78,answer1(game.data(78))))
game.logout