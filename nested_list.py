nested_list = [[1, 2, 3], [4, 5], [6, 7]]



flattened = [item for sublist in nested_list for item in sublist]
print(flattened)  


 The list comprehension includes two `for` loops: one for iterating over the outer list (`sublist`), and one for iterating over each element in the inner lists (`item`).
