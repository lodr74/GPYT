from __future__ import print_function
import requests

def lookup_ssid(macaddress):
    postdata = {'inputMAC':macaddress}
    return browser.post('http://127.0.0.1:5730/data', postdata).content

ssids = ['12:34:56:78:90','00:00:0c:9f:f0:01', 'aa:bb:cc:dd:ee:ff', '00:00:5e:00:01:1b', '00:00:5e:00:01:02', '00:00:5e:00:01:32', '68:1c:a2:06:68:ee', '14:d6:4d:25:57:86', '00:00:00:00:00:00', '00:00:5e:00:52:13', '00:00:00:dd:dd:dd', '00:00:0c:9f:f0:c9', '00:1b:17:00:01:15', '00:11:74:48:8f:30', '00:00:0c:9f:f0:cb']

browser = requests.session()
postdata = {'inputName':'apiusername','inputPassword':'apipassword'}
response = browser.post('http://127.0.0.1:5730/login', postdata)
if response.status_code == 200:
    print("You have been logged in")
    for eachmac in ssids:
        print("Looking up {0}".format(eachmac))
        print("-----", lookup_ssid(eachmac))

