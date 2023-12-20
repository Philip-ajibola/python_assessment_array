def concantinate_two_list(list,list1):
	list2 =list+list1
	return list2

def combine_two_list(list,list1):
	list2=[]
	for  number in range(len(list)):
		list2.append(list[number])
		list2.append(list1[number])
	return list2


list1 = [1,2,3,4]
list2 = ['a','b','c','d']
print(concantinate_two_list(list1,list2))
print(combine_two_list(list1,list2))
	


	