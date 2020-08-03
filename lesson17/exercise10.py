from math import sqrt

class Cycle:
    def __init__(self, c):
        self.c = c

    def __str__(self):
        return f"x^2+y^2={c}^2"

    def __eq__(self, other):
        return self.c == other.c

    def __lt__(self, other):
        return self.c < other.c

    def __call__(self, x, y=None):
        if y is None:
            if isinstance(x, (int,float)):
                if abs(x) < self.c:
                    return (x,sqrt(self.c**2-x**2)), (x,-sqrt(self.c**2-x**2))
                elif abs(x) == self.c:
                    return (x, 0)
                else:
                    return None
        else:
            if isinstance(x, (int, float)):
                if x**2+y**2<self.c**2:
                    print(f"({x},{y}) is inside the cycle")
                elif x**2+y**2==self.c**2:
                    print(f"({x},{y}) is on the cycle")
                else:
                    print(f"({x},{y}) is outside the cycle")

cyc = Cycle(5)
print(cyc(3))
print(cyc(5))
print(cyc(7))
cyc(1,1)
cyc(5,0)
cyc(8,8)