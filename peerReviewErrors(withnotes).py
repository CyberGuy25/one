# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: <author>
# Creation Date: <date>
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave():
    cave = ''
	while cave != '1' and cave != '2':
		print('Which cave will you go into? (1 or 2)')
		cave = input()
#the variable caves has not been defined
	return caves

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	#arguement is incorrect if we want to sleep for 2 seconds
	time.sleep(3)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		#perenthesis are missing from the call to the print function
		print 'Gobbles you down in one bite!'

playAgain = 'yes'
#need to use == (check for logical equivelance) not = (assignment)
while playAgain = 'yes' or playAgain = 'y':
	displayIntro()
	caveNumber = choosecave()
	checkCave(caveNumber)

	print('Do you want to play again? (yes or no)')
	playAgain = input()
	#check for playAgain=='n'
	if playAgain == "no":
		print("Thanks for planing")
