'''Create a program that asks the user for a number and then prints out a list of all
the divisors of that number. (If you don’t know what a divisor is, it is a number 
that divides evenly into another number. For example, 13 is a divisor of 26 because 
26 / 13 has no remainder.)'''

number = int(input("Please enter a number: "))


def divisor_function():
	x = range(1,number+1)	
	for element in x:
		if number % element ==0:
			print(element)


divisor_function()