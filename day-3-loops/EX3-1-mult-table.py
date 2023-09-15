# Exercise 3.1
# Multiplication table
print('************************')
number = input("Enter any whole number: ")
number = int(number)

print("Multiplication Table for", number)
for i in range(1, 11):
    print(f"{number} x {i} = {i*number}")
    
print('************************')

