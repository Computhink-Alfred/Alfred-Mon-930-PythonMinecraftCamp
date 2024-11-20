# Write all your codes for Day 3 here.
# REMEMBER to change main.py to import this file.
# You can COMMENT out the previous task before going on to the next task
# name = input("What is your name? ")

# print("Welcome back, " + name + "!")

# num1 = input("What is the 1st number to add? ")
# num2 = input("What is the 2nd number to add? ")

# ans = int(num1) + int(num2)
# print("The sum of " + num1 + " and " + num2 + " = " + str(ans))





# name = "Alfred"

# print("My name is " + name)

# input("What is your age? ") "15"

# print(10 + 5) #15
# print(int("10") + int("5")) #105

# num1 = int(input("What is the 1st number? "))
# num2 = int(input("What is the 2nd number? "))

# print(str(num1) + " + " + str(num2) + " = " + str(num1 + num2))
# print(str(num1) + " - " + str(num2) + " = " + str(num1 - num2))
# print(str(num1) + " x " + str(num2) + " = " + str(num1 * num2))
# print(str(num1) + " / " + str(num2) + " = " + str(num1 / num2))

# correctPassword = "ABCD"
# userPassword = input("What is the password? ")

# if correctPassword == userPassword:
#     print("Access Granted!")
#     name = input("What is your name? ")
#     print("Welcome home, " + name + "!")

# if correctPassword != userPassword:
#     print("I'm calling the police")



# YiHeng = int(input("What is your age? "))
# Jared = int(input("What is your age? "))

# if YiHeng == Jared:
#     print("Scenario 1")
# elif YiHeng > Jared:
#     print("Scenario 2")
# elif YiHeng < Jared:
#     print("Scenario 3")

# if YiHeng > Jared:
#     print("Scenario 1")

# if YiHeng == Jared:
#     print("Scenario 2")

# if YiHeng < Jared:
#     print("Scenario 3")


import random

randomNum = random.randint(1,5)
userGuess = int(input("Guess a number between 1 and 5: "))

if userGuess == randomNum:
    print("You are correct!")
else:
    print("You are wrong!")