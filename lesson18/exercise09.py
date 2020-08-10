from random import randrange, seed
from datetime import datetime
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, full_name, salary):
        self.full_name = full_name
        self.salary = salary
        self.served_cnt = 0

    def report(self):
        print(self.full_name + " served " + str(self.served_cnt) +  " customers.")

class Waiter(Person):
    def __init__(self, full_name, salary):
        Person.__init__(self, full_name, salary)

    def serve(self, customers, barista):
        self.served_cnt += customers
        print("Waiter " + self.full_name + " served " + str(customers) + " customers")
        barista.prepare(customers)


class Barista(Person):
    def __init__(self, full_name, salary):
        Person.__init__(self, full_name, salary)

    def prepare(self, customers):
        print("Barista " + self.full_name + " served " + str(customers) + " customers")
        self.served_cnt += customers


class Owner(Waiter, Barista):
    def __init__(self, full_name, salary):
        Person.__init__(self, full_name, salary)



def main():
    seed(datetime.now())

    o = Owner("owner", 100000)
    w1 = Waiter("waiter-1", 200000)
    w2 = Waiter("waiter-1", 200000)
    b = Barista("barista", 300000)

    waiters = [o, w1, w2]
    baristas = [o, b]

    for _ in range(10):
        waiters[randrange(3)].serve(randrange(1,5+1), baristas[randrange(2)])

    print("")
    o.report()
    w1.report()
    w2.report()
    b.report()

main()

