'''
#Homework 1
#Name: Nicholaas Hallisey
#Date: 1/26/2023
#Description of your program: The purpose of this program was to practice the basics of python and put them together
to make a working program. This program simulates security software that sends a code to an email and if the code is
correct, the user can answer the security questions. If all three are answered correctly a secret message will be displayed.
'''

#Allows me to use the random function for the program
import random

#This function will hold all of the code that asks the security questions
def answerSecurityQuestions():

    #This will act as a counter everytime an question is answered correctly
    correctAnswers = 0

    #This boolean will flag when to display the secret message
    allAnsweredCorrectly = False

    #This list holds all of the answers for the security questions
    securityAnswers = ['Earth', 'Human', 'Food']

    #This variable holds the secret message as a string
    secretMessage = 'Congratulations, you belong in college after all. I cannot say the same for my creator :('

    #This code just prints the following message to the console for the user
    print()
    print('Please answer the security questions. They are the most simple obvious answers')
    print('Answer them all correctly, a secret message will be revealed.')
    print()

    #This loop will keep asking the questions until at least one of them is answered correctly
    while correctAnswers < 1:

        #Using a loop, the first question will be asked once
        for i in range(1):
            print('What planet were you born on?')
            answer1 = input()
            continue
        #If the answer matches what's in the list, it increments the correct answer counter
        if answer1 == securityAnswers[0]:
            correctAnswers += 1
        #If the answer is immature, the program quits completely
        elif answer1 == 'Uranus':
            print('Bro, get out of here')
            break

        # Using a loop, the first question will be asked once
        for i in range(1):
            print('What species are you?')
            answer2 = input()
            continue
        # If the answer matches what's in the list, it increments the correct answer counter
        if answer2 == securityAnswers[1]:
            correctAnswers += 1

        # Using a loop, the first question will be asked once
        for i in range(1):
            print('What do humans eat?')
            answer3 = input()
            continue
        # If the answer matches what's in the list, it increments the correct answer counter
        if answer3 == securityAnswers[2]:
            correctAnswers += 1

    # Prints the following messages based on the following conditions
    if correctAnswers == 3:
        print('Nice, you got all of the answers right')
        allAnsweredCorrectly = True
    elif correctAnswers > 0:
        print('You got at least one of the answers right')
    elif correctAnswers < 1:
        print('You got none of the answers right. Come on :(')
    else :
        print('You broke the laws of reality if you are reading this.')

    #If the boolean has been flagged true, the secret message will be displayed
    if allAnsweredCorrectly:
        print('Secret message: ', secretMessage)


#Prints the following message to console
print('Hello, please enter your email address')

#Initializing a variable that simulates the email address
emailAddress = input()

#This variable is a random int that simulates a security code
#The number starts off as two large randomly generated floats, and adding them together and subracting one
decimalSecurityCode = random.randint(10000.00, 99999.00) + random.randint(10000.00, 99999.00) - 1

#The security code is then converted to an integer and doubled by two
integerSecurityCode = int(decimalSecurityCode) * 2

#Lastly the code is divided by four and the final calculation will be the security code for the user
quotientSecurityCode = integerSecurityCode // 4

#This converts the security code to a string
securityCode = str(integerSecurityCode)

#Displays the following message to the user
print("A", len(str(securityCode)), 'number security code has been sent to', emailAddress)
print('Security code: ' + str(securityCode))

print()
print('Please enter the security code that was sent to you')

#The user types in their answer for the security code
userAnswer = input()

#If the answer and the code don't match. The following message is displayed and the program ends
if userAnswer != securityCode :
    print('That is not correct')

#If the answer and code do match, the user will be sent to answer the security questions
else :
    print('That is correct')
    answerSecurityQuestions()
