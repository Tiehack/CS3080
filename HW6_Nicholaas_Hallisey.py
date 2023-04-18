"""
Homework 6
Name: Nicholaas Hallisey
Date: 4/14/23
Description: The purpose of this assignment is to practice using our programs with real time and to practice the concepts
of decorator functions and utilize their mechanics of editing already existing functions.
"""

#Importing the following libraries
import functools
import time
import sys
import pyperclip

# Part 1
# Defines the decorator function
def slow_down(func):

    # Sleep 1 second before calling the function
    @functools.wraps(func)

    # This is the modified function that is returned
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)

    # Returns the modified function
    return wrapper_slow_down


# Executes slow down before calling the funciton
@slow_down

#Defining the following function
def countdown(from_number):
    #Prints the following message when the countdown is less than 1
    if from_number < 1:
        print("Liftoff!")
    #Otherwise it prints and decrements the countdown
    else:
        print(from_number)
        countdown(from_number - 1)

#Calls countdown and starts at 5t
countdown(5)
print()


# Part 2
#Taking the following function that was used in class
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

#defining the cache function
def cache(func):
    #Creating a dictionary for the cache
    cache_dict = {}

    #Defining the wrapper function
    def wrapper(*args):
        #If the incoming argument already exists in the dictionary, it's returned
        if args in cache_dict:
            return cache_dict[args]
        #Otherwise the argument is added to the dictionary
        else:
            result = func(*args)
            cache_dict[args] = result
            return result

    #Returns the wrapper function
    return wrapper

#Calls the cache decorator and runs the changes on the old fibonacci function
@cache
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

#Prints the first 10 values of the edited fibonacci function
for i in range(10):
    print(fibonacci(i))

# Part 3
# Creating a dictionary that saves all of the clipboard changes
clipboard_dict = {}

# Parse the command line arguments
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':

    # Saves the current clipboard text under the specified keyword
    clipboard_dict[sys.argv[2].lower()] = pyperclip.paste()
    print(f"Text saved under keyword '{sys.argv[2].lower()}'")

elif len(sys.argv) == 2 and sys.argv[1].lower() == 'list':

    # Print a list of all saved keywords
    print("Saved keywords:")
    for key in clipboard_dict.keys():
        print(key)

elif len(sys.argv) == 2:

    # Copy the clipboard text associated with the specified keyword to the clipboard
    keyword = sys.argv[1].lower()

    if keyword in clipboard_dict:
        pyperclip.copy(clipboard_dict[keyword])
        print(f"Text from keyword '{keyword}' copied to clipboard")

    else:
        print(f"No text saved under keyword '{keyword}'")

else:

    # Invalid command line arguments
    print("Usage:")
    print("  To save clipboard text: python mcb.py save <keyword>")
    print("  To retrieve clipboard text: python mcb.py <keyword>")
    print("  To list saved keywords: python mcb.py list")
