# math calculations
# you can use int() instead of float() to convert string to number

#input
print("Enter numeric values: ")
x = float(input("x = "))
y = float(input("y = "))
z = float(input("z = "))

#calculation and output
result = x * (1 + x**2/y**2)**z + z*y*z
print("result =", result);