N = 10

subsets = set()
subsets.add(frozenset())

for i in range(1,N+1):
    new_subsets = set()
    for subset in subsets:
        nonfz = set(subset)
        nonfz.add(i)
        fz = frozenset(nonfz)
        new_subsets.add(fz)
    subsets.update(new_subsets)

print(subsets)
print(len(subsets))
