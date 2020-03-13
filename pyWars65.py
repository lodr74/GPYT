'''


>>> game.question(65)
'NAME:Unrange - Data will contain a comma separated list of integers. If there is a complete series of
incrementing numbers replace it with a start and stop separated by a dash. This is the opposite of the Python range function.
So 2,4,6,7,8,10,11,-4,-3,-2,14,15,16,18,17,16 will become  2,4,6-8,10-11,-4--2,14-16,18,17,16.  '

>>> game.data(65)
'12,13,14,-18,-28,90,87,-87,95,-33,6,7,8,9,10,1,2,91,13,-83,-85,63,-80,96,71,61,62'
>>> 

1) Caputer number in a variaable
2) loop through numbers until the number to the right is not equal to +1 to the previous number
  a) if the number to the right is not equal then write the captured # to the list
  b) if the # to the right is equal then write the ranged numbers starting with the captured variable to the list

'''

import pyWars

game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")

def answer1(data1):
    print("Data1 is:  \n %s" % data1)
    output_list = []
    starting_pt = ''
    output = ""
    holding_list = []
    data = data1.split(",")
    dat_len = len(data)
    #print(dat_len)
    x = 0
    while x != dat_len:
        i = data[x]
        if i == data[-1] and len(holding_list) == 0:
            print("i was: %s is the last element and i not in the holding_list" % i)
            output_list.append(i)
            break
        elif i == data[-1] and len(holding_list) != 0:
            print("i was: %s is the last element and i in the holding_list" % i)
            output_list.append(holding_list[0] + "-" + holding_list[-1])
            holding_list = []
            break
        else:
            j = data[x+1]
        if int(i)+1 == int(j):
            print("I was: %s and J was: %s in the (i+1)==j" % (i,j))
            holding_list.append(i)
        if int(i)+1 != int(j) and len(holding_list) == 0:
            print("I was: %s and J was: %s in the i!=j and holding_list == 0" % (i,j))
            output_list.append(i)
        if int(i)+1 != int(j) and len(holding_list) != 0:
            print("I was: %s and J was: %s in the i!=j and holding_list != 0" % (i,j))
            holding_list.append(i)
            print(holding_list)
            output_list.append(holding_list[0] + "-" + holding_list[-1])
            holding_list = []
        x+=1
    for num in output_list:
        if output == '':
            output = num
        else:
            output+=","+num
    print(data1)
    print(output)
    return output

print(game.answer(65,answer1(game.data(65))))
game.logout