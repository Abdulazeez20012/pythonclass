def print_multiplication_table(rows):
    for i in range(1, rows + 1):
        for j in range(1, rows + 1):
            print(f"{i} x {j} = {i * j}\t", end="")
        print()

rows = 10
print_multiplication_table(rows)





