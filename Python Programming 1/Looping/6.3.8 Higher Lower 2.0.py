my_float = float(3.3312)

# Your code here...
rounded_float = round(my_float, 2)

while True:
    guess = float(input("Guess my number: "))
    rounded_guess = round(guess, 2)
    if rounded_guess == rounded_float:
        break
    elif guess > my_float:
        print("Too high!")
    elif guess < my_float:
        print("Too low!")
print("Correct!")
