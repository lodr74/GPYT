'''
>>> game.question(4)
'POINTS:3,TIMED:Y - The data() function returns the contents of a text file on a forensics examiners machine.
The file contains partial file paths that are part of a forensics investigation. All of the paths point to
files that were in the C:\\windows\\system32\\ directory or one of its subdirectories.  Some of them are fully
qualified paths that in the form DRIVE:\\path\\filename.   Others only contain parts of that path. Make them
complete absolute paths using the following rules.  1) If no drive letter is provided set it to C:\\. (capital C:)
2) Make sure the path reflects that all of these files are somewhere beneath the \\windows\\system32\\ folder.
Submit the answer in the same format and order that was given to you (new line separated strings).'
>>> game.data(4)
'C:\\windows\\system32\\suspect.doc
\n\\windows\\system32\\backdoor.exe
\nconfig\\file1.exe
\nC:\\windows\\system32\\image1.jpg
\nconfig\\console.dll
\n\\windows\\system32\\newfile.txt
\n\\windows\\system32\\drivers\\backdoor.exe
\n\\windows\\system32\\drivers\\newfile.txt
\n\\windows\\system32\\suspect.doc
\nboot\\malware.exe
\n\\windows\\system32\\image1.jpg
\nC:\\windows\\system32\\drives.txt
\n\\windows\\system32\\suspect.doc
\nAppCompat\\newfile.txt'
>>> 

'''

import pyWars

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")

def answer(data):
    print(data)
    datalist = []
    datalist = data.split("\n")
    string = ''
    for i in datalist:
        if "C:" in i:
            pass
        elif "\\windows\\system32" in i:
            i = "C:" + i
        else:
            i = "C:\\windows\\system32\\" + i
        string = string + i + "\n"
    print(string.strip())
    return string.strip()



print(game.answer(4,answer(game.data(4))))
game.logout
