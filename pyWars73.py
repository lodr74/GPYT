'''
>>> game.question(73)
'NAME:Compare-and-predict - You have conducted analysis on a two factor authentication token,
R-es-A, and have determined that it is not as random as the creators perhaps hoped.  Due to your
awesome hacking skills, you have man in the middle access and have captured the last several responses
the user sent to the server.  You need to log in by faking the users authentication.  Correctly predict
the next number output by the secure token. '

>>> game.data(73)
[445, 4886, 53737, 591098, 6502069, 71522750]

[554, 6085, 66926, 736177, 8097938, 89077309]

[358, 3929, 43210, 475301, 5228302, 57511313]

[721, 7922, 87133, 958454, 10542985, 115972826] 
[140, 1531, 16832, 185143, 2036564, 22402195]
[598, 6569, 72250, 794741, 8742142, 96163553] 
[407, 4468, 49139, 540520, 5945711, 65402812]

1) Increment the last number by 1 and make it a holder
2) Add the last number and the number to left it together.  Subtract 1
    a) if there was a remainder put it in a holder
3) take the number to the left of of the last and the number to the left of it, add them together
    a) if there was a remainder in the previous function add it
    b) if there is a remainder put them in a holder
4) add the remainder and the number to the left of it together.
    a) if no remainder it carries over

'''

import pyWars
import itertools


game = pyWars.exercise()
game.login("mleigh","N0Passw0rd")

def firstNumber(num1, remainder):
    firstNum = int(num1) + int(remainder)
    return str(firstNum)

def lastNumber(num1,num2):
    print("The first number is: %s  and the 2nd number is: %s in function lastNumber" % (num1,num2))
    evalNumber = int(num1)+1
    #print("The eval num: is %s" % evalNum)
    holder = []
    if evalNumber > 9:
        for i in str(evalNumber):
            holder.append(i)
        lastNum = holder[1]
        print("The last num: is %s" % lastNum)
        remainder = holder[0]
        print("The remainder num: is %s" % remainder)
    else:
        lastNum = evalNumber
        remainder = 0
        print("The last num: is %s" % lastNum)
        print("The remainder num of the last num: is %s" % remainder)
    secondToLast = int(num1) + int(num2) + -1 + int(remainder)
    print("The Second to last number is: %i" % secondToLast )
    print("The remainder num of the last num: is %s" % remainder)
    return str(lastNum), str(secondToLast)

def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str

def doMath(num1,num2,remainder):
    remLst = []
    result = int(num1)+int(num2)+int(remainder)
    print("Adding %s to %s to %s = %i" % (num1, num2, remainder, result))
    if result > 9:
        for i in str(result):
            remLst.append(i)
        remainder = remLst[0]
        result = remLst[1]
    return str(result), str(remainder)

def answer1(data1):
    remainder = 0
    workingNum = data1[-1]
    print(workingNum)
    revNum = reverse(str(workingNum))
    print(revNum)
    lastNum, secToLastNum = lastNumber(revNum[0],revNum[1])
    x = 0
    finalNum = ''
    finalNum = lastNum + finalNum
    scndLastList = []
    if int(secToLastNum) > 9:
      for i in str(secToLastNum):
        scndLastList.append(i)
      remainder = scndLastList[0]
      secToLastNum = scndLastList[1]
      finalNum = secToLastNum + finalNum
    else:
      remainder = 0
      finalNum = secToLastNum + finalNum
    revNumLen = len(revNum)
    for i in itertools.islice(revNum, 1, revNumLen-1):
        print("i is: %s and remainder is: %s and the position in the string array is: %i and the value of X+1 is: %s" % (i,remainder, x,revNum[x+2] ))
        if i != x-1:
            result, remainder = doMath(i,revNum[x+2],remainder)
            print("The next num in the string  is: %s and the remainder is %s" % (result, remainder))
            finalNum = result + finalNum
            x+=1
        
    firstNum = firstNumber(revNum[-1],remainder)
    print("The first num is: %s" % firstNum)
    finalNum = firstNum + finalNum
    return finalNum
        
print(game.answer(73,answer1(game.data(73))))
game.logout