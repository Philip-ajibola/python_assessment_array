import print_odd_and_even_position_in_list

def test_odd_and_even_position_function():
	list = [1,2,3,4,5,6,7]
	check =[1,3,5,7]
	check1 = [2,4,6]
	assert print_odd_and_even_position_in_list.odd_position(list)==check
	assert print_odd_and_even_position_in_list.even_position(list)==check1
