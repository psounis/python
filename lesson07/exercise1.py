N = 5

A = set()
for i in range(1,N+1):
    A.add(i)

print(A)

result = set()
for element in A:
    result.add((element, element**2))

print(result)