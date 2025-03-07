import string
class PunctuationRemover:
    def __init__(self):
        self.punctuation = string.punctuation

    def remove_special_punctuation(self, input_string: str) -> str:
       
        return ''.join(char for char in input_string if char not in self.punctuation)
