'''
Write a program (using functions!) that asks the user for a long string containing multiple
 words. Print back to the user the same string, except with the words in backwards order.
  For example, say I type the string:

My name is Michele

Then I would see the string:

Michele is name My

shown back to me.'''

string = "My name is Jacob"

split_string = string.split(" ")

print(split_string)

print(len(split_string))
print(split_string[-1::-1])

def reversal():
	x = input("Type a string: ")
	split_string = x.split(" ")
	split_string = split_string[-1::-1]
	output = " ".join(split_string)
	return output

print(reversal())	
