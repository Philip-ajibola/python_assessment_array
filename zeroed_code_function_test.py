import zeroed_code_function

def test_zeroed_code_function():
	number1 = [5,6,7,8,9]
	result = [0,6,7,8,0]
	assert zeroed_code_function.zeroed_code(number1)==result