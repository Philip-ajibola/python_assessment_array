def check_string_is_palindrome(list):
	list1 = []
	list2 = []
	reversed = ""
	for number in range(len(list)):
		list1 = list[number]
		num =len(list1)-1 
		while num>=0:
			reversed +=""+list1[num]
			num-=1
		list2.append(reversed)
	if list == list2:
		print(f'{list[number]} is a palindrome')
		return True

	print(f'{list[number]} is not a palindrome')
	return False

name = ['mumu']
check_string_is_palindrome(name)
