#first number
a = 0
#second number
c= 0
for i in range(6):
    a = a+1
    for j in range(6):
        # used to reset second number to 0 when loop is restarted
        c= j + 1
        print(str(a) + "," +str(c))
