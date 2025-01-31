class stackFunction:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def clear(self):
        self.stack.clear()
