magic_number = 3

# Your code here...
while True:
    guess = int(input("Guess my number: "))
    if guess == magic_number:
        print("You got it!")
        break
    elif guess > magic_number:
        print("Too high!")
print("Correct!")
