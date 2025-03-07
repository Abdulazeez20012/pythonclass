class StringSwapper:
    def __init__(self, string1, string2):
        self.string1 = string1
        self.string2 = string2

    def swap_first_two_chars(self):
        if len(self.string1) < 2 or len(self.string2) < 2:
            return "Both strings must have at least two characters."

       
        swapped_string1 = self.string2[:2] + self.string1[2:]
        swapped_string2 = self.string1[:2] + self.string2[2:]

        
        return swapped_string1 + " " + swapped_string2
