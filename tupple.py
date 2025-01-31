numbers = (1,2,3,4,5)

print(numbers)

numbers = [1,2,3,4,5]
numbers[2]= 9
print(numbers)




my_tuple = (1,2,"Esther",[1,4,9])
my_tuple[3][1] = 59
print(my_tuple)
print(my_tuple[0])
print(my_tuple[1])


print()
mixed_tuple = (1,"Esther",3.14,[10,20,30],"divine")
mixed_tuple[3][2] = 50
print(mixed_tuple)



x = (1,2,9)  
y = (2,5,8)
print(x+y)
print(y * 3)

print(x * 3)


x = ('a','p','p','i','e')

print(x.count('p'))
print(x.index('e'))

print(x.count('e'))

print()

print('i' in x)


names = ("Mario","Sb","oj-Skills","Kenny","Emmanuel","Az")
for name in names:
 	print("Hello",name)
print()

for o,b in enumerate(names):
	print(o,b)




number = ("",[],1,3,(1,3,1))
all(number)
print(number)

thistuple = ("apple", "banana", "cherry")
print(thistuple[2:0])

