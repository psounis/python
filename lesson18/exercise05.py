class Customer:
    def __init__(self, full_name, address, orders=None):
        self.full_name = full_name
        self.address = address
        if orders is None:
            self.orders = []
        else:
            self.orders = orders

    def place_order(self, order):
        self.orders += [order]

    def __str__(self):
        st = f"Name: {self.full_name}, Address: {self.address}"
        st += "\n" + "-" * 35
        s = 0
        for order in self.orders:
            st += "\n" + str(order)
            s += order.payment.amount
        st += "\n" + "-" * 35
        st += f"\nTotal: {s}"
        return st


class Order:
    def __init__(self, date, payment):
        self.date = date
        self.payment = payment

    def __str__(self):
        return f"Date: {self.date}. Payment: {self.payment}"


class Payment:
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return str(self.amount)


class Credit(Payment):
    def __init__(self, amount, number, exp_date):
        super().__init__(amount)
        self.number = number
        self.exp_date = exp_date

    def __str__(self):
        return super().__str__() + ". CREDIT: Number: " + self.number + " Exp.Date" + self.exp_date


class Check(Payment):
    def __init__(self, amount, number, bank_code):
        super().__init__(amount)
        self.number = number
        self.bank_code = bank_code

    def __str__(self):
        return super().__str__() + ". CHECK: Number: " + self.number + " Bank Code" + self.bank_code


def main():
    c = Customer("Jim Psoun", "Papadaki 78")
    c.place_order(Order("20201020", Payment(12.12)))
    c.place_order(Order("20201021", Credit(22.12, "12937-2139883-388", "20231203")))
    c.place_order(Order("20201022", Check(32.12, "12389-123898-239", "3834720-98/3")))
    print(c)

main()