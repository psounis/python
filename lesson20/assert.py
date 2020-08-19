def my_sum(sth):
    s = 0
    for item in sth:
        s += item
    return s


assert my_sum((1,2,3)) == 6
assert my_sum([1,2,3]) == 6
assert my_sum({1,2,3}) == 6