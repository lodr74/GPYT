'''

'The data contains a Country Code.  Use GeoIPLite to find all of the Client IP addresses
that are in the dnslogs from that country.  The dnslogs are located in /home/student/Public/log/dnslogs/.
Submit a sorted unique list of IP addresses from that country found in the logs.  HINT: You only have three
seconds. Some modules are faster than others.'

'VG'

'''

import pyWars
import re
from os import listdir
from os.path import isfile, join
import GeoIP

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")

def answer1(data1):
    print(data1)
    positive_match = []
    dir_to_walk = '/home/student/Public/log/dnslogs/'
    gdb = GeoIP.open('/usr/share/GeoIP/GeoIP.dat', GeoIP.GEOIP_INDEX_CACHE | GeoIP.GEOIP_CHECK_CACHE)
    onlyfiles = [f for f in listdir(dir_to_walk) if isfile(join(dir_to_walk, f))]
    print(onlyfiles)
    for i in onlyfiles:
        #print(i)
        f2o = open("/home/student/Public/log/dnslogs/" + i).read()
        #print(f2o)
        #z = re.findall(r"client\s131.22.81.49#\d{5}:\squery:\s(\w+.\w+.\w+)",f2o)
        my_regex = r"client\s(\d+.\d+.\d+.\d+)#\d{5}:\squery:\s"
        #print(my_regex)
        z = re.findall(my_regex,f2o)
        print(len(z))
        if len(z) == 0:
            pass
        else:
            for i in z:
                print("i is: %s" % i)
                match = gdb.country_code_by_addr(i)
                if match == data1:
                    positive_match.append(i)
    return(sorted(positive_match))

print(game.answer(48,answer1(game.data(48))))
game.logout