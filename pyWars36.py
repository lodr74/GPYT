'''
>>> game.question(36)
'The data() method will return a string. Find all the text files beneath /home/student/Public/log/ that contain that string.
The answer is a sorted list of all of the absolute paths to files that contain the string.  Do not uncompress gzip files.

>>> game.data(36)
'wind'


'''

import pyWars
import codecs
import os
import gzip

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    dir_to_walk = "/home/student/Public/log/"
    #print("Testing for data1: %s" % data1)
    positive_match = []
    for currentdir, listofdirs, listoffiles in os.walk(dir_to_walk):
        #print("The list of directories are", listofdirs)
        #print("[*] Testing in current Directory: ", currentdir)
        for Xfiles in listoffiles:
        #    if currentdir.endswith("/"):
        #        filepath = currentdir + Xfiles
        #    else:
        #        filepath = currentdir + "/" + Xfiles
        #    print("Now testing: %s" % filepath)
            filepath = os.path.join(currentdir,Xfiles)
            #print("Now testing: %s" % filepath)
            fcontent = open(filepath, "rb").read()
            if data1.encode() in fcontent:
                positive_match.append(filepath)
        
            #f = open(filepath,"rb").read()
            #if data1.encode() in f:
                #print(data1.encode())
            #    positive_match.append(filepath)
        #print(positive_match)
        z = sorted(positive_match)
        #print(z)
        #return z
        print(game.answer(36,z))
answer1(game.data(36))
#print(game.answer(36,))
game.logout