def check_float_number(number1,number2):
	total_float = 0
	if type(number1)== float:
		total_float+= 1
	if type(number2)== float:
		total_float+= 1
	return total_float

number1 = 12.6
number2 = 11.5

print('Total float number is ',check_float_number(number1,number2))
	
	
