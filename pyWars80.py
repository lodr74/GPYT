'''
>>> game.question(80)
'NAME:Botnet-Decode - The data() contains a tupel with two parts.  Part 1 is an encoded command and control message to a bot.  Part 2 is the key.
The clear text message is the exact same length as the key.  Extract and submit the clear text message.'

>>> game.data(80)
('vApiaut9xwzcjT qQ 0lWVJ8mZYRNIfgbLofWCgsoU9K6PDbUF2AsrnBsg4Gbwjsz3TxQvcqmJualVRZYI6ObBpiCH5yt88GfNd6fPd32ens3EGnsk630fHbrHfGrrWNS4kC4rPXrkS86dkSDg
7fgU2EFKW3M2MgHOrGUSg7EPg3GdB0OE0yFo5FLMgFM3rrkdMW67836y', 'vApiaut9xwczjT Qq lmVZJYRI')


>>> game.data(80)
('pgWn5Gr2a 98 KcL 0N 4exdBmtXFIkXODPZkzOSHk3v23ODPTJoDglZUSAZHRa8kLQ9KN0pcmBtG5xdIFAobikJWn4loQrVPhEVhSS4vTV6qyfChTjbMskkhlRSbhjqRDiuDCfCHfDiZkiyjw6VO4P
Z774JM77ybE3ksbMSzA7juzwqXPXTUf4JVXjTfjTZv4yJTJoOjOTC', 'pgWn5Gr2a 89 KcL N0 mxtBdIF')
>>> game.data(80)
('fARqb5emvpQs i9 CUtFdukS7L3lw8JJcEPygDKoKJmuxWo6HJPArPDaUUrVyUMQvspt9fiSd75bk8LlD3wnHuRqUTDxerPMBrMEI4B0j2ygVKunGZWhh2hPZJYh4Bx2MTBnuCNNoDZHEX6Jo6hZJc
HTUnzTFOJXBMEnoUrTX0nXDgFyzz0ZKgcBEjCUc6ghKU2r6n0IyE', 'fARqb5emvpQs ti9S7kdLl38w')
>>> game.data(80)
('TLUczvAi2Raqb3NX Yu FS eYyHBZ7JlYpWDEKVZ9OKiwICQmQotL7f6dCpWOYRqjNK2baTuX3FvzSyeHBfkoJpUcGt6OAPxsp5MpP00EwprK6gfZJMdnEk4dQp0GMfCPVdV5jggrMrDjxIjWwnEZOf
7ZCoPIgWIZsCmxP0jmJVZxKpY9Qg4GVo5jQCEZ44699jWwDQdj9G', 'TLUczvAi2Raqb3NXF SyHeuB')
>>> game.data(80)
('WaXMet3QRKOUsvk cBHDSb68irf0VomHLPBNyJmquQ5nJLBB4JalISjNlJYRUAnAHOsKWvkDcteb068oiPYFSXMJEBm3Fx5EgTywY9yNhC2Vjuw4zIAVw4SHl5jhg2GgrlIgfyw5lLwYhC2FqCCLyd
Nr4SVyBFqjjfSn2rgrZq9fuEFgHpFE4B29Znl5yfdNdlgApnJC4', 'W
aXMet3QRKUOsvk Dcb608ioP')
>>> game.data(80)
('PhZstJoeqgRI 7V8BXLKF7Y5Ccb6La4EpHrLnaf9de3pH92pTyhMWM3zWd3dERgqIVBKPF8XvJt5Ccb6y4S0MZsMfSkoW32QEQT7Szym9YuYl3dum9EGm2OrMSnddAU4GnQ3nEOuQmw0Ai334rrErMU
dOM9DxOv7dGLMMmxrz3dpxmiQ9lv0nY9Ljikavynx0N3Glimzr', 'PhZstJoeqgRI VB8KF5CcXb6')
>>> 

'''

import pyWars
import base64

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    data,key = data1
    print(key)
    print(data)
    output = ''
    for i in key:
        output+=chr(data.replace(i," ",1).index(i)-data.index(i))
        print(output)
    return output

        
print(game.answer(80,answer1(game.data(80))))
game.logout