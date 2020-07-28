# class.attribute.py
class C:
    counter = 0

    def __init__(self):
        C.counter += 1


o1 = C()
o2 = C()
print(C.counter, o1.counter, o2.counter)