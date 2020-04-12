#author Chris "homing-pidgeon" Pidgeon
#date Sunday 12, April 2020

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
from datetime import date
from datetime import datetime

abc_lower = list(string.ascii_lowercase) #List of all lowercase letters of the alphabet
abc_upper = list(string.ascii_uppercase) #List of all uppercase letters of the alphabet
digits = [str(x) for x in range(0, 10)] #Numbers from 0 to 9 converted to strings
characters = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'] #All chacaters that can be printed in Python
full_characters = abc_lower + abc_upper + digits + characters #All characters, letters, and digits possible
random.seed()

def createPassword(desired_characters, intended_purpose):
    password = ""
    length = desired_characters
    count = 0

    while count < length:
        password = password + random.choice(full_characters)
        count += 1

    status = savePassword(password, intended_purpose)
    if status == True:
        print("\nYour randomized password is: {}".format(password))
        print("Your password can be found for future reference in the file just created for you!")
        print("\nThank you!")

def savePassword(password, intended_purpose):
    today = date.today()
    time = datetime.now()

    current_time = time.strftime("%H:%M:%S")
    date_formatted = today.strftime("%d/%m/%y")
    intended_purpose_alternate = intended_purpose.upper()
    file_created = False
    try:
        file = open("{}.txt".format(intended_purpose), "x")    
    except FileExistsError:
        print("\nFile already exists.")
        return file_created
    else:
        file_created = True

    if(file_created == True):
        print("\nFile {}.txt created.".format(intended_purpose))
        file.write("Password {} created at {} on {} for {}.".format(password, current_time, date_formatted, intended_purpose))
        file.close()
        return file_created

print("""\nWelcome to homing-pidgeon's password generator!\n
To begin, the program will require a number of characters corresponding to 
the length of your desired password. A password will then be generated that
is entirely random, and therefore incredibly strong in its security! These 
passwords can be found in a .txt file generated with each password.\n""")

loop = True
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

intended_purpose_input = input("\nFor what site or service is this password to be associated with?\n")
createPassword(desired_characters, intended_purpose_input)
