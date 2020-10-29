# Caroline Davis (cnd7cy)
import random
'''
This python file allows the user to play a simple number guessing game with the computer.

:param: answer = int value of the correct answer to the game
:param: guesses = the amount of guesses the user gets to find the answer
:param: guessAnswer = int value that the user guesses to be the answer
:return: This program has four outputs: "You win" if the user guesses correctly; "The number is lower than that" 
        if the user's guessAnswer value needs to lower; "The number is higher than that" if the user needs to 
        input a higher guessAnswer; "You lose" with the correct answer if the user is unable to guess the 
        answer correctly.
'''

answer = int(input("What should the answer be? "))
if answer == -1:
    answer = random.randrange(0, 100)

guesses = int(input("How many guesses? "))

guessAnswer = int(input("Guess a number: "))
if guessAnswer == answer:
    print("You win!")

for i in range(guesses - 1):
    if guessAnswer == answer:
        print("You win!")
        break

    elif guessAnswer > answer:
        print("The number is lower than that.")
        guessAnswer = int(input("Guess a number: "))

    elif guessAnswer < answer:
        print("The number is higher than that.")
        guessAnswer = int(input("Guess a number: "))

if guessAnswer != answer:
    print("You lose; the number was", str(answer) + ".")
