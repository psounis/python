my_set = set()

for i in range(6):
    if i%2==0:
        for j in range(6,10):
            if j%2==1:
                my_set.add((i,j))
print(my_set)

my_set = {(i, j) for i in range(6) if i%2==0
                 for j in range(6,10) if j%2==1}
print(my_set)