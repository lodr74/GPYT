'''
>>> game.question(16)
'POINTS:4,TIMED:Y - Submit a comma separated list of the Top 25 Most commonly occurring words from the target URL in the order frequency.
The most commonly occurring word should be first in the list and the 25th most common word should be last.  You should IGNORE CASE and treat
everything as lower case.  Use split() to create a list of words and a counter dictionary to count the words. Submit your answer as a string
of comma separated lower case words. Example: "a,the,of,is,at,--,python,rocks" '

>>> game.data(16)
'http://10.10.10.30/textdoc.php?seed=850405'





'''

import pyWars
import requests
from collections import Counter

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")

    

def answer(data):
    url = data
    r = requests.get(url)
    wordlist = str(r.text).lower().split()
    countList = Counter(wordlist)
    output = ''
    for i in countList.most_common(25):
        output = output + str(i[0]) + ","
        print(output)
    return output[:-1]
    
    
        

        


print(game.answer(16,answer(game.data(16))))
game.logout
