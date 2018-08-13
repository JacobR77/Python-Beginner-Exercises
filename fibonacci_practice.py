def fibonacci():
	x = int(input("How many runs?: "))
	sequence = [1,1]
	counter = 1
	while counter < x-1:
		n = sequence[-1] + sequence[-2]
		sequence.append(n)
		counter +=1
	return sequence

print(fibonacci())
