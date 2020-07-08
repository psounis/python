def C(n, k):
    if n == k:
        return 1
    elif k == 1:
        return n
    else:
        return C(n-1, k-1) + C(n-1, k)


print(C(49, 6))