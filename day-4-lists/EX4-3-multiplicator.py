# EXERCISE 4-1
# multiplicator

from random import uniform
from statistics import mean

# initialise empty list
rnd_numbers = [];

for i in range(10):
    # generate float number between 0 and 10 then round to 2 decimals
    num = round(uniform(0, 10.00), 2)
    # add to the list
    rnd_numbers.append(num)

# !!! empty line before the "List"
print("\nList:", rnd_numbers)

# multiplication
list_mult = 1
for x in rnd_numbers:
    list_mult *= x

print("Result of multiplication =", list_mult);

# sum
list_sum = sum(rnd_numbers)
print("Sum =", list_sum);

# average
list_avg = mean(rnd_numbers)
print("Avg =", round(list_avg, 2));

# min
list_min = min(rnd_numbers)
print("Min =", list_min);

# max
list_max = max(rnd_numbers)
print("Max =", list_max, "\n");