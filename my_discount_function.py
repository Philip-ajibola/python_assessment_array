def my_discount(price,discount):
	new_price = price*(1-(discount/100))
	return new_price

my_price = 800
discount = 6	

print(f'the actual price is {my_price} but with {discount}% discount you are paying {my_discount(my_price,discount)} ')