dict1 = {v:v**2 for v in range(10)}
print(dict1)

dict2 = {v:v**2 for v in range(10) if v%2==0}
print(dict2)

dict3 = {(i, j): 0 for i in range(1,7)
                   for j in range(1,7)}
print(dict3)