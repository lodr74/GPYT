import pyWars
from codecs import encode
from codecs import decode
import os
import gzip
from os.path import join,getsize
import re
import itertools
import GeoIP
from collections import Counter
from scapy.all import *

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer0():
    return game.answer(0,game.data(0))

def answer1():
    return game.answer(1,game.data(1)+5)

def answer2():
    '''
    >>> game.question(2)
    'ROT-13 encode the .data() string. For example ABCDEFG becomes NOPQRST '
    '''
    return game.answer(2, encode(game.data(2), 'rot13'))

def answer3():
    '''
    >>> game.question(3)
    'Decode the BASE64 encoded .data() string. '        
    '''
    return game.answer(3, decode(game.data(3), 'base64'))

def answer4():
    '''
    >>> game.question(3)
    'Decode the BASE64 encoded .data() string. '        
    '''
    return game.answer(4, game.data(4).upper())

def answer5():
    '''
    >>> game.question(5)
    "The answer is the position of the first letter of the word 'SANS' in the data() string. "      
    '''
    return game.answer(5, game.data(5).index("SANS"))

def answer6():
    '''
    'Read the .data() string and write it backwards. '     
    '''
    return game.answer(6, game.data(6)[::-1])

def answer7(out):
    '''
    'Submit data() forward+backwards+forward. For example SAM -> SAMMASSAM '
 
    '''
    return game.answer(7, out+out[::-1]+out)

def answer8(out):
    '''
    'Return the 2nd, 5th and 9th character.  For example 0123456789->148 '
    '''
    return game.answer(8, out[1]+out[4]+out[8])

def answer9(out):
    '''
    'Swap the first and last character. For example frog->grof, Hello World->dello Worlh etc. '
    '''
    return game.answer(9, out[-1]+out[1:-1]+out[0])

def answer10(out):
    '''
    'Reverse the first half of the data(). For example sandwich->dnaswich '
    '''
    return game.answer(10, out[0:int(len(out)/2)][::-1]+out[int(len(out)/2):])

def answer11(out):
    '''
    'Leet speak it (E->3,A->4,T->7,S->5,G->6) convert only uppercase letters. For example LeEtSpEAk->Le3t5p34k '
    '''
    return game.answer(11, out.replace("E","3").replace("A","4").replace("T","7").replace("S","5").replace("G","6"))

def answer12(out):
    '''
    'Read the list from data and return the 3rd element '
    '''
    return game.answer(12, out[2])

def answer13(out):
    '''
    'Build a list of numbers starting at 1 and up to but not including the number in data(). ' 
    '''
    return game.answer(13, list(range(1,out)))

def answer14(out):
    '''
    'Build a list of numbers starting at 1 and up to but not including the number in data(). ' 
    '''
    return game.answer(14, len(out))

def answer15(out):
    '''
    'Split the data element based on the comma (",") delimiter and return the 10th element '
    '''
    return game.answer(15, out.split(',')[9])


def answer16(out):
    '''
    'The data element contains a line from an /etc/shadow file. The shadow file is a colon delimited file.
     The 2nd field in the colon delimited field contains the password information.   The password information
     is a dollar sign delimited field with three parts.  The first part indicates what cypher is used.  The
     second part is the password salt.  The last part is the password hash.   Retrieve the password salt for
     the root user.'
    '''
    return game.answer(16, out.split(':')[1].split('$')[2])

def answer17(out):
    '''
    'Add the string "Pywars rocks" to the end of the list in the data element.  Submit the new list. '
    '''
    out.append("Pywars rocks")
    return game.answer(17, out)

def answer18(out):
    '''
    'Add up all the numbers in the list and submit the total. '
    '''
    return game.answer(18, (lambda x: sum(x))(out))

def answer19(out):
    '''
    'Given a string that contains numbers separated by spaces, add up the numbers and submit the sum.  "1 1 1" -> 3 '
    '''
    return game.answer(19, sum([int(x) for x in out.split()]))

def answer20(out):
    '''
    'Create a string by joining together the words "this","python","stuff","really","is","fun" by the character in .data().
    For example if data contains a hyphen (ie "-") then you submit "this-python-stuff-really-is-fun".  '
    '''
    return game.answer(20,  "this"+out+"python"+out+"stuff"+out+"really"+out+"is"+out+"fun")

def answer21(out):
    '''
    'The answer is the list of numbers between 1 and 1000 that are evenly divisible by the number provided.  2->[2,4,6,8..] 4->[4,8,12,16..] '
    '''
    return game.answer(21,[x for x in range(1,1001) if x%out==0])

def answer22(out):
    '''
    'Given a list of hexadecimal digits return a string that is made from their ASCII characters.  Ex [41 4f] -> "AO" '
    '''
    return game.answer(22,"".join([bytearray.fromhex(x).decode() for x in out]))

def answer23(out):
    '''
    'You will be given a list that contains two lists.  Combine the two lists and eliminate duplicates.  The answer is the SORTED combined list. 
    '''
    
    return game.answer(23,sorted(set(out[1]).union(set(out[0]))))

def answer24(out):
    '''
    'Sort the elements in the list in numerical order.  Submit the sorted list. ' 
    '''
    return game.answer(24,sorted(out))

def answer25(out):
    '''
    'Data contains a list of comma separated numbers.   If the second number is evenly divisible by the first return TRUE in a list at the same index.
    If it is not evenly divisible return false.  For example [ "6,36" , "2,8" , "3,11" ] you would answer [ "True" , "True", "False" ] because  36 is
    evenly divisible by 6, 8 is evenly divisible by 2 and 11 is NOT evenly divisible by 3.  Note the responses are case sensitive strings of either
    "True" or "False". '
    '''
    return game.answer(25,["True" if int(x[1])%int(x[0])==0 else "False" for x in [x.split(",") for x in out]])

def answer26(out):
    '''
    'Data contains a list of objects.  The answer is a list that contains the type of each of these elements.
    Create a list that contains the type of each element in the list provided. '
    '''
    return game.answer(26,list(map(type,out)))

def answer27(out):
    '''
    'Data contains a dictionary.  Submit a SORTED list of all of the keys in the dictionary. '
    '''
    return game.answer(27,sorted(out.keys()))

def answer28(out):
    '''
    'Data contains a dictionary.  Submit a SORTED list of all of the values in the dictionary.' 
    '''
    return game.answer(28,sorted(out.values()))

def answer29(out):
    '''
    ''Data contains a dictionary.  Submit a SORTED list of tuples.  There should be one tuple
    for each entry in the dictionary. Each tuple should contain a key and its associated value from the dictionary.' 
    '''
    return game.answer(29,sorted([(k, v) for k, v in out.items()]))

def answer30(out):
    '''
    'Data contains a dictionary.  Add together the integers stored in the dictionary entries with the keys "python" and "rocks" and submit their sum. '  
    '''
    return game.answer(30,out.get('python') + out.get('rocks'))

def answer31(out):
    '''
    "Data contains a dictionary of dictionaries.  The outer dictionary contains dates in the format of Month-Year.
    The value for each of those entries is another dictionary.  That dictionary contains Operating System classes
    as the key and its percentage of use in the target organization as the value.  What percentage of the attack
    surface was 'Vista' in '6-2017'?"    
    '''
    return game.answer(31,out.get('6-2017').get('Vista'))

def answer32(out):
    '''
    'Data contains a dictionary of dictionaries.  The outer dictionary contains dates in the format of Month-Year.
    The value for each of those entries is another dictionary.  That dictionary contains Operating System classes
    as the key and its percentage of use in the target organization as the value.  You have an exploit that will
    work against XP, NT and VISTA.  What month had the most vulnerable targets?  IE Add up the percentage for XP,
    NT and Vista.  Submit the month (1,2,3,4,5,6,7,8,9,10,11 or 12) that has the highest percentage. If two months
    have the same percentage submit the most recent.'
    
    I dont see how this can be done in 1 line
    '''
    high_total = 0.0
    for x in out:
        total_percent = float(out.get(x).get('Vista'))
        total_percent = total_percent + float(out.get(x).get('NT*'))
        total_percent = total_percent + float(out.get(x).get('WinXP'))
        if total_percent > high_total:
            high_total = total_percent
            high_month = x
        if total_percent == high_total:
            #print("Total percent is: %f and High Total is: %f" % (total_percent,high_total))
            if int(high_month.split('-')[0]) > int(x.split('-')[0]):
                high_month = x
    return game.answer(32,high_month.split('-')[0])

def answer33(out):
    '''
    'Data() contains the absolute path of a filename in your virtual machine.
    Determine the length of the file at that path. Open and read the contents of the file.
    Submit the file size (length of contents) as the answer.      
    '''
    return game.answer(33,len(open(out).read()))

def answer34(out):
    '''
    'The data() method returns an abosolute path to a directory on your file system.  Submit a sorted list of the filenames in that directory.'  
    '''
    return game.answer(34,sorted(os.listdir(out)))
                       
def answer35(out):
    '''
    'The Data() method will return a tuple.  The first item in the tuple contains the absolute path of a gzip compressed file in your virtual machine.
    The second item in the tuple is a line number.  Retreieve that line number from the specified file and submit it as a string.'  
    '''
    x = gzip.open(out[0]).readlines()
    return game.answer(35,x[out[1]-1].decode("utf-8"))

def answer36(out):
    '''
    'The data() method will return a string. Find all the text files beneath /home/student/Public/log/ that contain that string.
    The answer is a sorted list of all of the absolute paths to files that contain the string.  Do not uncompress gzip files.'
    '''
    log_home = '/home/student/Public/log/'
    to_be_returned = []
    for root,directoriews,files in os.walk(log_home):
        for ofile in files:
            if ofile[:-2] != "gz":
                with open(os.path.join(root,ofile)) as f:
                    try:
                        if out in f.read():
                            to_be_returned.append(os.path.join(root,ofile))
                    except:
                        pass
                        #print(os.path.join(root,ofile))
    return game.answer(36,sorted(to_be_returned))

def answer37(out):
    '''
    'Data contains a comma separated list of user names and passwords in the format user1 : password1, user2 : password2, etc.
    One of those passwords is the answer.  Guess which one. '
    '''
    return [game.answer(37,(x.split(': ')[1].strip())) for x in out.split(',')]

def answer38(out):
    '''
    'During incident response to some ransomware you learn that the malware is using a simple XOR encryption to encrypt a passphrases.
    You have determined that they are XORing every character in the passphrase with a 0x61.  Create a function that decrypts the passwords.
    Call your xor function to decrypt the password in the data element then submit the unencrypted passphrase.'    
    '''
    return game.answer(38,''.join(x for x in [chr(int(ord(a)) ^ 0x61) for a in out]))

def answer39(out):
    '''
    'You have determined that a stream encryption cypher is using repeating keys.  You XORed together two pieces of encrypted data which has the
    effect of eliminating the keys.  However the remaining data is still not clear text.  Instead it is the two pieces of original clear text data
    XORed together.  IE  (Data1 XOR key1) XOR (Data2 XOR key1) = (Data1 XOR Data2).  The Data element contains a list of two strings.  The first
    one is the encrypted data (Data1 XOR Data2).  The second one is some known clear text from either Data1 or Data2.  XOR the first string (Encrypted
    data) with the second string (clear text Data1 or Data2) to determine the other clear text data and submit the unencrypted string. '
   
    '''
    return game.answer(39,''.join(chr(x) for x in [ord(a) ^ ord(b) for a,b in zip(out[0],out[1])]))

def answer40(out):
    '''
    "Read the data element and submit the number of times any instance of the word 'python' (case insensitive) appears in the source. "
    
    '''
    return game.answer(40,out.lower().count('python'))
                       
def answer41(out):
    '''
    'Sentences end in a punctuation (period, question mark or exclamation mark) followed by two spaces.
    Data contains a paragraph with multiple sentences.  Use a regular expression to findall() sentences and submit a list of sentences. '

    '''
    return game.answer(41,re.findall(r"[A-Za-z0-9].+?\w*[.?!]\s\s",out))

def answer42(out):
    '''
    'Extract the SSNs from the data.  A SSN is any series of 9 consecutive digits.  Optionally, it may be a series of 3 digits followed by a
    space or a dash then 2 digits then a space or a dash followed by 4 digits.  Submit a list of SSNs in the order they appear in the data.
    All your SSNs should be in the format XXX-XX-XXXX'
    '''
    return game.answer(42,[x.replace(' ', '-') if ("-" or " ") in x else '-'.join([x[:3], x[3:5], x[5:]]) for x in re.findall(r"\d{9}|\d{3}\-\d{2}\-\d{4}|\d{3}\s\d{2}\s\d{4}",out)])

def answer43(out):
    '''
    'Data contains a several entries with strings and integers. Each entry is separated by an exclamation mark.   Break each string every x characters
    where x is the integer after the comma.  For example 123456,2 becomes the list ["12", "34", "56"].  Submit a list of lists as the answer [[list for
    first entry],[list for second entry],[list for third entry]].  ' 
    '''
    return game.answer(43,[re.findall('.{' + re.escape(i[1]) +'}',i[0]) for i in [x.split(',') for x in out.split("!")]])

def answer44(out):
    '''
    'The Data element contains a string from a mysterious programming language.  In this language variable names begin with an
    uppercase letter and end with the same uppercase letter.  For example in this line: ZAxuZAuA   There are two variables ZAxuZ and AuA.
    Notice that there is a capital A inside the variable ZAxuZ but it is not the start of a new variable because it is part of another variable.
    To make things more complex a variable name may contain the same uppercase letter than begins and ends the variable name if it is escaped with a 0.
    So the line ZAp0ZuZAuX0AZA contains the variables ZAp0ZuZ and AuX0AZA.  Use a regular expression to parse the line of code and extract all the
    variable names.  Submit a comma separated string of variable names.'
    
    definitely a multi-line answer

    '''
    return game.answer(44,"pass")


def answer45(out):
    '''
    'Read the data element and return a list of images in the HTML (marked by IMG [one or more html img tags] SRC or IMG DATA-SRC)
    in the order in which they appear in the source. '
    '''
    return game.answer(45,list(itertools.chain.from_iterable([[y for y in x if "http" in y] for x in re.findall(r"src=\\\'([\w\W]+?)\\\'|data-src=\"([\w\W]+?)\"|src=\"([\w\W]+?)\"",out) ])))


def answer46(out):
    '''
    'The data() contains filename of a BIND DNS log and a host name.  Open the file specified from the /home/student/Public/log/dnslogs directory.
    The answer is a sorted list of all the client IP addresses in the specified log file that queried that host.'
    '''
    return game.answer(46,sorted(re.findall(r'client\s(\d+.\d+.\d+.\d+)\#\d{5}:\squery:\s'+out[1],open('/home/student/Public/log/dnslogs/'+out[0]).read())))

def answer47(out):
    '''
    'The data() contains a client IP address.   Parse all of the DNS log files in /home/student/Public/log/dnslogs and return a sorted list of all the
    hostnames that were queried by that client.  Do not eliminate duplicates.'
    
    97.68.73.114#62709: query: fe2.update.microsoft.com IN A + ((8.8.8.8))
    '''
    return game.answer(47,[list(itertools.chain.from_iterable([re.findall(r"client\s%s#\d{5}:\squery:\s(\w+.\w+.\w+)" % out,open(os.path.join('/home/student/Public/log/dnslogs',i)).read()) for i in f[2]])) for f in os.walk('/home/student/Public/log/dnslogs')][0])

def answer48(out):
    '''
   'The data contains a Country Code.  Use GeoIPLite to find all of the Client IP addresses that are in the dnslogs from that country.
   The dnslogs are located in /home/student/Public/log/dnslogs/.  Submit a sorted unique list of IP addresses from that country found in the logs.
   HINT: You only have three seconds. Some modules are faster than others.'
   
   definitely a multi-line answer
    '''
    
    return game.answer(48,"pass")

def answer49(out):
    '''
    'Find the nth most frequently occurring User-Agent String in the log file /home/student/Public/log/apache2/access.log where n is the integer returned
    by the data method.'
    
    definitely a multi-line answer
    '''
    return game.answer(49,"pass")

def answer50(out):
    '''
    The data() method will return a string that you must convert to a scapy packet by calling 'somevar = Ether(.data())'.
    Then extract the TCP Sequence number and submit it as the answer.
    '''
    return game.answer(50,Ether(out)[TCP].seq)

def answer51(out):
    '''
    "The data() method will return a string that you must convert to a scapy packet by calling 'somevar = Ether(.data())'.   Submit the payload of the packet."
    '''
    return game.answer(51,Ether(out)[IP].load)

def answer52(out):
    '''
    "The data() method will return a list of strings that you must convert to a scapy PacketList by calling 'somevar = scapy.plist.PacketList([Ether(x) for x in
    .data()])'.   Then extract the flag that is embedded in the ICMP payloads and submit it as a string."
    '''
    return game.answer(52,''.join([x[Raw].load.decode() for x in scapy.plist.PacketList([Ether(x) for x in out])]))

def answer53(out):
    '''
    'Read /home/student/Public/packets/web.pcap  Commands are embedded in the packet payloads between the tags <command> and </command>.  The
    .data() method will give you a command number.  Submit that command as a string as the answer.  For example if .data() is a 5 you submit the 5th command that
    was transmitted.  Ignore blank commands (ie <command></command>).'
    '''
    return game.answer(53, "pass")

def main():
    print("Answer 0")
    print(answer0())
    print("Answer 1")
    print(answer1())
    print("Answer 2")
    print(answer2())
    print("Answer 3")    
    print(answer3())
    print("Answer 4")
    print(answer4())
    print("Answer 5")
    print(answer5())
    print("Answer 6")
    print(answer6())
    print("Answer 7")
    print(answer7(game.data(7)))
    print("Answer 8")
    print(answer8(game.data(8)))
    print("Answer 9")
    print(answer9(game.data(9)))
    print("Answer 10")
    print(answer10(game.data(10)))
    print("Answer 11")
    print(answer11(game.data(11))) 
    print("Answer 12")
    print(answer12(game.data(12)))
    print("Answer 13")
    print(answer13(game.data(13)))
    print("Answer 14")
    print(answer14(game.data(14)))
    print("Answer 15")
    print(answer15(game.data(15)))
    print("Answer 16")
    print(answer16(game.data(16)))
    print("Answer 17")
    print(answer17(game.data(17)))
    print("Answer 18")
    print(answer18(game.data(18)))
    print("Answer 19")
    print(answer19(game.data(19)))
    print("Answer 20")
    print(answer20(game.data(20)))
    print("Answer 21")
    print(answer21(game.data(21)))
    print("Answer 22")
    print(answer22(game.data(22)))
    print("Answer 23")
    print(answer23(game.data(23)))
    print("Answer 24")
    print(answer24(game.data(24)))
    print("Answer 25")
    print(answer25(game.data(25)))
    print("Answer 26")
    print(answer26(game.data(26)))
    print("Answer 27")
    print(answer27(game.data(27)))
    print("Answer 28")
    print(answer28(game.data(28)))
    print("Answer 29")
    print(answer29(game.data(29)))
    print("Answer 30")
    print(answer30(game.data(30)))
    print("Answer 31")
    print(answer31(game.data(31)))
    print("Answer 32")
    print(answer32(game.data(32)))
    print("Answer 33")
    print(answer33(game.data(33)))
    print("Answer 34")
    print(answer34(game.data(34)))
    print("Answer 35")
    print(answer35(game.data(35)))
    print("Answer 36")
    print(answer36(game.data(36)))
    print("Answer 37")
    print(answer37(game.data(37)))
    print("Answer 38")
    print(answer38(game.data(38)))
    print("Answer 39")
    print(answer39(game.data(39)))
    print("Answer 40")
    print(answer40(game.data(40)))
    print("Answer 41")
    print(answer41(game.data(41)))
    print("Answer 42")
    print(answer42(game.data(42)))
    print("Answer 43")
    print(answer43(game.data(43)))
    print("Answer 44")
    print(answer44(game.data(44)))
    print("Answer 45")
    print(answer45(game.data(45)))
    print("Answer 46")
    print(answer46(game.data(46)))
    print("Answer 47")
    print(answer47(game.data(47)))
    print("Answer 48")
    print(answer48(game.data(48)))
    print("Answer 49")
    print(answer49(game.data(49)))
    print("Answer 50")
    print(answer50(game.data(50)))
    print("Answer 51")
    print(answer51(game.data(51)))
    print("Answer 52")
    print(answer52(game.data(52)))
    print("Answer 53")
    print(answer52(game.data(53))) 
    game.logout


if __name__ == "__main__":
    main()
    
    