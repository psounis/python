my_list = [number for number in range(10) if number % 2 == 0]
print(my_list)
my_set = set(my_list)
print(my_set)
my_set.discard(2)
print(my_set)
my_set.remove(2)
print(my_set)
