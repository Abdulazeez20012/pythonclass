#squares = [(x, x**2) for x in range(1, 4)]
#print(squares) 


#def addition_of_numbers(add):
 #return sum([x for x in add])

#add=1,9,2,3,7,4

#print(addition_of_numbers(add))




def remove_vowels(words):
 vowel="aeiouAEIOU"
 return [' '.join([char for char in words is chr not in vowel]) for wordn in words] 
words= "Orange","beans","ice","beans","rice"
print(remove_vowels(words))










