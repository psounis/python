array = [[1,2,3], [4,5,6]]
array[0][1] = 0
for row in array:
    for elem in row:
        print(elem, end=" ")
    print("")
