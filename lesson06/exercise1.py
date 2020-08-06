my_list = []
for i in range(10):
    user_input = int(input("Give a number: "))
    while user_input < 10 or user_input > 20:
        user_input = int(input("Give a number(10...20): "))
    my_list.append(user_input)

print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)

list_squares = []
for i in range(10):
    list_squares.append(my_list[i]**2)

list_squares.sort()
tuple_squares = tuple(list_squares)
print(tuple_squares)
