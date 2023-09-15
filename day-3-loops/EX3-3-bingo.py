# exercise 3-3
# bingo card
import random

# "\n" is new line
print("\n");

print("--------------------------");
for j in range(0, 2):
    res_str = "|"
    for i in range(0, 5):
        num = random.randint(1, 99);

        # extra space for one digit numbers (for alignment)
        if num < 10:
            res_str +=" "

        # accumulate all numbers in one string
        res_str += " " + str(num) + " |"

    print(res_str);
    print("--------------------------");

# new line
print("\n");