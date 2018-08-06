#Is the number odd or even?


def oddoreven(x):
	x = int(input("Original- Please enter a number: "))
	if x % 2 != 0:
		return "odd"
	else:
		return "even"


print(oddoreven(1))

#additional challenges
#Challenge 1- Test to see if the value can be divided by 4

number = int(input("Challenge 1- Please enter a number: "))

if number % 4 == 0:
	print(str(number) + " is a multiple of 4")
else:
	print(str(number) + " is not a multiple of 4")


#Challenge 2. Ask the user for two numbers. Check if one divides into the other

def division_challenge(num,check):
	num = int(input("Challenge 2- Select a number: "))
	check = int(input("Challenge 2- Select a second number: "))
	if num % check == 0:
		return str(check) + " divides evenly into " + str(num) + "!"
	else:
		return str(check) + " does not divide evenly into " + str(num) + "!"

print(division_challenge(1,2))		