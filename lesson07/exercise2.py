from random import seed
from random import randrange
from datetime import datetime  # all 3 at the beginning

seed(datetime.now())  # once, before randint call

i = 0
columns = []
while True:
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

    # 1-9 EVEN

    rand_number = 2 * randrange(1,5)
    column.add(rand_number)

    # 41-49 ODD

    rand_number = randrange(41,49+1,2)
    column.add(rand_number)

    if column not in columns:
        columns.append(column)
        i += 1
        if i==10:
            break


for column in columns:
    print(column)
