'''

'The data() contains filename of a BIND DNS log and a host name.  Open the file specified from the
/home/student/Public/log/dnslogs directory.   The answer is a sorted list of all the client IP addresses
in the specified log file that queried that host.'

>>> mygame.data(46)

('13.log', 'www.yahoo.com')


'''

import pyWars
import re

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    print(data1)
    final_list = []
    f2o = open("/home/student/Public/log/dnslogs/" + data1[0]).read()
    #print(f2o)
    #for i in f2o:
        #print(i)
    #    if data1[1] in i:
            #print(i)
    return sorted(re.findall(r"client\s(\d+.\d+.\d+.\d+)\#\d{5}:\squery:\s"+data1[1],f2o))
    #final_list.append(re.findall(r"client\s(\d+.\d+.\d+.\d+)\#\d{5}:\squery:\s",data1[1]))
    #print(final_list)
    #        final_list.append(re.findall(r"client\s(\d+.\d+.\d+.\d+\#):\squery:\s",i))
    #print(type(final_list)) 
    #srt_list = sorted(final_list)
    #print(srt_list)
    #print(data1)
    #return srt_list
    #print(game.answer(46,srt_list))

        
print(game.answer(46,answer1(game.data(46))))
game.logout