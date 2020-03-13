'''
'Name:IOS-Encoding - The data element contains part of a Cisco IOS config. Cisco uses a custom Base64 encoder/decoder to encode a SHA256 hash.
Research how Cisco does this and reverse it. Submit the all uppercase hex SHA256 hash of the password. '

'router# show running | include ^username.*secret 4\nusername admin secret 4 gfHrwk.7OVzLyvb.BvgnFA9ZCvwYesxKARcjmtTN7yE'


Need to add a translate table for cisco custom character set versus normal character set

'''

import pyWars
import codecs

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data):
    print(data)
    cisco = "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    translation = str.maketrans(cisco,normal)
    data = data.split()[-1]
    print(type(data))
    return codecs.encode( codecs.decode( data.translate(translation).encode()+b"=", "BASE64"), "HEX").upper().decode()
         
print(game.answer(82,answer1(game.data(82))))
game.logout