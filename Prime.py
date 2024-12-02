number = int(input("Enter number"))
for i in range (2,number) :
	if number % i == 0 :
		print("false")
break
for j in range (2,number):
	if number % i !=0:
		print("True")
break

