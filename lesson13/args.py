def my_sum(*numbers):
    print(numbers)
    s = 0
    for number in numbers:
        print(number)
        s += int(number)
    return s

print(f"sum={my_sum(1,2,3,4,5)}")
