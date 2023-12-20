
def largest_number(list):
	largest = list[0]
	for number in list:
		if number > largest:
			largest = number;
	return largest;


list= [1,2,3,4,5]
print('largest number is :', largest_number(list))
	
	