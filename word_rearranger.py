class WordRearranger:
    def __init__(self, word):
        self.word = word

    def rearrange_case(self):
        upper_case = [char for char in self.word if char.isupper()]
        lower_case = [char for char in self.word if char.islower()]

        return ''.join(upper_case + lower_case)