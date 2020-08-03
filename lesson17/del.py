class A:
    def __init__(self, n):
        self.name = n
    def __del__(self):
        print(self.name + " destroyed")
        del self


def f():
    t = A("t")

f()

x = A("x")
del x
y = A("y")
z = y
print(z, y)
ar = [y, 2]
del y
print(ar,ar[0])