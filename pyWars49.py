'''

>>> game.question(49)
'Find the nth most frequently occurring User-Agent String in the log file
/home/student/Public/log/apache2/access.log where n is the integer returned by the data method.'

>>> game.data(49)
5
>>> 

'''

import pyWars
import re
from collections import Counter

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")

def answer1(data1):
    print(data1)
    df = open("/home/student/Public/log/apache2/access.log").read()
    fc = Counter()
    fc.update(re.findall(r'[\d.]+.*?\[.*?\] ".*?" \d+ \d+ ".*?" "(.*?)"', df))
    print(fc.most_common(data1))
    print(fc.most_common(data1)[int(data1)-1])
    return fc.most_common(data1)[int(data1)-1][0]
    
    
print(game.answer(49,answer1(game.data(49))))
game.logout