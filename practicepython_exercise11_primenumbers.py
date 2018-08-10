num = int(input("Insert a number: "))
a = [x for x in range(2,num) if num % 2 ==0]

def is_prime(n):
	print(a)
	if num> 1:
		if len(a) == 0:
			print ("prime")
		else:
			print ("Not prime")
	else:
	 	print ("Not prime")			

is_prime(num)
	




