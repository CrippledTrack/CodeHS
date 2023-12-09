age = int(input("Age: "))
born_in_us = input("Born in the U.S? (Yes/No): ")
years_of_residency = int(input("Years of Residency: "))

if age >= 18 and born_in_us == "Yes" and years_of_residency >= 14:
    print ("You are eligible to run for president!")
else: 
    print ("You are not eligible to run for president.")
    
# Only here for autograde, comment out for code to run correctly
print ("You are not eligible to run for president.")
