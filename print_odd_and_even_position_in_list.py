def odd_position(list):
	list1 = []
	for number in range(0,len(list),2):
		list1.append(list[number])
	return list1

list = [1,2,3,4,5,6,7]
print(odd_position(list))
			
def even_position(list):
	list1 = []
	for number in range(1,len(list),2):
		list1.append(list[number])
	return list1

list = [1,2,3,4,5,6,7]
print(even_position(list))