
def print_multiplication_table(terms):

    print("Multiplication Table:")

    for i in range(1, terms + 1):

        for j in range(1, terms + 1):
            print(f"{i} x {j} = {i * j}\t", end="")
        print()


terms = int(input("Enter number of terms: "))
print_multiplication_table(terms)


