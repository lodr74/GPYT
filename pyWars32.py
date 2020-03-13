'''
Data contains a dictionary of dictionaries.  The outerThe value for each of those entries is another dictionary.  That dictionary contains Operating System classes
as the key and its percentage dictionary contains dates in the format of Month-Year.
The value for each of those entries is another dictionary.  That dictionary contains Operating System classes as the key and its percentage
of use in the target organization as the value.  You have an exploit that will work against XP, NT and VISTA.  What month had the most vulnerable targets?
IE Add up the percentage for XP, NT and Vista. Submit the month (1,2,3,4,5,6,7,8,9,10,11 or 12) that has the highest percentage.
If two months have the same percentage submit the most recent.


{'12-2017': {'Linux': '0.1', 'Mac': '0.03', 'WinXP': '0.08', 'Win7': '0.49', 'Vista': '0.27', 'Mobile': '0.29', 'NT*': '0.09'},
'5-2017': {'Linux': '0.12', 'Mac': '0.04', 'WinXP': '0.06', 'Win7': '0.46', 'Vista': '0.2', 'Mobile': '0.23', 'NT*': '0.07'}


- Cycle through each date key
    - Get the values foe XP,NT and Vista
        - Sum the values
    - store the date key and the sums as a value in a dictionary
    - sort values based on the largest sum
        - return the key for the largest sum
            - split the key by '-'
                - return the first element

'''

import pyWars
import codecs

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")

sums_dict = {}
x = 0

def answer1(data1):
    print(data1)
    for i in data1.items():
        #print(i)
        x = 0.0
        holder = i[1]
        #print(holder)
        #print(dir(holder))
        print(i[0])
        if 'NT*' in holder:
            print("X is before NT: %s" % str(x))
            x += float(holder.get('NT*'))
            print("X is after NT: %s" % str(x))
        if 'WinXP' in holder:
            print("X is before WinXP: %s" % str(x))
            x += float(holder.get('WinXP'))
            print("X is after WinXP: %s" % str(x))
        if 'Vista' in holder:
            print("X is before Vista: %s" % str(x))
            x += float(holder.get('Vista'))
            print("X is after Vista: %s" % str(x))
        print(type(x))
        sums_dict[i[0]] = x
        print(sums_dict)
    sorted_dict = (sorted(sums_dict.items(), key = lambda kv:(kv[1], kv[0]), reverse=True))
    print(sorted_dict)
    for j in sorted_dict:
        z = j[0].split('-')
        print(z[0])
        return str(z[0])
        break
            
print(game.answer(32,answer1(game.data(32))))
game.logout