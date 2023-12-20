import concantinate_two_list_function

def test_concantinate_two_list_function():
	list = [1,2,3,4]
	list1 = ['a','b','c','d']
	list2 = [1,2,3,4,'a','b','c','d']
	list3 = [1,'a',2,'b',3,'c',4,'d']
	assert concantinate_two_list_function.concantinate_two_list(list,list1)==list2
	assert concantinate_two_list_function.combine_two_list(list,list1)==list3