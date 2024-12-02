def get_cube(number):
	if type(number) in [int, float]:
		return roud((number **3), 3)
	raise TypeError