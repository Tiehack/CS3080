'''
Homework 4
Name: Nicholaas Hallisey
Date: 3/8/2023
This program is meant to practice more python coding. This program covers a few concepts that can be solved
with the math and read library. The solutions are set accordingly.
'''

#Adds the libraries to the program
import math
import re

#For Part 1
#Creating a class that represents a rectangle
class Rectangle:
    #Constructs the rectangle object
    def __init__(self, length, width):
        self.length = length
        self.width = width

    #Function for calculating and returning the area
    def area(self):
        return self.length * self.width

    #Function for calculating and returning the diagonal
    def diagonal(self):
        return math.sqrt(math.pow(self.length, 2) + math.pow(self.width, 2))

    #Function for calculating and returning the perimeter
    def perimeter(self):
        return (self.length + self.width) * 2

#Creating a class that represents a circle
class Circle:
    #Constructor for the circle object
    def __init__(self, radius):
        self.radius = radius

    #Function for calculating and returning the area
    def area(self):
        return self.length * self.width

    #Function for calculating and returning the diameter
    def diameter(self):
        return 2 * self.radius

    #Function for calculating and returning the perimeter
    def perimeter(self):
        return 2 * math.pi * self.radius

#Class that represents a square
class Square:
    #Constructor for the square object
    def __init__(self, side):
        self.side = side

    #Function for calculating and returning the area
    def area(self):
        return self.side * self.side

    #Function for calculating and returning the diagonal
    def diagonal(self):
        return math.sqrt(math.pow(self.length, 2) + math.pow(self.width, 2))

    #Function for calculating and returning the perimeter
    def perimeter(self):
        return (self.side + self.side) * 2

#For part 3
#This function takes a string and checks to see if it passes all of the condtions for a valid password
def checkPassword(password):
    #Checks to see if the password is of valid length
    if len(password) < 8:
        print("Password must be at least 8 characters")
        return False

    #Checks to see if the password contains a lowercase letter
    if not re.search("[a-z]", password):
        print("Password must have at least one lowercase letter")
        return False

    #Checks to see if the password contains a capital letter
    if not re.search("[A-Z]", password):
        print("Password must have at least one capital letter")
        return False

    #Checks to see if the password contains a digit
    if not re.search("[0-9]", password):
        print("Password must contain at least one number")
        return False

    #If all checks, the function returns true meaning the string is a valid password
    else:
        print("Your password has been set")
        return True

#Part 1
#Creating a rectangle with rectangle class
myRectangle = Rectangle(20, 10)

#Creating a circle that uses functions from rectangle class
myCircle = Circle(myRectangle.diagonal() / 2)

#Prints the perimeter of the circle
circlePerimeter = myCircle.perimeter()
print(circlePerimeter)

#Part 2
#Setting a pattern that matches an email address
emailPattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

#Setting a pattern that matches a phone number
phoneNumberPattern = r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b'

#Declaring a string for the program to read
clipBoard = "970-321-5212, MyEmail@gmail.com"

#Takes the string and checks to see if any characters match the email pattern
emailAddresses = re.findall(emailPattern, clipBoard)

#Takes the string and checks to see if any characters math the phone number pattern
phoneNumbers = re.findall(phoneNumberPattern, clipBoard)

#Prints any found email addresses in the string
for email in emailAddresses:
    print(emailAddresses)

#Prints any found phone numbers in the string
for numbers in phoneNumbers:
    print(numbers)

#Part 3
#Keeps the loop running until the function clears the string for a valid password
validPassword = False

#Loops while the validPassword Boolean is False
while validPassword == False:
    #Prompts the user for password and they enter it
    print("Type in a valid password. It must have at least 8 values, contains uppercase and lowercase letters, and at least one digit")
    password = input()

    #Sends the entered password into the checkPassword funciton that checks if it's valid
    if checkPassword(password):
        #If the function returns True, the loop breaks
        validPassword = True

