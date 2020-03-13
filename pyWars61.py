'''
"NAME:LetterPairs - Given a list of items, create a sorted list of all the possible pairs of those items.
For example, given ['d','a','c'] return ['a,c', 'd,a', 'd,c'].  Note that the results must be sorted alphabetically.
Also note that a,d and d,a are the same and there should be no duplicates in your answer.  In this case since d,a was
created first you eliminate the 2nd duplication (a,d).  After eliminating duplicates sort your list."

>>> game.data(61)
['t', 'p', 'g', 'm', 'l']



'''

import pyWars



game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")

def answer1(data1):
    print("Create all possible pairs of the following: %s" % data1)
    final_list = []
    for i in data1:
        for j in data1:
            if i == j:
                continue
            varX = i + "," + j
            varY = j + "," + i
            print("Testing : %s" % varX)
            if varY in final_list:
                continue
            if varX not in final_list:
                final_list.append(varX)
    print(sorted(final_list))
    return sorted(final_list)
    
    
   
print(game.answer(61,answer1(game.data(61))))
game.logout