def fibonacci(n):
    def fib_rec(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib_rec(n - 1) + fib_rec(n - 2)

    if n < 0:
        return None
    else:
        return fib_rec(n)


for i in range(11):
    print(f"fibonacci({i})={fibonacci(i)}")