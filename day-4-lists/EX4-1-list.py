# EXERCISE 4-1
# create a list from input
# my code is a bit more advansed as
# I use TRY...EXCEPT statement to TRY to convert my input to float
# you may just comment the code between (1) and (2)

# create empty list
num_list = []
for i in range(5):
    # enter element
    element = input("Enter any string or number: ");

    # try to convert to float
    # (1)
    try:
        # program tries to convert input to float
        element = float(element)
    except:
        # program goes here if it's impossible to convert to float
        print(f"It's impossible to convert \"{element}\" to float")
    #(2)

    # add element into list
    num_list.append(element)

# dipslay list
print("My list:",num_list)
# empty line
print("\n");

