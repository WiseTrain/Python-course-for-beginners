# user input
sec = input("Enter the number of seconds:")

# convertion from string to int
# "try" is a special constraction in case of incorrect input
# it exits the program if the user entered "abc" instead of "100"
# "exit()" means "to exit the programm" = "finish"
try:
  sec = int(sec)
except:
  print("Invalid input: the value must be integer")
  exit()

#calculate number of days
dd = sec // (24 * 60 * 60) 
sec = sec % (24 * 60 * 60)

# calculate number of hours
hh = sec // (60 * 60)
sec = sec % (60 * 60)

# calculate number of minutes and seconds
mm = sec // 60
sec = sec % 60

print(f'{dd} : {hh} : {mm} : {sec}')

# tests
# 0, 60, 3600, ..., abc
