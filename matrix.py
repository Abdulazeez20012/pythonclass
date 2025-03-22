matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed)  



**Explanation:** The outer loop iterates over the columns (`i`), and the inner loop collects elements from each row (`row[i]`), effectively transposing the matrix.

