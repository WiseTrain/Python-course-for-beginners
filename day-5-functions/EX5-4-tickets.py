# ticket price calculator

# calculates the ticket price
# parameters: age (int number) and f_student (boolean)
# By default the person is NOT a student (False)
def ticket_price_calculator(age, f_student=False):

    if f_student and age > 5:
        return 15.00
    
    if age <=5:
        return 0.00
    elif age <= 18 or age > 65:
        return 20.00
    else:
        return 30.00;

print("Ticket price for age 65 is", ticket_price_calculator(65))
print("Ticket price for age 50 is",ticket_price_calculator(50))
print("Ticket price for age 50 (student) is",ticket_price_calculator(50, True))
print("Ticket price for age 5 is",ticket_price_calculator(5))
print("Ticket price for age 15 is",ticket_price_calculator(15))