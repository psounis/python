def square(x):
    return x*x


def cube(x):
    return x**3


def f(x):
    return 3*cube(x)+4*square(x)+x+1


print("  x : ", end="")
for i in range(10):
    print("| " + str(i).center(6), end="")
print("|\nf(x): ", end="")
for i in range(10):
    print("| " + str(f(i)).center(6), end="")
print("|")