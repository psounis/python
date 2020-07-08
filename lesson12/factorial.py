def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

for i in range(1,11):
    print(f"factorial({i})={factorial(i)} ")