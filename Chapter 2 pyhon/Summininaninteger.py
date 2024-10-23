num = int(input("Please enter an integer between 0 and 1000: "))
if 0 <= num <= 1000:
  
    digit_sum = 0
    while num != 0:
        last_digit = num % 10  
        digit_sum += last_digit     
        num = num // 10
    print(f"The sum of the digits is: {digit_sum}")

