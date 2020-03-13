'''
>>> game.question(79)
'NAME:Crazy-Credit - During an internal penetration test you find a SQL injection vulnerability that allows you to extract
what appears to be encrypted data from the "CreditCard" field of a database.   You create an account with the credit card number
"4111111111111111" and use the SQL injection to look at its encrypted value.  Its encrypted value is "04x46O6xPTOe0T.   Then you
change that credit card number to "4111111111111112" and the encrypted value becomes "04x46O6xPTOe06".  This is obviously not real
encryption but an encoding scheme of some kind.  You report the findings and say it must be changed.  In a politically charged
meeting with the CEO and the website developer, the developer insists that it is a "proprietary encryption scheme" that cant be
broken and refuses to change it.  You insist that it can be broken.  The CEO turns to you and says "Prove it".  The CEO asks you
to decrypt ALL of the credit card numbers in the database.   You go back to your office and enter a few more values credit card
numbers then check the corresponding encoded value.  You have the following credit card numbers and their encoded values.
0=e, 1=H, 2=4, 3=f, 4=M, 5=0, 6=P, 7=x, 8=k, 9=T, 10=6, 11=O, 12=1, 13=B, 14=He, 15=HH, 16=H4, 17=Hf, 18=HM, 19=H0, 20=HP.
Examining the results you determine this is a base14 number where the values 0-13 (normally represented by the characters
0123456789ABCD) are represented by the the characters \'eH4fM0PxkT6O1B\'.   Looking back in the database you find every credit
card entry has a unique corresponding field called "enc_key" and the record for your credit card has that exact string
(\'eH4fM0PxkT6O1B\') in the enc_key field.   \nTo decrypt the credit card number "04x46O6xPTOe0T" with a key of \'eH4fM0PxkT6O1B\'
you replace all \'e\' in the credit card number with 0.  \'H\' with 1. \'4\' with 2 and so on.  You get an result of \'5272ABA769B059\'
and use the "int() function to convert your base14 number to base10.  You call int(\'5272ABA769B059\', 14) and get a result of
"4111111111111111".  Success! You decrypted their supposedly encrypted credit card.   But there is a problem.  The int() function
can only be used to convert bases between 2 and 36 and most of the credit cards have an enc_key that is more than 32 characters
long and are thus more than base32.   You must write a function that given an enc_key and an encoded credit card number will
produce a clear text version of the credit card number. \nThe data element contains two strings separated by a comma.  The first
part is the "enc_key" field from the database that contains characters that represent the base system characters.   The second part
is a credit card number "encrypted" in those characters that you must convert to decimal.  You will know what the base is by looking
at the length of string of characters in the enc_key field.    For example, if the data element contained \'0123456789ABCDEF, FF\'
then \'FF\' is a credit card number "encrypted" as a base16 number where \'0123456789ABCDEF\' represents the digits.  \'A\' is at the
10th position in the string of characters and \'F\' is at the 15th position.   So \'AF\' is 10*16**1+15*16**0 = 175.  \n\nRead the data
element and submit the clear text credit card number by converting it to a decimal value.  The base length, characters and credit card
number will be random.'

>>> game.data(79)
'3FgYfeDvhS0LbAai4kyBCrdw8uoNQHVlKcZWsOqmE29nPjtJ1MGIUX657zR,NR52jfWS9'
>>>

'''

import pyWars
import os

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")


def answer1(data1):

        
print(game.answer(79,answer1(game.data(79))))
game.logout