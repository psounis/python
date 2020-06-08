array = []
rows = int(input("Give number of rows: "))
cols = int(input("Give number of columns: "))

for i in range(rows):
    array.append([])
    for j in range(cols):
        elem = int(input("Give " + str(i) + "," + str(j) + " element: "))
        array[i].append(elem)

print(array)