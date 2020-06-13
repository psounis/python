my_set = {number for number in range(3)}
print(my_set)

my_set = {number for number in range(10) if number%2 == 0}
print(my_set)

my_set = {number if number%2 == 0 else number/2
           for number in range(10)}
print(my_set)