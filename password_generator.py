#This will be my first personal Python project. I have a desire to build a quick, easy to use
#password generator. This generator will perform the following tasks:

#   -The program will prompt the user to enter an amount of characters.
#   -The program will also ask for a site or service that the password is for
#    which will allow the program to save the password attached to this site (for future reference).
#   -The program will then create a string of letters (uppercase and lowercase),
#    digits, and symbols, constricted to the amount of characters supplied by the user.
#   -The program will print this string, allowing the user to copy and paste this for their
#    desired usage.

import random
import string
import datetime

abc_lower = list(string.ascii_lowercase) #List of all lowercase letters of the alphabet
abc_upper = list(string.ascii_uppercase) #List of all uppercase letters of the alphabet
digits = [str(x) for x in range(0, 10)] #Numbers from 0 to 9 converted to strings
characters = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'] #All chacaters that can be printed in Python
password = ""
loop = True

def createPassword(desired_characters):
    pass

def savePassword(password, intended_purpose):
    pass

print("""\nWelcome to homing-pidgeon's password generator!\n
To begin, the program will require a number of characters corresponding to 
the length of your desired password. A password will then be generated that
is entirely random, and therefore incredibly strong in its security! These 
passwords can be found in a .txt file generated with each password.\n""")

while(loop):
    try:
        desired_characters = int(input("How long should the password be? (Maximum 30)\n"))
    except ValueError:
        print("Only numbers can be entered. Please try again.")
    else:
        if desired_characters not in range(0, 31):
            print("This is an invalid input. Please keep inout a number between 0 and 30.")
        else:
            loop = False
            break

intended_purpose = input("For what site or service is this password to be associated with?\n")

random_password = createPassword(desired_characters)
file_name = savePassword(password, intended_purpose)
print("Your randomized password is: {}".format(random_password))
print("This password will be stored in a file named {}.txt for future reference.".format(file_name))
