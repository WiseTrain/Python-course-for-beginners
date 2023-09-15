# n + nn + nnn calculator
# two correct versions (v.1 and v.2) see below

# welcome message:
print("\033[33m|||||||||| n + nn + nnn calculator ||||||||||\033[0m");
#
# input
n = input("Enter any digit n=")


# ******************************************
# **************    v.1  *******************
# Use "\n" if you need to go to new line
print("\nv.1")

# calculation
nn = n + n
nnn = n + n + n
print(n, type(n), nn, type(nn), nnn, type(nn))

# incorrect:
# result = n + nn + nnn
# correct: 
result = int(n) + int(nn) + int(nnn)
print(f'n + nn + nnn = {result}')


# ******************************************
# **************    v.2  *******************
print("\nv.2")
n = int(n);
print(n, type(n))

nn = 10*n + n
nnn = 100*n + 10*n + n
result = n + nn + nnn
print(f'{n} + {nn} + {nnn} = {result}\n')

