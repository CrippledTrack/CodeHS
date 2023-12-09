#ingredient one number/name
ingredient_one = input("Enter ingredient 1:")
amount_one = input("Ounces of "+ingredient_one +":")

#ingreditent two number/name
ingredient_two = input("Enter ingredient 2:")
amount_two = input("Ounces of "+ingredient_two +":")

#ingredient three number/name
ingredient_three = input("Enter ingredient 3:")
amount_three = input("Ounces of "+ingredient_three +":")

#number of servings
servings = input("Number of servings:")

#calculating number of ingreidents needed
total_one = float(float(amount_one) * int(servings))
total_two = (float(amount_two) * int(servings))
total_three = (float(amount_three) * int(servings))

#displaying number of ingreidents needed
print ("Total ounces of "+ingredient_one + ": "+ str(total_one))
print ("Total ounces of "+ingredient_two + ": "+ str(total_two))
print ("Total ounces of "+ingredient_three + ": "+ str(total_three))
