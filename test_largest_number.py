import largest_number

def test_largest_function():
	assert largest_number.largest(27,19,10)==27
	assert largest_number.largest(81,191,7)==191
	assert largest_number.largest(21,6,91)==91