my_list = []
for number in range(10):
    user_input = int(input("Give " + str(number) + ": "))
    my_list.append(user_input)

my_tuple = tuple(my_list)

list_squares = []
for element in my_tuple:
    list_squares.append(element ** 2)

tuple_squares = tuple(list_squares)
print(tuple_squares)