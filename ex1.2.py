#HELLO

try:
    input = raw_input
except:
    pass


x = int(input("Enter integer 1: "))
y = int(input("enter integer 2: "))
a = x+y
b = x*y
c = x/y
print("%d + %d = %d" % (x,y,a))
print("%d * %d = %d" % (x,y,b))
print("%d / %d = %06.2f" % (x,y,c))
