###############################################################################
###############################   Imports   ###################################
###############################################################################

# Used to generate a random number.
import random
# Used to use user input from command prompt.
import sys

###############################################################################
##########################   Global Variables   ###############################
###############################################################################

# Stores the number of digits.
numberOfDigits = 1

###############################################################################
##############################   Functions   ##################################
###############################################################################
def guess_the_number():
	""" Generates a random number, prompts the user to guess a number, takes 
		the user inputs and validates the input. If the user input is equal to
		the random number, prints a success message, else prompts the user to 
		make another guess by informing if the guess was too low or too high.
	"""

	# Specifying the number of digits is a global variable else python will
	# create a new local variable.
	global numberOfDigits

	# Calculating the min and max n-digit number where n is the length provided
	# by the user. 
	minNumber = 10**(numberOfDigits-1)
	maxNumber = 10**(numberOfDigits) - 1

	# Generating a random n-digit number
	randomInteger = random.randint(minNumber, maxNumber)

	# Initializing the count of guesses
	count = 0

	# Prompting the user to input a n-digit number
	userInput = raw_input("Guess a {0}-digit number: ".format(numberOfDigits))

	# The program will keep on prompting the user till they guess the correct
	# number.
	while True:
		# Check if the user has put in a number.
		try :
			guessedNumber = int(userInput)
			count += 1
		except :
			# Show validation if the user has entered a number
			userInput = raw_input("Invalid input. Try again: ") 
			continue
		else : 
			# If the guessed number is not n-digit, validate.
			if (guessedNumber < minNumber) or (guessedNumber > maxNumber):
				userInput = raw_input("Invalid input. Try again: ")
			# Print success message when the user guesses the correct number, 
			# else show validation and prompt the user to guess again.
			elif guessedNumber == randomInteger:
				# Breaking the print statement into two according to Python
				# style guide.
				print "Congratulations. You guessed the correct number in ", 
				print "{0} tries.".format(count)
				break
			elif guessedNumber > randomInteger:
				userInput = raw_input("Try again. Guess a lower number: ")
			else:
				userInput = raw_input("Try again. Guess a higher number: ")
				

###############################################################################
################################   Main   #####################################
###############################################################################
def main(): 
	"""	Starts the high low game. Takes the user input of number of digits and 
		retains it. If the user input is not available, defaults the number of 
		digits to 1."""
	# Specifying the number of digits is a global variable else python will
	# create a new local variable.
	global numberOfDigits

	# Sets the number of digits from the user input.
	try:
		numberOfDigits = int(sys.argv[1])
	# If the user does not provide the length, the number of digits is defaulted
	# to 1.
	except:
		numberOfDigits = 1

	# Starts the game.
	print "Let's play the mimsmind0 game."
	guess_the_number()

###############################################################################
############################   Boiler Plate   #################################
###############################################################################
if __name__ == '__main__':
    main()
