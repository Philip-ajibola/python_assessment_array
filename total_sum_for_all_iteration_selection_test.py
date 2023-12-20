import total_sum_for_all_iteration_selection

def test_total_sum_for_all_iteration_selection_function():
	number = [10,20,30,40,50]
	assert total_sum_for_all_iteration_selection.total_sum_for_forLoop(number)==150
	assert total_sum_for_all_iteration_selection.total_sum_for_whileLoop(number)==150
	assert total_sum_for_all_iteration_selection.total_sum_for_doWhileLoop(number)==150