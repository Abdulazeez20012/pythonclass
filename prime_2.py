def is_prime(num):
	if num <2:
		return "number must be greater that 1"
	if num== 2:
		return True
	
	for value in range(3,num): 
		if num % value == 0 :
			find_out = num % value
				print("A before False", find_out)
	return False
				print("After False", find_out)
	return True
			
			return False
	return True

number = input(input("slot in a number: "))

print(is_prime(number))