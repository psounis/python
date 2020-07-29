class Person:
    def __init__(self, full_name, age, id_number):
        self.full_name = full_name
        self.age = age
        self.id_number = id_number


class Account:
    def __init__(self, number, owner, amount):
        self.number = number
        self.owner = owner
        self.amount = amount

    def transfer_to(self, account, amount):
        if amount <= self.amount:
            self.amount -= amount
            account.amount += amount
            print(self.owner.full_name + " transfered " + str(amount) + " to " + account.owner.full_name)
        else:
            print("Not enough credit!")


p1 = Person("Bob Hope", "dead", "13219398")
p2 = Person("Donald Trump", 75, "02139484")
a1 = Account("132489480328", p1, 123878.23)
a2 = Account("213094809328", p2, 12388902993.99)
a1.transfer_to(a2,100000)