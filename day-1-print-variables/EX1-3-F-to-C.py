# F to C converter
# you can use float() instead of int() to convert string to number
print('|------- Fahrenheit to Celsium converter -------|');
#input
F = int(input("Enter temperature(Fahrenheit) F="))

#calculation
C = (F - 32) * 5 / 9

# round C to 2 decimals
C = round(C, 2)

# output
print(F,"F = ", C, "C");
# empty line
print("\n");