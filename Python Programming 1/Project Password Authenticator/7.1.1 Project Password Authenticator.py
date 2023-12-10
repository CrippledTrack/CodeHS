password = "potato123"
 
for i in range(3):
    guess = input("Enter your password: ")
    if guess == password:
# Stops code is correct password is guessed
        print("Correct password! Access granted.")
        break
# prints text shown and reloops if maximum number of attempts has been reached
    elif i != 2:
        print("incorrect password please try again")
#prints text shown below and stops code
    else:
        print("incorrect password. Maximum number of attempts reached. Access denied.")
        break
