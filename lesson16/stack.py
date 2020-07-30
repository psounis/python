class Stack:
    def __init__(self):
        self.array = []

    def push(self,elem):
        self.array.append(elem)

    def pop(self):
        if not self.array:
            return None
        else:
            return self.array.pop()

    def length(self):
        return len(self.array)
    