def reverse_list(list):
	return list[::-1]

list = [5,6,7,8,9,10]
print(f'the reverse of{list} is {reverse_list(list)}')


def reverse_list1(list):
	list1 = []
	#number =  len(list)-1
	#number2 = 0
	for numbers in range(len(list)-1,-1):
		list1.append(list[numbers])
		#number-=1
		#number2+=1
	return list1
list = [5,6,7,8,9,10]
print(f'the reverse of{list} is {reverse_list1(list)}')