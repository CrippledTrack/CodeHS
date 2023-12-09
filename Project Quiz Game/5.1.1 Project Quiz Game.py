print("Multiple-Choice Quiz Game")
print("")

#a,b,c options are placeholders

# Question 1
print("Question 1")
print(" (a)")
print(" (b)")
print(" (c)")
print("")
answer_one = input("> ")
if answer_one == "a":
    print("Correct!")
    correct = (+1)
else:
    print("Incorrect.")
    
# Question 2
print("Question 2")
print(" (a)")
print(" (b)")
print(" (c)")
print("")
answer_two = input("> ")
if answer_two == "c":
    print("Correct!")
    correct = (correct+1)
else:
    print("Incorrect.")
    
# Question 3
print("Question 3")
print(" (a)")
print(" (b)")
print(" (c)")
print("")
answer_three = input("> ")
if answer_three == "c":
    print("Correct!")
    correct = (correct+1)
else:
    print("Incorrect.")
    
#Complete
print ("")
print ("Quiz complete!")
print ("you answered "+str(correct)+" out of 3 questions correctly")
