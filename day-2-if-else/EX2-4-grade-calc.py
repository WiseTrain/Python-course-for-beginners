# grade calculator
# pre-set variables for text colors:
RED = "\033[31m"
GREEN = "\033[32m"
RESET_COLOR = "\033[0m"

# user input
# I will use GREEN and RESET_COLOR instead of awkward value "\033[31m"
mark = input(f"Enter your exam mark (0-100): {GREEN}")
mark = float(mark)

# if input is incorrect I will finish the program (exit)
# it is called "early exit"
if mark < 0 or mark > 100:
    # I will use RED and RESET_COLOR instead of awkward value "\033[31m"
    print(f"{RED}Incorrect input: the mark must be a number between 0 and 100%.{RESET_COLOR}")
    exit()

## ********* v1. *********
# if mark >= 90 and mark <=100:
#     grade = "A+"
# elif mark >= 80 and mark < 90:
#     grade = "A"
# elif mark >= 70 and mark < 80:
#     grade = "B"
# elif mark >= 60 and mark < 70:
#     grade = "C"
# elif mark >= 50 and mark < 60:
#     grade = "D"
# else:
#     grade = "Fail"

# ***** v2 *****
if mark >= 90:
    grade = "A+"
elif mark >= 80 :
    grade = "A"
elif mark >= 70:
    grade = "B"
elif mark >= 60:
    grade = "C"
elif mark >= 50:
    grade = "D"
else:
    grade = "Fail"


# I will use GREEN and RESET_COLOR instead of awkward value "\033[32m"
print(f"{RESET_COLOR}Your grade is {GREEN}{grade}{RESET_COLOR}")


