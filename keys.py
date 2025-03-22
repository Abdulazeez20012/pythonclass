keys = ['a', 'b', 'c']
values = [1, 2, 3]

dictionary = {keys[i]: values[i] for i in range(len(keys))}
print(dictionary) 


**Explanation:** The `range(len(keys))` creates an index for iterating over both lists and pairing elements to form the dictionary.
