# EX5-3 FACTORIAL(n)
# calculates factorial n!
# parameters: n (any integer number) 
def factorial(n):
    # check if the input is integer
    # exit the function if not
    if not(isinstance(n, int)):
        print("Incorrect input.")
        return -1
    
    f = 1
    for i in range(1, n+1):
        f *= i
    return f;


n = input("\nEnter any whole number: ")

# try to convert the input into integer
try: 
    n = int(n)
except:
    print("Incorrect input.")
    exit(0)

print(f"{n}! = {factorial(n)}\n")