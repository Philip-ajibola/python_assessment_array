def check_element(list,element):
	for index in list:
		if element in list:
			return True;
		else:
			return False;

list = [12,34,55,66,74]
check = 66
check1 = 65

condition = check_element(list,check)
condition1 = check_element(list,check1)

if(condition):
	print(check,'is Present in the list')
else:
	print(check,'is not Present in the list')

if(condition1):
	print(check1,'is Present in the list')
else:
	print(check1,'is not Present in the list')