def binary_search(array, x):
    def bs(array, x, start, finish):
        middle = (start + finish) // 2

        if start<=finish:
            if x == array[middle]:
                return middle
            elif x < array[middle]:
                return bs(array, x, start, middle-1)
            else: # x > array[middle]
                return bs(array, x, middle+1, finish)
        else:
            return -1

    return bs(array, x, 0, len(array)-1)

my_list = [i*i for i in range(10)]
print(my_list)
print(binary_search(my_list, 2))