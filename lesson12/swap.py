def swap(a,b):
    tmp = a
    a = b
    b = tmp
    return a,b


a = 3
b = 4
print(f"a={a}, b={b}")
print(type(swap(a, b)))
a, b = swap(a, b)
print(f"a={a}, b={b}")

a = 3
b = 4
a,b = (b,a)
print(f"a={a}, b={b}")

a = 3
b = 4
a,b = b,a
print(f"a={a}, b={b}")
