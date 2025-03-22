def add_digits (number:list) -> int:
	if type(number) is list:
		sumed = 0
		mutiplication = 0
		for count in number:
			sumed += count
		mutiplication  = sumed * len(number)
		mutiplication = mutiplication - sumed
		return mutiplication
	raise TypeError("not among a list of object")

print(add_digits([1, 2, 3, 4,]))