'''

>>> mygame.question(45)
'Read the data element and return a list of images in the HTML (marked by IMG [one or more html img tags]
SRC or IMG DATA-SRC) in the order in which they appear in the source. '

'''

import pyWars
import re

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    #src=\'http://a.l.yimg.com/pv/static/img/metro_sprite-201109271557.png\
    final_list = []
    tags = re.findall(r"src=\\\'([\w\W]+?)\\\'|data-src=\"([\w\W]+?)\"|src=\"([\w\W]+?)\"",data1,re.IGNORECASE)
    for i in tags:
        for n in i:
            if n is '':
                pass
            else:
                #print(n)
                final_list.append(n)
    return final_list
        
print(game.answer(45,answer1(game.data(45))))
game.logout