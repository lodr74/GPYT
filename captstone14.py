'''
>>> game.question(14)
'POINTS:3,TIMED:Y - Data will contain a tuple with two IP addresses.
The answer is a tuple that contains the longitude as floats associated with each IP according to GeoLiteCityLegacy.dat.'

>>> game.data(14)
('191.18.142.80', '137.70.236.160'




'''

import pyWars
import requests
import re
import GeoIP

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")

    

def answer(data):
    gdb = GeoIP.open('/home/student/Documents/pythonclass/apps/GeoLiteCityLegacy.dat', GeoIP.GEOIP_INDEX_CACHE | GeoIP.GEOIP_CHECK_CACHE)
    ips = data
    match = (gdb.record_by_addr(ips[0])['longitude'], gdb.record_by_addr(ips[1])['longitude'])
    return match

        


print(game.answer(14,answer(game.data(14))))
game.logout
