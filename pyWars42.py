'''

>>> mygame.question(42)
'Extract the SSNs from the data.  A SSN is any series of 9 consecutive digits.
Optionally, it may be a series of 3 digits followed by a space or a dash then 2
digits then a space or a dash followed by 4 digits.  Submit a list of SSNs in the order they appear in the data.
All your SSNs should be in the format XXX-XX-XXXX'

>>> mygame.data(42)
'mlEbFQKPX681-93-0491zYKhIQWNBJPbAdn 067 39 5136PfvS- hchRm--opX-OmSOYz748390858AVrD KS -Y
OOmYkuDpAvhgy477-15-1277HHyv-lFpJGrrtnou-wXXVHA478630868onxBjInXnVRpACTgiaRk-i215 59 6489
s vjEG dvdABMrCrFL960-98-7896FWs-wqLW ufNIHaf-fVLzOB fmG-awN997561369BF QugtUaM WOXW144 86 1515nnm-LnHIbEa-OmOUWevpJPL-sWMSa338-53-8866oUE-j-AV
BGoxsocY RAvC-994 62 1193zacTDymiKD-rs-TlwjmTgBKV-K-981 26 4863P RpkAknXe'


'''

import pyWars
import re

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    print(data1)
    regex = re.findall(r"\d{9}|\d{3}-\d\d-\d{4}|\d{3}\s\d\d\s\d{4}",data1)
    ssn = []
    #print(regex)
    for w in regex:
        #ssn = [w.replace(' ', '-')
        if "-" in w:
            ssn.append(w)
        elif " " in w:
            ssn.append(w.replace(' ', '-'))
        else:
            ssn.append(w[:3] + "-" + w[3:5] + "-" + w[5:9])
    #print(ssn)
    return ssn
        
print(game.answer(42,answer1(game.data(42))))
game.logout