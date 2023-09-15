# EXIRCISE 6-1
# greeting generator
from time import strptime

# returns a greating (str) depending on the time
# parameter: time (string "HH:MM")
def greeting_generator(time):

    if time < "00:00" or time > "23:59":
        result = "Hello"
    elif time <= "11:59":
        result = "Good morning"
    elif time <= "17:59":
        result = "Good afternoon"
    else:
        result = "Good evening"

    return result

# *******************************************
# V2. Use strptime() from time module
# to convert string "HH:MM" to datetime datatype
def greeting_generator_v2(time_str):
    result = "Hello"

    # trying to convert the string to datetime datatype
    try: 
        time_variable = strptime(time_str, '%H:%M')
    except:
        return result
    
    if time_variable < strptime("12:00", '%H:%M'):
        result = "Good morning"
    elif time_variable < strptime("18:00", '%H:%M'):
        result = "Good afternoon"
    else:
        result = "Good evening"

    return result
    


# test 1. input = 00:00
# expected: "Good morning"
print("00:00", greeting_generator("00:00"))
# work as axpected

# test 2. input = "11:59"
# expected: "Good morning"
print("11:59", greeting_generator("11:59"))
# work as expected

# test 3. input = "15:00"
# expected: "Good afternoon"
print("15:00", greeting_generator("15:00"))
# work as expected

# test 4: input = 18:00
# expected: "Good evening"
print("18:00", greeting_generator("18:00"))
# work as expected

# test 5: input = 23:88
# expected: "Hello"
print("23:88", greeting_generator("23:88"))
# work as expected

# test 6: input = 0000000
# expected: "Hello"
print("0000000", greeting_generator("0000000"))
# work as expected

# test 7: input = "15:99"
# expected: "Hello"
print("15:99", greeting_generator("15:99"))
# actual output = "Good afternoon"
# !!! doesn't work as expected

# current date and time 
# print(datetime.datetime.now())