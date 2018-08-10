'''Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high,
or exactly right.'''

#import module for random number generation
import random

#set stop to false
stop = False


#set up while statement
while (not stop):

#produce random number between 1 and 9 (inclusive)
	generated_number = random.randint(1,10)

#get user guess
	user_guess = int(input("Please guess a number between 1 and 9: "))

	if user_guess > generated_number:
		print ("Too high! The answer was " + str(generated_number) )
	elif user_guess < generated_number:
		print ("Too low! The answer was " + str(generated_number) )
	elif user_guess == generated_number:
		print ("Exactly right! The answer was " + str(enerated_number) )
	else:
	 	print ("are you sure you entered a number between 1-9?")

#check if they want to play again
	answer = input("Do you want to play again? Yes or No")

	if answer.upper()== "YES":
		print ("New game starting...")
	elif answer.upper() == "NO":
		stop = True
		print ("Game Over")
	else: print('Wrong answer, please type Yes or No in your next attempt!')

