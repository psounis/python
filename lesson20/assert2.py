def my_avg(sth):
    assert len(sth)!=0, "iterable is empty!"
    s = 0
    for item in sth:
        s += item
    return s/len(sth)

print(my_avg(()))

