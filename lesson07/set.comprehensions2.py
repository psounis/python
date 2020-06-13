my_set = set()

for i in range(2):
    for j in range(3):
        my_set.add((i,j))
print(my_set)

my_set = {(i, j) for i in range(2)
                 for j in range(3)}
print(my_set)