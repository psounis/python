from linked_list import LinkedList
from random import randrange

class OrderedList(LinkedList):
    def __init__(self):
        super().__init__()

    def insert(self, data):
        if self.empty():
            self.insert_start(data)
        elif data < self.head.data:
            self.insert_start(data)
        else:
            prev = self.head
            cur = self.head.next
            while cur is not None:
                if data < cur.data:
                    self.insert_after(prev,data)
                    return
                else:
                    prev = cur
                    cur = cur.next
            else:
                self.insert_after(prev, data)

    def delete(self, data):
        if self.empty():
            return None
        elif self.head.data == data:
            return self.delete_start()
        else:
            prev = self.head
            cur = self.head.next
            while cur is not None:
                if data == cur.data:
                    return self.delete_after(prev)
                else:
                    prev = cur
                    cur = cur.next
            else:
                return None


l = LinkedList()
for i in range(4,-1,-1):
    l.insert_start(i)
print(l)

l.insert_after(l.head.next.next, 5)
print(l)

print(l.delete_start())
print(l)

print(l.delete_after(l.head.next))
print(l)

print("-" * 20)

ol = OrderedList()

for i in range(50):
    val = randrange(10)
    if i%2 == 0:
        ol.insert(val)
        print(f"inserted {val}.")
    else:
        ret = ol.delete(val)
        if ret is None:
            print(f"Deleting... {val} not found!")
        else:
            print(f"Deleted {val}")
    print(ol)

