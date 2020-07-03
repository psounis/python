def f(arg):
    print(arg)
    print(f"id arg={id(arg)}")
    arg = [3]
    print(arg)
    print(f"id arg={id(arg)}")

l = [1,2]
print(l)
print(f"id l={id(l)}")
f(l)
print(l)
print(f"id l={id(l)}")


arg = [r1]