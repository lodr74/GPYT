'''

>>> mygame.question(44)

'The Data element contains a string from a mysterious programming language.
In this language variable names begin with an uppercase letter and end with the same uppercase letter.
For example in this line: ZAxuZAuA   There are two variables ZAxuZ and AuA.  Notice that there is a capital
A inside the variable ZAxuZ but it is not the start of a new variable because it is part of another variable.
To make things more complex a variable name may contain the same uppercase letter than begins and ends the variable
name if it is escaped with a 0.  So the line ZAp0ZuZAuX0AZA contains the variables ZAp0ZuZ and AuX0AZA.  Use a regular
expression to parse the line of code and extract all the variable names.  Submit a comma separated string of variable names.'


>>> data element
BdbcCXWCzYYAV0BaB1xkzgwidhk2keeeDwXxba0DcAEYyyaDigbgyfzggy0zkibjFczZxEwywTAcUcTFgzbyavy02kwwvv30d0aiCYxyTZaaUdYxC2kwfi2x0zhaw2w
XCTFVcATTCTXhyvidycchbc10ea3ckUbwwYVBFzxawWdUycyg23k22gwf3wajVEFxYEEXzcyFBEXwXVzkhdajzxyhdci2bvcadfAaFvWbFYWbdcCYz0AvA0igzg1fvvh
jkh0xjCWExAzZUdWyyvVACjcfk3a2x30fUDFAVFwXWTACDXwBCxATUbdvezv00c33XBzAFFWyEdyEXiybvbc01wdvvg3yxkv

'''

import pyWars
import re

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    bString = data1
    term = len(bString)
    stringer_bell = ''
    print("Starting the program \n")
    print(data1 + "\n")
    final_list = ''
    start = 0
    count = 0
    dstart = 0
    dstop = 0
    for i in data1:
        print("Testing letter: %s" % i)
        print("The count is %i and the start_POS is %i" % (count,dstart))
        
        if (i in stringer_bell) and (count < dstart):
            print("Testing : %s - Letter in existing variable" % i)
            count = count + 1
            continue
        
        if count < dstart:
            print("Testing: %i - Count is less than the start_pos: %i" % (count, dstart))
            count = count +1
            continue
        
        if i.isupper() == False:
            print("Testing : %s - Letter is lower case" % i)
            count = count + 1
            continue
        else:
            print("Testing : %s - Letter is capitalized and should start the variable" % i)
            letter = i
            regex_match = r"(%s\w+?[^0]%s)" % (letter, letter)
            y = re.search(regex_match ,bString)
            start = y.regs[0][0]
            stop = y.regs[0][1]
            stringer_bell = bString[start:stop]
            data1search = re.search(stringer_bell,data1)
            dstart = data1search.regs[0][1]
            print("The new data search positions start at %i" % (dstart))
            print(data1 + "\n")
            print(stringer_bell + "\n") 
            if final_list is '':
                print("Final_List is empty: %s \n" % final_list)
                final_list = stringer_bell
            else:
                final_list = final_list + "," + stringer_bell
            start = stop
            bString = bString[start:]
            count = count + 1
    return final_list

        
print(game.answer(44,answer1(game.data(44))))
game.logout