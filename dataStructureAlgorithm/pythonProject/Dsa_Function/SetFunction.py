class SetFunction:
    def __init__(self):
        self.set = set()
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def add(self, item):
        self.set.add(item)
        self.size += 1