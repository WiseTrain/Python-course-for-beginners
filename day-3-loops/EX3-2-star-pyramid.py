# exercise 3-2
# star design

#(1)
for i in range(10):
    res_string = ""
    for j in range(i+1):
        res_string += "* "
    print(res_string);

# (2)
for i in range(10, 0, -1):
    res_string = ""
    for j in range(i):
        res_string += "* "
    print(res_string);

# "*" + "*" + "*" = "***"