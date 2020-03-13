'''

>>> game.question(38)
'During incident response to some ransomware you learn that the malware is using a simple XOR encryption to encrypt
a passphrases.  You have determined that they are XORing every character in the passphrase with a 0x61.  Create a
function that decrypts the passwords.  Call your xor function to decrypt the password in the data element then submit
the unencrypted passphrase.'
>>> game.data(38)

'3\x0e\x02\nL/L3\x0e\r\rA\x13\x14\x0fA\x00\x16\x00\x18@A\x13\x14\x0fA\x00\x16\x00\x18@'

'''

import pyWars
import codecs
import os
import gzip

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")

def answer1(data1):
    test = ""
    #print(":".join("{:02x}".format(ord(c)) for c in data1))
    for c in data1:
        #print(ord(c))
        test +=  chr(int(ord(c)) ^ 0x61)
    return test
        
print(game.answer(38,answer1(game.data(38))))
game.logout