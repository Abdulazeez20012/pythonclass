def divide_or_square(azeez):

	result = 0
   
    if not isinstance(azeez, (int, float)):
        raise ValueError("Input must be a number.")
    
    if azeez < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    
    if azeez % 5 == 0:

        return round(math.sqrt(azeez), 2)
    else:
        return azeez % 5


