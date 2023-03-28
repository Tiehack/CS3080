'''
Homework 5
Name: Nicholaas Hallisey
Date: 3/22/23
Description: This program is meant to utilize concepts of python that involve iterations and conservation of memory.
'''

#Imports the math library
import math

#Part 1
#Creates the class for the reverse iteration
class ReverseIter:
    #We initialize a new iterator set it to expect a new list
    def __init__(self, incomingList):
        self.incomingList = incomingList
        self.index = len(incomingList)

    #Setting the return of the iterator.
    def __iter__(self):
        return self

    #The functionality that tells the iterator to read the incoming list backwards
    def __next__(self):
        self.index -= 1
        if self.index >= 0:
            return self.incomingList[self.index]
        else:
            raise StopIteration

#Defining a new list
aList = ['A', 'B', 'C', 'D', 'E']

#Sends the list into the iterator
readBackwards = ReverseIter(aList)

#Use the iterator to read and print the list backwards
for item in readBackwards:
    print(item)

#Line spacing
print()

#Part 2
#Creating the generator function
#This generates a set of integers. I used this from the example code used in class
def integers():
    i = 1
    while True:
        yield i
        i += 1

#This generates a sequence of numbers for the pyt function to use. I used this from the example code used in class
def take(n, seq):
    seq = iter(seq)
    result = []
    try:
        for i in range(n):
            result.append(next(seq))
    except StopIteration:
        pass
    return result

#Defining the pyt function
def pyt():
    #Takes the integers from integers function. This will act as our hypotenuse.
    for z in integers():
        #Loops and takes numbers from a range of one to the hypotenuse. This acts our x side variable.
        for x in range(1, z):
            #Loops and takes numbers from a range of x + 1 to the hypotenuse. This acts as our y side variable.
            for y in range(x + 1, z):
                #If our x, y and z variables follow the laws of the pythagorean theorm, they check as triplets
                if math.pow(z, 2) == math.pow(x, 2) + math.pow(y, 2):
                    #They are then yielded.
                    yield (x, y, z)

#Setting n to 10, so it will print the first 10 triplets
n = 10
print(take(n, pyt()))
print()

#Part 3
#Simulates the range function but yields the sequence rather than generates them, to save memory.
def genrange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

#Uses the genrange function to start at 0, stop at 5, and increment by 1 each time.
for i in genrange(0, 5, 1):
    print(i)