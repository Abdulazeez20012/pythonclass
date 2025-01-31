class my_encrypt:

    def encrypt_text(input_text):
        result = ""

        for char in input_text:
            if 'a' <= char <= 'z':
                new_char = chr(((ord(char) - ord('a') + 13) % 26) + ord('a'))
                result += new_char
            elif 'A' <= char <= 'Z':
                new_char = chr(((ord(char) - ord('A') + 13) % 26) + ord('A'))
                result += new_char
            else:
                result += char

        return result