# EX 6-1. Random password
from random import choice
import string

# generates a password containing
# letters, digits and punctuation

# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)
# print(string.printable)

# ******************************************
# v.1
def password_generator_v1(pwd_length):
    # length of the password:

    # all characters: letters + digits
    # use \ if you need to continue your command to next line 
    char_alphanumeric = "0123456789abcdefghijklmnopqrstuvwxy\
        zABCDEFGHIJKLMNOPQRSTUVWXYZ"
    char_punctuation = "!$%&'()*+,-/:;<=>?@[\]^_{|}~"

    pwd = ""
    for i in range(pwd_length-1): 
        pwd += choice(char_alphanumeric)
    pwd += choice(char_punctuation) 

    return pwd


# ****************************************
# v.2 - string library
def password_generator_v2(pwd_length):
    # length of the password:
    PWD_LENGTH = 10 

    # all characters: letters + digits
    char_alphanumeric = string.ascii_letters + string.digits
    # print(char_alphanumeric)

    pwd = ""
    for i in range(pwd_length-1): 
        pwd += choice(char_alphanumeric)
    pwd += choice(string.punctuation) 

    return pwd


# test: 
print("\nNew password is:", password_generator_v1(10))
print("New password is:", password_generator_v2(20), "\n")