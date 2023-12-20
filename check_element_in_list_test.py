import check_element_in_list

def test_check_element_function():
	list = [10,15,29,34,56,78]
	check = 78
	check1 = 90
	assert check_element_in_list.check_element(list,check)==True
	assert check_element_in_list.check_element(list,check1)==False


