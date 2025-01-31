class arrayFunction:
    def __init__(self):
        self.array = []

    def add(self, item):
        self.array.append(item)

    def remove(self, item):
        if item in self.array:
            self.array.remove(item)
        else:
            return "Item not found"

    def get(self, index):
        if 0 <= index < len(self.array):
            return self.array[index]
        else:
            return "Index out of range"

    def contains(self, item):
        return item in self.array

    def size(self):
        return len(self.array)

    def clear(self):
        self.array.clear()
