# Discount calculator
sum = input("Enter the total \033[31msum\033[0m of money spent: $")
sum = float(sum)

if sum >= 500:
    discount = 10.00
else:
    discount = 0.00

# to pay after discount
sum_disc = sum * discount / 100
pay_after_disc = sum  - sum_disc

print(f'Discount applied: \033[31m${sum_disc}\033[0m ({discount}%)')
print(f'Total to Pay after Discount: $\033[31m{pay_after_disc}\033[0m')