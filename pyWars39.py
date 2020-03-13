'''

>>> mygame.question(39)

'You have determined that a stream encryption cypher is using repeating keys.
You XORed together two pieces of encrypted data which has the effect of eliminating the keys.
However the remaining data is still not clear text.  Instead it is the two pieces of original clear
text data XORed together.

IE  (Data1 XOR key1) XOR (Data2 XOR key1) = (Data1 XOR Data2).  The Data
element contains a list of two strings.  The first one is the encrypted data (Data1 XOR Data2).  The
second one is some known clear text from either Data1 or Data2.  XOR the first string (Encrypted data)
with the second string (clear text Data1 or Data2) to determine the other clear text data and submit
the unencrypted string. '

>>> mygame.data(39)

['\x16EW\x16\x07\x0b\x06\x03ZFI\x0f\x00\x1e\x01\x1c\x01#B\x12\x13\x1fD', 'A wafer-thin mintA wafe']

'''

import pyWars


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    print("The length of the first element: %d" % len(data1[0]))
    print("The length of the 2nd element: %d" % len(data1[1]))
    test = ""
    output = ""
    l = [ord(a) ^ ord(b) for a,b in zip(data1[0],data1[1])]
    for i in l:
        output += chr(i)
    return output
    

        
print(game.answer(39,answer1(game.data(39))))
game.logout