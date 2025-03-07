class WordWithCE:
    def __init__(self, word):
        self.word = word

    def insert_ce_in_middle(self):
        middle = len(self.word) // 2

        if len(self.word) % 2 == 0:
            return self.word[:middle] + "ce" + self.word[middle:]
        else:
            return self.word + "ce"
