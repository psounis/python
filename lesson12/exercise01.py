def factorial(n):
    p = 1
    for i in range(2, n+1):
        p = p * i

    return p

for i in range(2, 50):
    print(factorial(i))