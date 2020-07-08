def print_list(l):
    if len(l) > 0:
        print(l[0], end=" ")
        print_list(l[1:])


def print_list2(l):
    if len(l) > 0:
        print_list2(l[1:])
        print(l[0], end=" ")


print_list([1,2,3])
print("")
print_list2([1,2,3])