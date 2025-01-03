def add_large_numbers(num1, num2):

    number1 = [0] * 40
    number2 = [0] * 40
    sum_digits = [0] * 40
    carry = 0

    for i in range(len(num1)):
        number1[39 - i] = int(num1[len(num1) - 1 - i])

    for i in range(len(num2)):
        number2[39 - i] = int(num2[len(num2) - 1 - i])


    for i in range(39, -1, -1):
        total = number1[i] + number2[i] + carry
        sum_digits[i] = total % 10
        carry = total // 10

    result = ""
    leading_zero = True
    for i in range(40):
        if sum_digits[i] != 0:
            leading_zero = False
        if not leading_zero:
            result += str(sum_digits[i])

  
    if leading_zero:
        return "0"
    
    return result

if __name__ == "__main__":
    num1 = input("Enter first huge number (up to 40 digits): ")
    num2 = input("Enter second huge number (up to 40 digits): ")

    result = add_large_numbers(num1, num2)

    print("Sum: " + result)
