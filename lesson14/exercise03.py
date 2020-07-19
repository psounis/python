def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(n-1,i,-1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]


ar = [9,2,4,7,1,8,6,3]
bubble_sort(ar)
print(ar)