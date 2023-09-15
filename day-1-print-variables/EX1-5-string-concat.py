# string concatination

first_name = input("Enter your first name: ")
family_name = input("Enter your family name: ")
role = input("Enter your role: ")

result_string = first_name + " " + family_name + " (" + role + ")"

# print result (colored text)
print("Result:\033[95m", result_string, "\033[0m");

# empty string:
print("\n")