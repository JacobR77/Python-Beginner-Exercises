'''
Let’s say I give you a list saved in a variable:
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
Write one line of Python that takes this list a and makes a
new list that has only the even elements of this list in it.'''

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for value in a:
	if value % 2 ==0:
		print (value)

#More list comprehension practice

squares = []
for x in range(11):
	squares.append(x**2)

print (squares)

cubes = [x**3 for x in range(11)]
print (cubes)

names = ['Emmet','Nial','Curtis','Stephen','James']
print (names)

proper_names = ['FDnA ' + individual for individual in names]
print (proper_names)