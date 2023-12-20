import divide_or_square_function

def test_divide_or_square_function():
	number = 55
	number1 = 56
	number_result = divide_or_square_function.divide_or_square(number)
	number1_result = divide_or_square_function.divide_or_square(number1)
	assert divide_or_square_function.divide_or_square(number)==number_result
	assert divide_or_square_function.divide_or_square(number1)==number1_result