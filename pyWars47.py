'''

'The data() contains a client IP address.   Parse all of the DNS log files in /home/student/Public/log/dnslogs
and return a sorted list of all the hostnames that were queried by that client.  Do not eliminate duplicates.'



'''

import pyWars
import re
from os import listdir
from os.path import isfile, join

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")

def answer1(data1):
    print(data1)
    positive_match = []
    dir_to_walk = '/home/student/Public/log/dnslogs/'
    onlyfiles = [f for f in listdir(dir_to_walk) if isfile(join(dir_to_walk, f))]
    print(onlyfiles)
    for i in onlyfiles:
        #print(i)
        f2o = open("/home/student/Public/log/dnslogs/" + i).read()
        #print(f2o)
        #z = re.findall(r"client\s131.22.81.49#\d{5}:\squery:\s(\w+.\w+.\w+)",f2o)
        my_regex = r"client\s%s#\d{5}:\squery:\s(\w+.\w+.\w+)" % data1
        #print(my_regex)
        z = re.findall(my_regex,f2o)
        print(len(z))
        if len(z) == 0:
            pass
        else:
            for i in z:
                positive_match.append(i)
    print(len(positive_match))
    return(sorted(positive_match))

print(game.answer(47,answer1(game.data(47))))
game.logout