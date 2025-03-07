class CharacterFrequency:
    def __init__(self, input_string):
        self.input_string = input_string

    def count_characters(self):
        char_count = {}
        for char in self.input_string:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        return char_count
