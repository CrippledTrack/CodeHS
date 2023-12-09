initial = int("1000")
deposit = "deposit"
withdrawl = "withdrawal"
deposit_or_withdrawl = input("deposit or withdrawl: ")
if deposit_or_withdrawl == withdrawl:
    final = int(input("enter amount: "))
    balance = (initial - final)
    if final <= 999:
        print("You have "+str(balance))
    else:
        print("you cannot have a negative balance!")
elif deposit_or_withdrawl == deposit:
    final = int(input("enter amount: "))
    balance = (initial + final)
    print ("you have "+str(balance))
else:
    print ("Invalid transaction")
