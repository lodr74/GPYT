'''
>>> game.question(62)
"NAME:Socket1 - Start the socket challenge server by running '/opt/socketchallenge' in your VM.  Next use the socket module to connect to port 19000 and submit the pin from .data().
Then follow the instructions given when you read the socket. (Hint:Testing this with netcat first might help you understand the challenge. Look at the pin and then run 'nc 127.0.0.1 19000') "

>>> game.data(62)
48664
>>>


'''

import pyWars
import socket


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def conPrime(port,pin):
    try:
        sock = socket.socket()
        print("Connecting to data stream on port %i...." % port, flush=True)
        sock.connect(("127.0.0.1", port))
        print("Recieving data...", flush=True)
        sock.recv(1000).decode
        print("Sending pin: %s" % pin, flush=True)  
        sock.send(pin.encode())
        print("Recieving data from 2nd data stream...", flush=True)
        output = sock.recv(100).decode()
        print("Printing the data received...\n")
        print(output)
        print("Sending the data received to the parent function...\n")
        return output
    except OSError as err:
        print("Fuck!!!")
        print("OS error: {0}".format(err))
        return "Error: No Ouput"

def answer1(port, data1):
    print("The first pin is: %s" % data1)
    output = conPrime(int(port),str(data1))
    if output == "Error: No Ouput":
        print("WTF!!!")
        return
    print("Output is : \n")
    print(output)
    if "Connect to " in output:
        output_list = output.split()
        print(output_list[2])
        print("The new port is %s and the new pin is: %s" % (output_list[2], output_list[-1]))
        answer1(int(output_list[2]), output_list[-1])
    else:
        print("Printing output...")
        print(output)
        output_return = output.split()
        print("Sending %s to return..." % output_return[3])
        print(game.answer(62,output_return[3]))

    
    
    
   
answer1(19000, game.data(62))
game.logout