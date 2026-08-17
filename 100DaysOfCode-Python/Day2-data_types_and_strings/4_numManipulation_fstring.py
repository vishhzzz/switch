bmi = 84 / 1.65 ** 2
print("Your BMI is: ")
print(bmi)

# Now it is a very large number (decimal places)

# we can round it via certain ways
print(int(bmi)) # this will round it down to the nearest integer. 
# also known as flooring 

# we can do mathematical rounding using round() function
print(round(bmi))

# we can also round it to certain decimal places using round() function
print(round(bmi, 2)) # this will round it to 2 decimal places.

# we can also use f-string to format the output
print(f"Your BMI is: {bmi}") # this will print the BMI with all the decimal places.

print(f"Your BMI is: {bmi:.3f}") # this will print the BMI with 3 decimal places.