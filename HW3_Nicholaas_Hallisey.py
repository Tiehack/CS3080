'''
Homework 3
Name: Nicholaas Hallisey
Date: 2/21/23
Description: This program is meant to expand my knowledge on dictionaries and practice
more python concepts we went over in class.
'''

import pprint

#For Part 2
#This function takes the string sent in as a parameter, saves it as a dictionary and prints how many of each letter is in the string
def printDictionary(incomingString):
    #Declaring the dictionary
    characterDictionary = {}

    #Scans each letter inside the dictionary
    for char in incomingString:
        #If the letter has already scanned, implement its count by one
        if char in characterDictionary:
            characterDictionary[char] += 1
        #Otherwise, insert the letter inside the dictionary
        else:
            characterDictionary[char] = 1

    #Prints every letter inside the dictionary with pprint() and how many times a letter appears
    print("Each character in the string and how many times they appear:")
    pprint.pprint(characterDictionary)
    print()


#For Part 3
#Prints the contents of the dictionary sent in as a parameter
def printInventory(incomingDictionary):
    print("Here is the following inventory of items:")
    pprint.pprint(incomingDictionary)
    print()

#Adds the following item to the dictionary that is sent in as a parameter
def addItem(incomingDictionary, item):
    #If the item already exists in the dictionary, increment it's count by one
    if item in incomingDictionary:
        incomingDictionary[item] += 1
    #Otherwise, add it to the dictionary
    else:
        incomingDictionary[item] = 1
    print()

    #Return the changed dictionary
    return incomingDictionary

def deleteItem(incomingDictionary, item):
    #If the count of the particular item is 0, it notifies the user
    if incomingDictionary[item] == 0:
        print('There is none of this item:', item)
    #Otherwise, it will decrement that item's count inside the dictionary
    else:
        incomingDictionary[item] -= 1

    # Return the changed dictionary
    return incomingDictionary

#For Part 4
#Simulates tic tac toe
def ticTacToe():
    #Saving the board as a dictionary with empty keys
    board = {'1': ' ', '2': ' ', '3': ' ',
             '4': ' ', '5': ' ', '6': ' ',
             '7': ' ', '8': ' ', '9': ' '}

    #This function prints the contents of the updated board everytime it's called
    def printBoard(board):
        print('[', board['1'], ']', '[', board['2'], ']', '[', board['3'], ']')
        print('[', board['4'], ']', '[', board['5'], ']', '[', board['6'], ']')
        print('[', board['7'], ']', '[', board['8'], ']', '[', board['9'], ']')

    #Prints the empty board for the user
    printBoard(board)

    #For a total of nine tries
    for i in range(9):
        #The user who's turn it is selects which slot they'd like to fill
        print('Choose what slot you would like to fill')
        slot = input()

        #That user types what they'd like to fill inside that slot
        print('What would you like to fill that slot with?')
        letter = input()

        #If the selected slot is empty, it fills it with what the user typed in
        if board[slot] == ' ':
            board[slot] = letter
        else:
            #Otherwise it alerts the user that it has already been filled
            print("That slot has already been filled")

        #Prints the updated board
        printBoard(board)

#Part 1
#Saves the grid a dictionary
grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]

#Prints the contents of the grid board with a nested for loop
for i in range(6):
    for j in range(9):
        if j < 8:
            print(grid[j][i], end = "")
        else:
            print(grid[j][i])

print()

#Part 2
#Sends the following string inside the printDictionary functiton
charString = "The quick brown fox jumps over the lazy dog."
printDictionary(charString)

#Part 3
#Tests out the printInventory function with the following dictionary
Inventory = {"Hand Sanitizer" : 10, "Soap" : 6, "Kleenex" : 22, "Lotion" : 16, "Razors" : 12}
printInventory(Inventory)

#Updates the inventory dictionary with the following item
addItem(Inventory, "Advil")
print(Inventory)

#Updates the inventory dictionary with the following item again
addItem(Inventory, "Advil")
print(Inventory)

#Updates the inventory dictionary by decrementing the following item
deleteItem(Inventory, "Advil")
print(Inventory)

#Updates the inventory dictionary by decrementing the following item again
deleteItem(Inventory, "Advil")
print(Inventory)

#Updates the inventory dictionary by decrementing the following item
deleteItem(Inventory, "Advil")

#Part 4
#Utilizes the tikTacToe function
ticTacToe()
