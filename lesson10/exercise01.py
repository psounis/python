subsets = set()
N=4

for i in range(1,N+1):
    for j in range(i+1,N+1):
        subsets.add(frozenset({i,j}))

print(subsets)