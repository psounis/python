from random import seed
from random import randrange
from datetime import datetime  # all 3 at the beginning

seed(datetime.now())  # once, before randint call

for _ in range(10):
    column = set()

    # 10-19

    rand_number = randrange(10,20)
    column.add(rand_number)

    while True:
        rand_number = randrange(10,20)
        if rand_number not in column:
            column.add(rand_number)
            break

    # 20-39

    rand_number = randrange(20,40)
    column.add(rand_number)

    while True:
        rand_number = randrange(20,40)
        if rand_number not in column:
            column.add(rand_number)
            break

    # 1 - 9

    rand_number = randrange(1,10)
    column.add(rand_number)


    # 40 - 49

    rand_number = randrange(40,50)
    column.add(rand_number)

    print(column)