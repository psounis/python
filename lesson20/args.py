def my_sum(*numbers):
    s = 0
    for number in numbers:
        s += int(number)
    return s
