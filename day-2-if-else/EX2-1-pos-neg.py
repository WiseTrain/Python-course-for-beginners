# Discount calculator
number = input("Enter any numeric value: ")
number = float(number)

if number > 0:
    num_type = "positive"
elif number < 0:
    num_type = "negative"
else:
    num_type = "zero"

print(f'This number is {num_type}.')