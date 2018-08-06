#Python Exercise #1

#import datetime module
import datetime

now = datetime.datetime.now()

#Enter name and age#
name = input("What is your name? ")
age = int(input("What is your age? "))

year_when_100 = int(now.year) + (100-age)

#print("You will turn 100 in " + str(year_when_100))

'''print_copies = int(input("How many copies do you need printed? "))
while print_copies >0:
	print("You will turn 100 in " + str(year_when_100) + "\n")
	print_copies = print_copies-1'''

def copies_to_print(x):
	while x > 0:
		print ("You will turn 100 in " + str(year_when_100) + "\n")
		x = x-1

print(copies_to_print(8))


