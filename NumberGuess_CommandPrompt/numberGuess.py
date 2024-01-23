'''
Program: numberGuess.py
Chapter 3 example (Pg 90-91)
01/03/2024

Standard number guessing game application. User will provide the range of numbers for the game. program will prompt and guide tthe player until they get the correct number.
'''

import random
import time

# Input Phase
smaller = input('Please, enter the smaller number: ')
while smaller. isnumeric() != True:
	smaller = input('Sorry, please enter a small DIGIT: ')
smaller = int(smaller)

larger = input('Now, please enter the larger number: ')
while larger. isnumeric() != True:
	larger = input('Sorry, please enter a larger DIGIT: ')
larger = int(larger)

#Processing Phase
magicNum = random.randint(smaller, larger)
print('Selecting your magic number ...')
time.sleep(3)

# Variable to track the number of attempts for the game
count = 0
# loop to keep the game going until the number is guessed
while True:
	userNumber = int(input('Enter your guess: '))
	count += 1

	# Logic to determine the game outcome
	if userNumber < magicNum:
		print('Sorry, Your guess was too SMALL!')
	elif userNumber > magicNum:
		print('Sorry, Your guess was too BIG!')
	else:
		print('You guessed the correct number!')
		break

	# Output Phase
	input('Thanks for playing! Please press ENTER to QUIT.')
