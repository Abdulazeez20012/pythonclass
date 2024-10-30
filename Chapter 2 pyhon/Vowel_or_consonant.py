def vowel_or_consonant(ch):

    if ch.lower() in 'aeiou':
        return "vowel"
    elif ch.isalpha():
        return "consonant"
    else:
        return "error"

while True:
    ch = input("Enter a single character (a-z or A-Z): ")

    if len(ch) != 1:
        print("Error: Please enter a single character.")
    else:
        result = vowel_or_consonant(ch)
        if result == "error":
            print("Error: Please enter a letter (a-z or A-Z).")
        else:
            print(f"{ch} is a {result}.")
            break

