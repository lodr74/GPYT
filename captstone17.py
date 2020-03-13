'''
"POINTS:4,TIMED:Y - Download the ssh key for the student2 account from http://10.10.10.30/student2_sshkey using the browser of your choice.
You will have to run 'chmod 400 student2_sshkey' to use the key.  Then use that key to execute the command in the data element.  The command
to execute including the user name, target server and a command on the target are in the data element.  Capture the response you get when
executing the command line in the data element and submit it as the answer. "

>>> game.data(17)
'Command = ssh student2@10.10.10.30 -i <SSH Keyfile you just downloaded> ./genflag seed=164939'


'''

import pyWars
import os
import subprocess
import sys

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")

    

def answer(data):
    command = data
    print(command)
    key = '/home/student/Downloads/student2_sshkey'
    command = str(command.replace('<SSH Keyfile you just downloaded>', key)).split(" = ")
    command = command[1]
    commands = command.split(" ")
    ident = "-i " + key
    print(ident)
    ssh = commands[0]
    print(ssh)
    user = commands[1]
    print(user)
    seed = commands[4] + " " + commands[5]
    print(seed)
    print(commands)
    ssh = subprocess.Popen(["ssh", "-i", "/home/student/Downloads/student2_sshkey", "student2@10.10.10.30", seed],
                        stdin =subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        universal_newlines=True,
                        bufsize=0)
    # Send ssh commands to stdin
    #ssh.stdin.write(seed)
    ssh.stdin.close()

    # Fetch output
    for line in ssh.stdout:
        print(line.strip())
        return line.strip()
    
        

        


print(game.answer(17,answer(game.data(17))))
game.logout
