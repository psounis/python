from random import seed
from random import randrange
from datetime import datetime  # all 3 at the beginning

seed(datetime.now())  # once, before randint call

numbers = {}
N = 10

for i in range(1,6+1):
    numbers[i] = 0

for _ in range(N):
    num = randrange(1, 6+1)
    numbers[num] += 1

for i in range(1,6+1):
    print(str(i) + ": " + str(numbers[i]/N))

