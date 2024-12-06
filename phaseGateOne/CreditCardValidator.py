def luhn_check(card_number):
    total_sum = 0
    reverse_digits = card_number[::-1]

    for i in range(len(reverse_digits)):
        digit = int(reverse_digits[i])


        if i % 2 == 1:
            digit *= 2
            if digit > 9:  
                digit -= 9
        total_sum += digit

   
    return total_sum % 10 == 0


def card_type(card_number):
    if card_number[0] == '4':
        return "Visa"
    elif card_number[0] == '5':
        return "MasterCard"
    elif card_number[:2] == '37':
        return "American Express"
    elif card_number[0] == '6':
        return "Discover"
    else:
        return "Invalid Card"


def main():
    print("Enter credit card number:")
    card_number = input() 

    card_length = len(card_number)
    valid = luhn_check(card_number) 
    card_type_result = card_type(card_number)  


    print(f"\nCredit Card Type: {card_type_result}")
    print(f"Credit Card Number: {card_number}")
    print(f"Credit Card Digit Length: {card_length}")
    print(f"Credit Card Validity Status: {'Valid' if valid else 'Invalid'}")


if __name__ == "__main__":
    main()
