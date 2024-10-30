def print_multiplication_table(rows):
    i = 1
    while i <= rows:
        j = 1
        while j <= rows:
            print(f"{i} x {j} = {i * j}\t", end="")
            j += 1
        print()
        i += 1

rows = 10
print_multiplication_table(rows)