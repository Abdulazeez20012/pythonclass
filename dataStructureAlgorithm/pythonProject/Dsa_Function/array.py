class Array:
    def __init__(self):
        self.array = []
        self._size = 0

    def add(self, element):
        self.array.append(element)
        self._size += 1

    def remove(self, element):
        if element in self.array:
            self.array.remove(element)
            self._size -= 1

    def get(self, index):
        if 0 <= index < self._size:
            return self.array[index]
        return "Index out of range"

    def contains(self, element):
        return element in self.array

    def size(self):
        return self._size

    def clear(self):
        self.array = []
        self._size = 0
