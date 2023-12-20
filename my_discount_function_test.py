import my_discount_function

def test_my_discount_function():
	price = 950
	discount = 25
	assert my_discount_function.my_discount(950,25)==712.5
