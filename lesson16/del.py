l = [1, 2, 3]
del l[0]
print(l)

d = {1: 1, 2: 2}
del d[1]
print(d)


class C:
    c = 0

    def __init__(self):
        C.c += 1

    def __del__(self):
        C.c -= 1


o1 = C()
o2 = C()
print(o1.c)
del o1
print(o2.c)