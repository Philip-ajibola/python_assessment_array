def total_sum_for_forLoop(list):
	total = 0
	for number in range(len(list)):
		total+=list[number]
	return total

def total_sum_for_whileLoop(list):
	total = 0
	num=0
	while num<len(list):
		total+=list[num]
		num+=1
	return total

def total_sum_for_doWhileLoop(list):
	total = 0
	total+=list[0]
	number = 1
	while number<len(list):
		total+=list[number]
		number+=1
	return total

number = [1,2,3,4,5]
print(total_sum_for_forLoop(number))
print(total_sum_for_whileLoop(number))
print(total_sum_for_doWhileLoop(number))




