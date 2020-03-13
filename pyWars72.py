'''
>>> game.question(72)
'NAME:XML-Parsing - You gained access to an XML document that contains user names and pass phrases for a web applications.
Retrieve the pass phrase for the first user name in XML document. '

>>> game.data(72)
'<?xml version="1.0" encoding="utf-8"?>\n<root>\n    <users>\n        <username passphrase=\'Its just a flesh wound\' />\n
<username passphrase=\'this parrot is dead\' />\n        <username passphrase=\'nudge nudge wink wink\' />\n    </users>\n</root>'
me-to-sans%22%2C+%22thats+no+ordinary+rabbit%22%5D%2C+%22error%22%3A+%22thou+count+to+three%2C+no+more%2C+no+less%22%7D'

'''

import pyWars
import xml.etree.ElementTree as ET


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    print("The api string is : \n %s" % data1)
    root = ET.fromstring(data1)
    for username in root.iter('username'):
        x = username.attrib
        password = x["passphrase"]
        # If I were to do this for real I would return all passphrases to a list and return the first element only.  I cheated. 
        return password
        
print(game.answer(72,answer1(game.data(72))))

game.logout