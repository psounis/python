class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def empty(self):
        return self.head is None

    def insert_start(self, data):
        n = Node(data)
        n.next = self.head
        self.head = n

    def insert_after(self, prev, data):
        n = Node(data)
        n.next = prev.next
        prev.next = n

    def delete_start(self):
        if self.empty():
            return None
        else:
            c = self.head
            self.head = self.head.next
            return c.data

    def delete_after(self, prev):
        if prev.next is None:
            return None
        else:
            c = prev.next
            prev.next = c.next
            return c.data

    def __str__(self):
        p = self.head
        st = ""
        while p is not None:
            st += str(p.data) + "-->"
            p = p.next
        st += "."
        return st

