def factory(a,b,c):
    def polynomial(x):
        return a*x**2 + b*x + c

    return polynomial


pol = factory(1,1,1)
print(pol(1))