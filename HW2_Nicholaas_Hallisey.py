'''
Homework 2
Name: Nicholaas Hallisey
Date: 2/15/23
Description: This program is meant to practice more python. This program includes
all of the instructions specified on canvas. It contains the collatz function, the
print functions and the guessingGame functionality.
'''

#Allows me to use random
import random

#Collatz (Part 1)
def collatz(number):
    #Tries the following code and searches for errors
    try:
        number = int(number)

        if number % 2 == 0:
            number = number // 2
            print(number)
            return number
        elif number % 1 == 0:
            number = 3 * number + 1
            print(number)
            return number

    #If there is an issue, it prints the following message and quits the program
    except:
        print("Your answer must be an integer")
        quit()

#This function prints all of the elements of a list with commas after each element
#and adds 'and' in front of the last element
def strList(incomingList):
    for i in incomingList:
        if i == incomingList[-1]:
            print("and", i)
        else:
            print(i, end = ", ")

#Function for the guessing game
def guessingGame():

    #Randomly generates a lower and upper bound guess
    lowerBounds = random.randint(0, 50)
    upperBounds = random.randint(51, 100)

    #Creates a list that will store already used guesses so they can't be used again
    guesses = []

    #Generates the random number that is supposed to be guessed
    number = random.randint(lowerBounds, upperBounds)

    #Prints the following message to the console
    print('I am thinking of a number between', lowerBounds, 'and', upperBounds, 'You have 10 tries.')

    #Simulates a turn for each guess
    for i in range(10):
        print('Take a guess')

        #Guesses the number
        guess = random.randint(lowerBounds, upperBounds)

        #Checks to see if the guess has already been used, if it has it guesses again
        notInList = False
        while notInList == False :
            if guess in guesses:
                guess = random.randint(lowerBounds, upperBounds)
            else:
                guesses.append(guess)
                notInList = True

        #Prints the current guess
        print(guess)

        #Prints the conditions for the guesses
        if guess > number:
            print("Your guess is too high")
        elif guess < number:
            print("Your number is too low")
        elif guess == number:
            print("Good job! You guessed my number in", i, "guesses")
            break


#Gathers input from user
print("Enter a number:")
userAnswer = input()

#Runs the user through the collatz function until their number is 1
while (userAnswer != 1):
    userAnswer = collatz(userAnswer)
print()

#Part 3
print('Item List:')
itemList = ['Wallet', 'Phone', 'Keys']
print(itemList)
print()

#Sorts the list
print('Sorted List:')
itemList.sort()
print(itemList)
print()

#Prints first item in list
print('First item in list:')
print(itemList[0])
print()

#Slices the list and prints everything except first element
print('Sliced List:')
sliceIndex = slice(1, 3)
print(itemList[sliceIndex])
print()

#Prints last item in list
print('Last item in list:')
print(itemList[-1])
print()

#Searches for specified element in list then returns location
print('Keys is at index', itemList.index('Keys'))
print()

#Adds the following element to the list
print('Adding tablet to the list')
itemList.append('Tablet')
print(itemList)
print()

#Adding the following element to the list at specified location
print('Adding mask to the list')
itemList.insert(2, 'Mask')
print(itemList)
print()

#Removes the following element from list
print('Removing phone from the list')
itemList.remove('Phone')
print(itemList)
print()

#Reverses the list
print('Reversing the list')
itemList.reverse()
print(itemList)
print()

#Prints the list using the strList function
print('Printing list...')
strList(itemList)
print()

#Runs program through guessingGame function
guessingGame()