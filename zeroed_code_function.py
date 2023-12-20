def zeroed_code(list):
	list1=[]
	for number in range(len(list)):
		if number == 0 or number == len(list)-1:
			list[number] = 0
		list1.append(list[number])
	return list1

#number = [1,2,3,4,5]
#print(zeroed_code(number))

		
		