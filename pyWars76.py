'''
>>> game.question(76)
'NAME:Malware-Loader - The data element contains a copy of advapi32.dll.  This challenge requires that you use the pefile
module to analyze the dynamic link library and find the function that it imports named RpcBindingSetAuthInfoA.  What is the
preferred load address of this API in memory?  Submit your answer as a hex address with a leading 0x followed by hex characters.
Ex 0xffdd10ae   '

'''

import pyWars
import pefile


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):
    pe = pefile.PE(data=data1)
    print("[*] Listing imported DLLs...")
    for entry in pe.DIRECTORY_ENTRY_IMPORT:
        print('\t' + entry.dll.decode('utf-8'))
        dll_name = entry.dll.decode('utf-8')
        print("[*] %s imports:" % dll_name)
        for func in entry.imports:
            if func.name.decode('utf-8') == 'RpcBindingSetAuthInfoA':
                print("\t%s at 0x%08x" % (func.name.decode('utf-8'), func.address))
                funky = str("0x%08x" % func.address)
                print(funky)
                return funky
                

        
print(game.answer(76,answer1(game.data(76))))
game.logout