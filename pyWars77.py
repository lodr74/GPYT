'''
>>> game.question(77)
"NAME:FAST-Hash - You are given the hash to a file in .data().  It may be a piece of malware, a known illegal image,
or other forensics artifact.  You don't know the name of the file.  Search the hard drive to find the file that has
that hash. (Search the file structure in your Class VM). Note: It is possible that you will find hash collisions and 
multiple file names may have to be submitted one at a time until the right file is found.   Retrieve the hash from the
data element.  Submit the full path of the file that has that hash as your answer.  "

>>> game.data(77)
'eb5a24ad827bae80b198ef7bb63ff40a'

'''

import pyWars
import os
import hashlib

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def indexfiles(path, file_dict):
   for root, dirs, files in os.walk(path):
        #print(root)
        for filename in files:
            targetFile = os.path.join(root,filename)
            try:
                content = open(targetFile,"rb").read()
                hashed_file = hashlib.md5(content)
                file_dict[hashed_file.hexdigest()] = targetFile
            except:
                print("OS Error")
    


def answer():
    file_dict = {}
    index_list = []
    indexfiles("/usr/sbin",file_dict)
    indexfiles("/usr/bin",file_dict)
    indexfiles("/home",file_dict)
    #print(game.answer(77,answer1(game.data(77))))
    hashLookup = game.data(77)
    #print(hashLookup)
    #print(file_dict)
    for i in range(100):
        print("looking up match")
        match = file_dict.get(hashLookup)
        print("evaluating match")
        if match:
            print("match")
            return match


def main():
    data = answer()
    print(game.answer(77,data))
    game.logout    

if __name__ == "__main__":
    main()