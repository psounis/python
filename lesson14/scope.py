def outer():
    x = 3

    def inner():
        x = 4
        print("inner x= " + str(x))

    inner()
    print("outer x= " + str(x))


x = 2
print("global x= " + str(x))
outer()