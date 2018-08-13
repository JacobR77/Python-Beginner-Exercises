'''Write a program (function!) that takes a list and returns a new list that
contains all the elements of the first list minus all the duplicates.'''

def duplicates(x):
	return set(x)
	

user_list = input("Input a list: ")
print(user_list)

print(duplicates(user_list))