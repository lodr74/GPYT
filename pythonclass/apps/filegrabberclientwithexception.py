from __future__ import print_function
import socket
import time

mysocket = socket.socket()
connected = False
while not connected:
    # for each port in a list of ports we want to try
        # delay for a second with time.sleep()
        try:
            mysocket.connect(("127.0.0.1",  # <current port variable in from loop> ))
        except socket.error:
            # then it didn't work so lets "continue" to the next item in the for loop
        else:
            # We must have connected so set the "connected" varaible to true
            #"break" out of the while loop

while True:
    print(mysocket.recv(2048).decode())

