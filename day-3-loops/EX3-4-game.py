# exercise 3-4. "Guess the number game"
import random

#pre-set colours
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

print(f'''
*************************************
{GREEN}Welcome to the Guess the Number game!{RESET}
*************************************

I have chosen a number between {GREEN}1{RESET} and {GREEN}20{RESET}. Can you guess it?''')

# generate the number
secret_number = random.randint(1, 20)
# print(secret_number);

# set the initial value of the user_guess
user_guess = -1
# counter = number of attempts
counter = 0

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# I will use endless loop to demonstrate how to exit the loop (break): 
# while True:
# You may use 
# while user_guess != secret_number:
# ---- it is also correct ----
while True:
    user_guess = input(f"Enter your guess (between 1 and 20):{GREEN} ");
    user_guess = int(user_guess)

    # increment counter
    counter += 1

    # compare user's guess with secret number
    if user_guess == secret_number:
        print(f"{GREEN}Congratulations! You guessed the number {user_guess} in {counter} attempts.{RESET}")

        # !!!! exit the loop !!!!
        break

    elif user_guess > secret_number:
        print (f"{RED}Too high! Try again.{RESET}")
    elif user_guess < secret_number:
        print (f"{RED}Too low! Try again.{RESET}")


# empty line
print("\n");