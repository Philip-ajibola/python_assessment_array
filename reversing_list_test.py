import reversing_list

def test_reverse_list_function():
	list = [1,2,3,4,5,6]
	list1 = reversing_list.reverse_list(list)
	assert reversing_list.reverse_list(list)==list1

	