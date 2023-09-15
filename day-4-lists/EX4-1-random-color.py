# EXERCISE 4-2
# random colours

from random import choice
# list of colours
COLOURS = ["\033[30m", "\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m", "\033[37m",
	    "\033[90m", "\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m", "\033[97m",
	    "\033[49m", "\033[40m", "\033[41m", "\033[42m", "\033[43m", "\033[44m", "\033[45m", "\033[46m", "\033[47m",
	    "\033[100m", "\033[101m", "\033[102m", "\033[103m", "\033[104m", "\033[105m", "\033[106m", "\033[107m"]

# reset the colour
RESET_COLOUR = "\033[0m"

for i in range(30):
    # select random colour from COLOURS
    sel_color = choice(COLOURS)
    # print "Hello, students!" with selected colour
    print(sel_color, "Hello, students!", RESET_COLOUR)