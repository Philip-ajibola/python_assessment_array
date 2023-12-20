def divide_or_square(number):
	if number%5==0:
		number1=number**0.5
	if number%5!=0:
		number1=number%5
	return number1

number = 55
number1 = 59
print(divide_or_square(number))
print(divide_or_square(number1))
		
		


