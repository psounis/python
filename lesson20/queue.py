class Queue:
    def __init__(self):
        self.array = []

    def enqueue(self, elem):
        self.array.append(elem)

    def dequeue(self):
        if not self.array:
            return None
        else:
            return self.array.pop(0)

    def __str__(self):
        return ", ".join(self.array)

    def __add__(self, other):
        new_q = Queue()
        new_q.array = self.array[:]
        new_q.enqueue(other)
        return new_q

    def __iadd__(self, other):
        self.enqueue(other)
        return self

    def __neg__(self):
        return self.dequeue()

    def __len__(self):
        return len(self.array)