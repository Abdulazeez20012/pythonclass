def square_odd_number(): 
 numbers =[10,3,7,1,9,4,2,8,5,6] 
 return[x**2 for x in numbers if x % 2 !=0]


print(square_odd_number())
