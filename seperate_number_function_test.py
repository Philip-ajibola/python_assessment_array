import seperate_number_function

def test_seperate_number_function():
	number=1234
	assert seperate_number_function.seperate_number(number)==['1','2','3','4']
