'''
'POINTS:2,TIMED:Y - The target url will only respond when the User-Agent string is set to "pywars-browser-1.0".
Write a python script to connect to the target url with that User-Agent then capture and submit the response as the answer. '

'''

import pyWars
import requests

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")

    

def answer(data):
    url = data
    headers = { 'User-Agent': 'pywars-browser-1.0'}
    response = requests.get(url, headers=headers)
    print(response.text)
    flag = str(response.text).split("=")
    return flag[1]
        

        


print(game.answer(19,answer(game.data(19))))
game.logout
