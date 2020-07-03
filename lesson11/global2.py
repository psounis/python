def f():
    global x
    x = 3
    print(x)

x = 2
f()
print(x)