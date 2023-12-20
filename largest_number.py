def largest(x,y,z):
	largest = 0
	if x>y and x>z:
		largest = x
	if y>x and y>z:
		largest = y
	if z>y and z>x:
		largest = z
	return largest
print(largest(4,5,6))
print(largest(99,89,17))
print(largest(0,1,2))
		