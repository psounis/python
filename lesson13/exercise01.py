def f(x, y, z):
    return 2 * x**3 + 3 * x**2 * y + y ** 2 * z + 1


print(f(5, 2, 3))
print(f(y=2,z=3,x=5))
print(f(5,z=3,y=2))
print(f(5,2,z=3))