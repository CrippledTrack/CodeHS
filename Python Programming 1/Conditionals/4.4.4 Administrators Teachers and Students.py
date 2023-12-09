who = input("Are you an administrator, teacher, or student?: ")

if who == "teacher":
    print ("Administrators and teachers get keys!")
elif who == "administrator":
    print ("Administrators and teachers get keys!")
elif who == "student":
    print ("Students do not get keys!")
else:
    print ("You can only be an administrator, teacher, or student!")
