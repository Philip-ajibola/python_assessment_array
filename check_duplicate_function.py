def check_duplicate(list):
	list1 = []
	numbers = len(list)-1
	checker = 0
	for number in range(len(list)):

		for number1 in range(number+1,len(list)):
			if list[number] == list[number1]:
				return print(f"{list[number]} has a duplicate")
	return print("no duplicate found")

			
name = ['apple','mango','banana','grape','banana']
check_duplicate(name)
	