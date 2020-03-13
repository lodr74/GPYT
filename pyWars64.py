'''


'NAME:Rerange - Data contains a large string.  If, in the string, you see two integers separated by dashes (5-7)
replace that with the individual numbers in that range (ie 5,6,7).   Resubmit the answer with all of the number ranges expanded.
Example "string",9,7,4-6,"apple"  becomes "string",9,7,4,5,6,"apple". Submit a single string containing all the expanded entries.  '

>>> game.data(64)
'GIAC,6-19,0-17,0-18,8-19,2,2-18,9-16,SANS,1-19,2,0-18,0-16,Python,GIAC,0-15,GIAC,7-17,2-15,Python,5,GIAC,0-18,5-15,2-18'

1) split based on ","
2) iterated through list
3) if new var has a "-"
    a) split
    b) determine #'s in between
    c) reassemble and concatenate string

'''

import pyWars

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")

def answer1(data1):
    print("The first pin is: %s" % data1)
    output_list = data1.split(",")
    output = ''
    print(output_list)
    for i in output_list:
        if "-" in i:
            x = i.split("-")
            print(x)
            iterator = int(x[0])
            while iterator < (int(x[1])+1):
                #print("Starting while loop with: %i" % iterator)
                if output is '':
                    output+=str(iterator)
                else:
                    itstr = "," + str(iterator)
                    output+=itstr
                #print("New output is: %s" % output)
                iterator+=1
        else:
            if output is '':
                output+=i
            else:
                newstr = "," + i
                output+=newstr
            #print("New output is: %s" % output)
    
    print(output)
    return output

print(game.answer(64,answer1(game.data(64))))
game.logout