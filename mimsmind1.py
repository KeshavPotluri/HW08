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
numberOfDigits = 3

# Stores the max number of chances
numberOfChances = 0

###############################################################################
##############################   Functions   ##################################
###############################################################################
def generate_number():
	"""Generates the a random number that is of length that is provided by the
		user"""
	global numberOfDigits

	# Initialize the random number 
	randomNumber = ''

	# Generate an n digit random number as a string.
	for number in range(numberOfDigits):
		randomNumber = randomNumber + str(random.randint(0,9))

	# Return the random number
	return randomNumber


def cows_and_bulls():
	"""Takes in the user input, validates it and returns the number of cows and
		bulls. If the user guesses correctly, show a success message. If the user
		exhausts his guesses, show an apologetic message."""
	# Specifying the number of digits is a global variable else python will
	# create a new local variable.
	global numberOfDigits
	global numberOfChances

	# Generating a random n-digit number
	randomInteger = generate_number()

	# Initializing the count of guesses
	count = 0

	# Prompting the user to input a n-digit number
	userInput = raw_input("Guess a {0}-digit number: ".format(numberOfDigits))

	# While the user still has chances left, compute the cows and bulls
	while count < numberOfChances:

		# initialize the number of cows and bulls
		numberOfCows = 0
		numberOfBulls = 0

		# store the random integer into a temperory number
		tempRandomInteger = randomInteger

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
			if len(userInput) != numberOfDigits :
				userInput = raw_input("Invalid input. Try again: ")
				continue
			# Print success message when the user guesses the correct number, 
			# else show validation and prompt the user to guess again.
			elif userInput == randomInteger:
				# Breaking the print statement into two according to Python
				# style guide.
				print "Congratulations. You guessed the correct number in ", 
				print "{0} tries.".format(count)
				break
			# If the user is not able to guess the correct number and exhausts all
			# the chances, throw a message.
			elif count == numberOfChances:
				print "Sorry. You did not guess the correct number in {0} tries.".format(numberOfChances), 
				print "The correct number is {0}.".format(randomInteger)
				break
			else:
				# Get the number of bulls by comparing digits at the same index
				for j in range(len(userInput)):
					if userInput[j] == randomInteger[j]:
						numberOfBulls += 1
				# Get the number of cows + bulls by checking if the digit in the
				# guess occurs in the generated number
				for j in range(len(userInput)):
					if userInput[j] in tempRandomInteger:
						index = tempRandomInteger.find(userInput[j])
						# remove the occurance so that it handles the condition where
						# digits repeat 777, 878 etc.
						temp = tempRandomInteger[:index] + tempRandomInteger[index+1:]
						tempRandomInteger = temp
						numberOfCows += 1
				# Tell the user the number of cows and bulls
				userInput = raw_input("{0} bulls(s), {1} cow(s). Try again: ".format(numberOfBulls, numberOfCows - numberOfBulls))

		


###############################################################################
################################   Main   #####################################
###############################################################################
def main(): 
	"""	Starts the Cows and Bulls game. Takes the user input of number of digits 
		and retains it. If the user input is not available, defaults the number of 
		digits to 3."""
	# Specifying the number of digits is a global variable else python will
	# create a new local variable.
	global numberOfDigits
	global numberOfChances

	# Sets the number of digits from the user input.
	try:
		numberOfDigits = int(sys.argv[1])
	# If the user does not provide the length, the number of digits is defaulted
	# to 1.
	except:
		numberOfDigits = 3

	# Sets the number of chances.
	numberOfChances = 2**numberOfDigits + 1

	# Starts the game.
	print "Let's play the mimsmind1 game. You have {0} guesses.".format(numberOfChances)
	cows_and_bulls()

###############################################################################
############################   Boiler Plate   #################################
###############################################################################
if __name__ == '__main__':
    main()
