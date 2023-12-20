def sum_total(list):
	total=0
	for number in range(len(list)):
		total+=list[number]
	return total

list = [10,12,14,16,18]
print(sum_total(list))