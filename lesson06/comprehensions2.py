my_list = []
for number in range(10):
    if number % 2 == 0:
        my_list.append(number)
print(my_list)

my_list = [number for number in range(10) if number%2 == 0]
print(my_list)