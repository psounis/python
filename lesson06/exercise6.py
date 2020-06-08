array = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2]
]

array.insert(0, [0, 0, 0, 0])

for row in array:
    for elem in row:
        print(elem, end=" ")
    print("")

for row in array:
    row.append(1)

print("")
for row in array:
    for elem in row:
        print(elem, end=" ")
    print("")
