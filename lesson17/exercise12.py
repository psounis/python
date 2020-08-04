from queue import Queue
from random import randrange, seed
from datetime import datetime

class Bank:
    def __init__(self, N):
        self.N = N
        self.cash_desks = [Queue() for i in range(N)]

    def customer_enters(self, full_name):
        cash_desk = randrange(self.N)
        self.cash_desks[cash_desk] += full_name
        print(full_name + " entered! To be served by cash desk: " + str(cash_desk))

    def customer_served(self):
        not_empty_cash_desks = [i for i in range(self.N) if len(self.cash_desks[i]) > 0]

        if len(not_empty_cash_desks) > 0:
            cash_desk = not_empty_cash_desks[randrange(len(not_empty_cash_desks))]
            customer = - self.cash_desks[cash_desk]
            print(f"{customer} served by cash desk {cash_desk}")
        else:
            print("No customers.")

    def __str__(self):
        st = "\n" + "=" * 20
        for i in range(self.N):
            st += "\nCash Desk " + str(i) +": "
            st += str(self.cash_desks[i])
        st += "\n" + "=" * 20
        return st


def main():
    seed(datetime.now())

    bank = Bank(3)

    for i in range(100):
        num = randrange(100)
        if num <=29:
            bank.customer_served()
        else:
            bank.customer_enters("Cust" + str(randrange(1000)))

        if i % 10 == 0:
            print(bank)

    print("BANK CLOSED")

main()